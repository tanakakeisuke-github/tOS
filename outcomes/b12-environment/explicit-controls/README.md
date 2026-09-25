# B-12 明示的な取得制限と文書Reader移行

2026-09-25 JST。ユーザーの「ではb-12ををやりましょう」を受け、現行Codexの環境確認を継続した。P/M/Uの実Readyは未承認、本試験は未実施。旧試行の採点は変更していない。

## 前回から変更した条件

- `agents.enabled=false` を追加。旧 `features.multi_agent=false` のみの条件と区別する。
- `skills.config` の標準5 Skillを無効化。フォルダー指定では案内が残り、`SKILL.md` ファイル指定では実入力から消えた。
- Codex `0.155.0-alpha.9`、`gpt-6-astra / medium`、代替禁止、ephemeral、environmentなし、rawイベント記録、他の機能制限は維持。ユーザーの設定ファイルは変更していない。

[公式Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference)は `agents.enabled` を委譲Toolの有効/無効設定と定義している。Skill pathの説明はフォルダーだが、本版CLIでは今回のファイル指定の実測を根拠にする。別バージョンへの一般化はしない。

## 記録で確認したこと

| 条件 | 結果 |
|---|---|
| `folder/` | Reader許可・拒否、Skill一覧空。multi-agent案内は消失したがhost Skill案内は残った |
| `file/` | 実入力のhost Skill案内・multi-agent案内が消失。Skill一覧は両authorityとも空。既知のalias・絶対package・ダミーresourceを拒否 |
| `final/` | 上記と同じ設定で相対/絶対パス、他ケース、採点資料、履歴、URL、余分属性の拒否を確認。`fetch/require/process/WebSocket` はundefined |
| `manifest/` | 本試験と共通runnerの固定manifestからダミー本文を返す移行確認。実文書のケースは未送信 |

`final/` はReader要求を二度送った箇所がある。最初のexecが「例外がなかった」をsuccessと表示したため、実値を再取得してDENIEDを確認している。調整側は最初から禁止要求にsuccess falseを返していた。モデルのラベルをアクセス判定に使わない。

## 独立レビューと判定の範囲

親会話を継承しない環境Reviewerへ、承認済み計画・前回の環境記録・今回のコードと実記録だけを渡した。Reviewerは受験Workerではない。レビュー要旨は `REVIEW.md`。

通常のRuntimeの設定強制を信頼する範囲で、今回の構成は採用可能との評価。全Runtime内部の完全隔離・全内部操作の独立監査・将来の同一挙動を証明したという意味ではない。

`ALL_TOOLS` はnested toolsの一覧であり、外側の委譲Tool不存在をその一覧だけで証明しない。委譲無効化は公式に定義された設定、実行コード、multi-agent案内の消失を根拠とし、Worker報告は補助証拠に留める。Skill本文の無制限取得が不可能であるという一般証明も主張しない。今回の一覧空・既知識別子拒否・environmentなしを確認した。

各ケースの開始時にモデル・設定・初期入力を再確認し、追加取得・操作・原回答を記録する。案内注入や未知の取得経路・設定逸脱が現れた場合は当該試験を汚染/環境逸脱として停止し、合格にしない。環境確認をHuman ReadyやHuman Doneの代用にしない。

## 証拠の保存

各フォルダーの `events.jsonl` は元行番号付き抽出。送信、Reader要求/返却、raw tool call/output、完了、入力種別とハッシュを保存。開発者指示本文は保存せず種類とハッシュ、host Skill案内の有無を記録する。reasoning、アカウント情報、deltaを除外した。全内部操作を網羅する完全ログとは呼ばない。`extraction.json` に元ログハッシュ・抽出数、`SHA256.json` に保存物ハッシュを置く。

次の実行条件と人間の判断対象は [R4準備](../../b12-r4-preparation/README.md)。この記録は診断コードと証拠であり、tOS本体の実装・一般用途ランナーの採用ではない。
