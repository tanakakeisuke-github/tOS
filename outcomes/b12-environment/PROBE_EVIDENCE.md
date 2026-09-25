# B-12 read-isolation preflight

Date: 2026-09-25 JST. No exam was run and no repository document was sent to a model.

Installed CLI: /Applications/ChatGPT.app/Contents/Resources/codex, version codex-cli 0.155.0-alpha.9.

Inherited security metadata (not changed): CODEX_PERMISSION_PROFILE=:workspace; CODEX_SANDBOX=seatbelt; CODEX_SANDBOX_NETWORK_DISABLED=1.

A harmless sandbox probe was run via normal require_escalated approval to avoid forbidden nested Seatbelt application. It kept inherited security metadata intact:

```
codex sandbox -P b12_probe -C /private/tmp/tos-b12-env-investigation/fixture \
 -c 'permissions.b12_probe.filesystem={":root"="deny",":minimal"="read","/private/tmp/tos-b12-env-investigation/fixture"="read","/private/tmp/tos-b12-env-investigation/blocked.txt"="deny"}' \
 -c 'permissions.b12_probe.network.enabled=false' \
 /bin/sh -c 'cat allowed.txt; cat ../blocked.txt'
```

Observed exit 0, stdout:

```
allowed-dummy
blocked-dummy
```

Conclusion: even root-deny plus exact-file-deny did not enforce the expected read isolation in this invocation. This runner must not be used for B-12 on the strength of its configuration alone. The cause remains unproven. The inherited :workspace permission metadata is a possible factor, not an established root cause. No inherited policy was unset, changed, or bypassed.

Official docs checked:
- https://learn.chatgpt.com/docs/permissions : custom permission profiles do not compose with legacy sandbox configuration; older sandbox settings can take precedence. More-specific filesystem entries should override broader entries.
- https://learn.chatgpt.com/docs/config-file/config-reference : features.shell_tool controls default shell; tools.view_image controls local image reads; mcp_servers.<id>.enabled_tools allows individual MCP tool names.

Potential alternative (NOT validated or deployed): immutable virtual-file reader exposing only manifest keys, returning preloaded fixture strings, with append-only operation logging; shell, image, browser, app, plugins, other MCP, memories, skills, and delegation disabled. However, official documentation and the local feature catalog do not establish an authoritative allow-only-tools switch for all native tools (including apply_patch). Merely asking the model to obey the reader is insufficient proof. This alternative requires tool-inventory verification and adversarial dummy probes before real exam documents are introduced.

Recommended bounded handoff: run the exact dummy probe in a fresh, independently configured worker host or isolated VM/container with only fixture mounted; confirm allowed read, denied traversal, denied outside file, denied writes and network; capture CLI/model metadata and all tool operations. Do not count B-12 complete until that environment gate passes and the actual exam is separately run and reviewed.

## Additive direct Seatbelt probe

`dummy.sb` denies reading the investigation directory, reopens only `fixture/`, denies all writes and all network access, while leaving other inherited behavior unchanged. Ran via normal approved escalation:

```
/usr/bin/sandbox-exec -f /private/tmp/tos-b12-env-investigation/dummy.sb /bin/sh -c 'cat /private/tmp/tos-b12-env-investigation/fixture/allowed.txt; cat /private/tmp/tos-b12-env-investigation/fixture/../blocked.txt'
```

Observed exit 1:

```
allowed-dummy
cat: /private/tmp/tos-b12-env-investigation/fixture/../blocked.txt: Operation not permitted
```

This positively verifies that a direct additive Seatbelt denial can enforce the forbidden-file/traversal boundary on this host, unlike the Codex profile probe above. `dummy.sb` is a primitive proof, NOT full fixture-only isolation: it deliberately permits reads elsewhere. A stronger deny-all profile `dummy-strict.sb` reopening system runtime trees and fixture failed with exit 134 and no output; this is not a usable approved-read boundary yet.

A whole-CLI wrapper using explicit deny subpaths may be practical, but remains untested. It would require exhaustive exclusion of unrelated material, automatic-context audit, and confirming all aliases/links and tool processes are within the wrapper. Do not infer successful model identity, authentication, all tool confinement, or actual B-12 execution from these shell-only tests.

## Final bounded conclusion

Root-agent experiment (reported by root, not independently rerun here): `runtime.sb`, with global `file-read-data` denial and exceptions for system runtime roots and the fixture, also aborted with exit 134.

Preserved observations:
- Codex permission profile with root deny and exact blocked-file deny: FAIL; both harmless files readable.
- Direct additive Seatbelt subtree deny with fixture exception: PASS for allowed read and traversal-to-blocked-file denial only.
- Direct global `file-read*` deny with runtime/fixture exceptions (`dummy-strict.sb`): FAIL to start; exit 134.
- Root global `file-read-data` deny with runtime/fixture exceptions (`runtime.sb`): FAIL to start; exit 134 (root-reported).
- MCP-only runner: not implemented or validated; comprehensive removal of alternative native access tools not proven.

Final environment gate: NOT MET. Full worker isolation remains unverified. No actual B-12 exam was started in this investigation. No configured model identity was verified through a worker run. The next requirement is a functioning worker environment that positively permits the approved fixture, rejects outside/traversal reads and unauthorized writes, disables external retrieval, audits initial context/tool exposure, and records model identity and operations before any exam input is introduced. A successful narrow sandbox primitive is insufficient to claim this gate passed.
