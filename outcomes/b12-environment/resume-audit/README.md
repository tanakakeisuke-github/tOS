# B-12 再開時の取得経路・監査確認

2026-09-25 JST。**環境未成立。改訂後P/M/Uは未実施・未採点、Ready未固定。** 本記録は環境の自己確認であり、独立Review・Human受入は未実施。

## 基準と今回の変更

再開時にGitHubからIssue #25の本文・全4コメント、PR #26の状態・head・コメント、指定ブランチの `bootstrap/NEXT_SESSION.md` 全文を確認した。PR #26はOPEN/Draft、headは `0f53d8f8124d15bd2bdbc099a7461af2fc6939f7`。PR #28はMERGEDで、承認済みKnowledgeの基準は `7ab8b092544f6f00b8ca8d791ed6473cfef6cd43`。Issue本文の旧Readyを改訂後のReadyとは扱わない。

前回probe3と同じCodex `0.155.0-alpha.9`、要求 `gpt-6-astra` / `medium`、代替禁止、新規ephemeral session、`environments: []`、固定ID Readerを維持。変更は `experimentalRawEvents: true` と、Skill一覧・ダミー読取の実呼出を加えた診断入力。旧会話、実tOS資料、P/M/U設問・期待回答は送信していない。ユーザー設定ファイル・安全設定は変更していない。

ローカルCLIの生成schemaでrawイベント設定を確認した。公式仕様の入口は [Codex App Server](https://learn.chatgpt.com/docs/app-server)。設定の存在と下記の実測を根拠とし、公式ページだけで全経路隔離を認定しない。

最初の起動は調整側sandboxからCodexの通常状態DBを初期化できず、initialize前に終了。その後、同一の診断コマンドを承認機構経由で通常状態領域へアクセス可能にして実行した。Worker側の開始応答はreadOnly / networkAccess false、環境なし。調整プロセスの実行許可とWorkerの隔離を混同しない。

## 観測と限界

| 確認項目 | 実測 | 判断 |
|---|---|---|
| 実行設定 | 応答model `gpt-6-astra`、reasoningEffort `medium`。environment、runtimeWorkspaceRoots、instructionSourcesは空 | ランタイム応答を確認。サービス内部の検証ではない |
| Reader | allowed.txt成功、相対・絶対の範囲外IDは拒否 | 調整側の要求・返却とraw tool outputで確認 |
| Skill一覧 | orchestrator / executorともskills空、warnings空、next_cursor null | 今回の一覧呼出は空。一般的なSkill経路の不存在は意味しない |
| Skillダミー読取 | 指定package/resourceに `skill package is not available` | 登録されていないpackageの拒否。実在packageの範囲外参照を網羅した試験ではない |
| 自動入力 | raw入力イベントに `host_skills.instructions` と標準5 Skillの名前・説明・ローカル位置が現れた | **instructionSources空から、自動読込なしとは推定できない**。Skill本文や禁止されたtOS資料を読んだ証拠ではない |
| 操作監査 | 3つのfunctions.exec呼出と対応する3返却をrawイベントで保存 | 前回のReaderだけの記録から前進。ただしcode-mode内部の全操作を独立に記録・強制する監査ではない |
| 委譲 | 今回は呼び出していない。raw入力にmulti-agentの案内が残る | 委譲の技術的無効化・子への制約継承は未検証 |

標準Skill案内はimagegen、openai-docs、plugin-creator、skill-creator、skill-installer。`features.skip_host_skill_discovery=true` 等の指定中でも入力イベントに現れた。この観測だけで原因や不具合とは断定しない。開始応答と実入力は別々に確認する必要がある。

## 保存と再現

- `probe.py`：実行コード。`/private/tmp/tos-b12-resume-audit` に専用の空ディレクトリとログを作る。再実行は既存ログを上書きするため、rootを別の新規領域に変え、blocked.txtを置くこと。今回のコマンドは `python3 /private/tmp/tos-b12-resume-audit/probe.py --run`。
- `blocked.txt`：今回置いた無害なダミーファイル。Readerはファイルを開かず、許可IDに定数を返す。
- `thread-start.json`：実行設定応答。
- `events.jsonl`：送信、初期化・開始応答、Reader要求、完了、警告、raw tool call/output、host Skill案内の抜粋。元ログ行番号を保持。host Skill案内以外の開発者指示、reasoning、アカウント情報、delta等は収録しない。全モデル入力・全内部操作を保存した完全ログとは呼ばない。
- `extraction.json`：元ログのハッシュ、イベント件数、抽出条件。元ログは調整側ローカルに保持するが、次回の必須入力にはしない。
- `ThreadStartParams.schema.json`：今回のCLIから生成したschema。
- `SHA256.json`：保存ファイルのハッシュ。

## 人間へ返す環境判断

現設定では本試験の開始条件を満たしたと証明できない。試験基準の緩和や標準Skillの黙認を採用しない。次の進路を人間に求める。

1. **現行Codex Runtimeを維持する**：Skill案内の注入元、明示的な取得Tool許可リスト、委譲の制限・継承、内部操作の監査を解決対象として継続する。実現可能性は未確認であり、P/M/Uの開始時期は確約できない。
2. **別の隔離Runtime構成を候補として評価する**：ケース資料だけを置いた専用環境と全取得操作を記録する構成を検討する。Model、送信先、費用、認証方式、取得Tool、隔離境界を具体化して人間に提示してから採用する。既存のCodex利用承認を別の送信先・課金経路へ一般化しない。

どちらも環境成立後に入力版・設問・担当・採点者を固定し、改訂後の実Readyを人間が判断する。今回の環境確認への依頼をP/M/U Readyに読み替えない。
