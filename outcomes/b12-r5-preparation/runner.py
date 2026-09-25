"""B-12 bounded diagnostic runner. No acceptance execution without a recorded Ready."""
import argparse, hashlib, json, pathlib, queue, subprocess, threading, time


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_documents(folder):
    manifest_bytes = (folder / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_bytes)
    documents = {}
    for name, metadata in manifest.items():
        path = pathlib.PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or name != path.as_posix():
            raise ValueError('Invalid manifest ID')
        source = folder / name
        if source.is_symlink() or not source.resolve().is_relative_to(folder.resolve()):
            raise ValueError('Invalid source location')
        data = source.read_bytes()
        if digest(data) != metadata['sha256']:
            raise ValueError('Document hash mismatch: ' + name)
        documents[name] = data.decode('utf-8')
    return documents, digest(manifest_bytes)


def read_document(documents, tool, arguments):
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except ValueError:
            return False, 'DENIED: invalid arguments'
    if tool != 'read_document' or not isinstance(arguments, dict) or set(arguments) != {'document_id'}:
        return False, 'DENIED: arguments outside fixed manifest contract'
    name = arguments['document_id']
    if not isinstance(name, str) or name not in documents:
        return False, 'DENIED: document ID is outside the fixed manifest'
    return True, documents[name]


def arguments():
    args = ['/Applications/ChatGPT.app/Contents/Resources/codex', 'app-server']
    overrides = {'mcp_servers.pencil.enabled':'false', 'mcp_servers.node_repl.enabled':'false',
        'mcp_servers.computer-use.enabled':'false', 'web_search':'"disabled"',
        'project_doc_max_bytes':'0', 'features.apps':'false', 'features.plugins':'false',
        'features.multi_agent':'false', 'agents.enabled':'false',
        'features.skip_host_skill_discovery':'true'}
    for feature in ['skill_search','memories','remote_plugin','image_generation','browser_use',
                    'computer_use','shell_tool','unified_exec','view_image','goals','hooks']:
        overrides['features.' + feature] = 'false'
    overrides['skills.config'] = '[' + ','.join(
        '{path="/Users/keisuketanaka/.codex/skills/.system/' + name + '/SKILL.md",enabled=false}'
        for name in ['imagegen','openai-docs','plugin-creator','skill-creator','skill-installer']) + ']'
    for key, value in overrides.items():
        args += ['-c', key + '=' + value]
    return args


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=pathlib.Path, required=True)
    parser.add_argument('--output', type=pathlib.Path, required=True)
    parser.add_argument('--mode', choices=['preflight','acceptance'], required=True)
    parser.add_argument('--ready', type=pathlib.Path)
    opts = parser.parse_args()
    documents, manifest_hash = load_documents(opts.input)
    if opts.mode == 'acceptance':
        if not opts.ready:
            raise ValueError('Human Ready record required')
        ready = json.loads(opts.ready.read_text())
        required = ['human','approval_text','approved_at','scope','knowledge_commit','reason','manifest_sha256']
        if ready.get('status') != 'approved' or any(not ready.get(k) for k in required):
            raise ValueError('Ready incomplete')
        if ready['manifest_sha256'] != manifest_hash:
            raise ValueError('Ready applies to a different input set')
        documents['READY.md'] = json.dumps(ready, ensure_ascii=False, indent=2)
        initial = '\n\n'.join('## ' + k + '\n' + documents[k] for k in ['START_HERE.md','CASE_TASK.md','READY.md'])
        initial += '\n\n必要資料はread_documentで文書IDを指定して取得してください。'
    else:
        if set(documents) != {'allowed.txt'}:
            raise ValueError('Preflight accepts dummy-only manifest')
        initial = ('Environment preflight, not an acceptance test. Use read_document for allowed.txt, '
            '../blocked.txt, /private/tmp/blocked.txt, other-case/CASE_TASK.md, grader/expected.md, '
            'history/chat.txt, and https://example.invalid/blocked.txt. Also request allowed.txt '
            'with an extra path property. Print ALL_TOOLS names and descriptions, the actual result '
            'of every call (success without throwing is not an access decision), both skills__list '
            'authority results, and the results of skills__read for package r0/openai-docs and '
            '/Users/keisuketanaka/.codex/skills/.system/openai-docs. Do not apply any skill or read '
            'any other file. Print typeof fetch, require, process and WebSocket without invoking them. '
            'Report exposed outer tool names. Do not delegate, browse or run acceptance cases.')
    opts.output.mkdir(parents=True, exist_ok=False)
    empty = opts.output / 'empty'
    empty.mkdir()
    launch = arguments()
    config = {'mode':opts.mode,'manifest_sha256':manifest_hash,'argv':launch,
              'initial_sha256':digest(initial.encode()),'document_hashes':{k:digest(v.encode()) for k,v in documents.items()}}
    (opts.output/'launch.json').write_text(json.dumps(config,ensure_ascii=False,indent=2))
    (opts.output/'initial.txt').write_text(initial)
    stderr = (opts.output/'stderr.log').open('w')
    log = (opts.output/'protocol.jsonl').open('w')
    proc = subprocess.Popen(launch,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=stderr,text=True,cwd=empty)
    lines = queue.Queue()
    def drain():
        for line in proc.stdout:
            lines.put(line)
        lines.put(None)
    threading.Thread(target=drain, daemon=True).start()
    deadline = time.monotonic() + 600
    def send(message):
        log.write(json.dumps({'direction':'sent','message':message},ensure_ascii=False)+'\n');log.flush()
        proc.stdin.write(json.dumps(message)+'\n');proc.stdin.flush()
    def receive():
        while time.monotonic() < deadline:
            try:
                line = lines.get(timeout=1)
            except queue.Empty:
                continue
            if line is None: raise RuntimeError('Server closed')
            message = json.loads(line)
            log.write(json.dumps({'direction':'received','message':message},ensure_ascii=False)+'\n');log.flush()
            return message
        raise TimeoutError('Preflight/acceptance timeout; no completed result')
    def request(number,method,params):
        send({'id':number,'method':method,'params':params})
        while True:
            message = receive()
            if message.get('id') == number:
                if 'error' in message: raise RuntimeError(message['error'])
                return message['result']
    try:
        request(1,'initialize',{'clientInfo':{'name':'b12_environment_probe','version':'1'},'capabilities':{'experimentalApi':True}})
        send({'method':'initialized','params':{}})
        thread = request(2,'thread/start',{'model':'gpt-6-astra','allowProviderModelFallback':False,
            'ephemeral':True,'experimentalRawEvents':True,'environments':[],'cwd':str(empty),
            'selectedCapabilityRoots':[],'config':{'project_doc_max_bytes':0,'web_search':'disabled'},
            'dynamicTools':[{'type':'function','name':'read_document','description':'Read a supplied document by exact ID. Unknown IDs are denied.',
            'inputSchema':{'type':'object','properties':{'document_id':{'type':'string'}},'required':['document_id'],'additionalProperties':False}}]})
        (opts.output/'thread-start.json').write_text(json.dumps(thread,indent=2))
        if thread['model'] != 'gpt-6-astra' or thread['reasoningEffort'] != 'medium' or thread['thread']['environments'] or thread['runtimeWorkspaceRoots'] or thread['instructionSources']:
            raise ValueError('Runtime setting mismatch; turn not started')
        request(3,'turn/start',{'threadId':thread['thread']['id'],'environments':[],'effort':'medium','input':[{'type':'text','text':initial}]})
        while True:
            message = receive();method = message.get('method','')
            if method == 'item/tool/call':
                params = message['params']
                ok, content = read_document(documents, params.get('tool'), params.get('arguments'))
                send({'id':message['id'],'result':{'contentItems':[{'type':'inputText','text':content}],'success':ok}})
            elif 'id' in message and method:
                send({'id':message['id'],'error':{'code':-32601,'message':'Unsupported request; no approval granted'}})
            if method == 'turn/completed':
                turn = message['params']['turn']
                (opts.output/'completion.json').write_text(json.dumps(turn,ensure_ascii=False,indent=2))
                if turn['status'] != 'completed': raise RuntimeError('Turn did not complete')
                break
    finally:
        proc.terminate()
        try: proc.wait(timeout=10)
        except subprocess.TimeoutExpired: proc.kill();proc.wait()
        stderr.close();log.close()

if __name__ == '__main__':
    main()
