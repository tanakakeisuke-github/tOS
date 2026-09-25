# B-12 app-server事前確認

判定：環境未成立。P/M/U受験ではない。既存のセキュリティ設定・ユーザー設定ファイルは変更していない。モデル送信は承認済みCodex利用の範囲で、下記ダミー入力だけを使用した。

## 条件と証拠

インストール済みCLI `0.155.0-alpha.9` の `app-server generate-json-schema` で確認した `thread/start` / `turn/start` の `environments: []` は環境アクセスを無効にする契約である。新規ephemeral thread、空ディレクトリ、動的 `read_document`、モデル `gpt-6-astra`、代替禁止、effort `medium`。instructionSources・runtimeWorkspaceRoots・thread.environmentsは応答上すべて空。

Readerはファイルパスを開かず、要求が `{"document_id":"allowed.txt"}` と完全一致する場合だけ `ALLOWED_DUMMY_42` を返す。他は拒否。範囲外のダミーファイルは `BLOCKED_DUMMY_73`。旧会話・tOS文書・採点情報を送っていない。

| 試行 | 観測 | 限界 |
|---|---|---|
| probe1 | Readerの許可1件、拒否2件を調整側ログで確認。実行モデル応答取得。 | Workerが報告したツール一覧にSkill取得・委譲が残る。 |
| probe2 | 追加機能とcode-mode hostを無効化。Workerは `code-mode host is disabled` と報告。Reader呼出なし。 | 禁止読取と同時に必要読取も成立しない。エラー内容はWorker報告であり、この抜粋に独立したhostエラー原文はない。 |
| probe3 | code-mode hostを維持、追加機能を無効化。Reader許可1件・拒否2件をログで再確認。 | Worker報告では `skills__list` / `skills__read` とcollaborationが残る。禁止資料へ到達できるか・委譲先へ同一制限が適用されるかは未検証。 |

Workerのツール一覧や「アクセスしなかった」という回答は自己申告として区別する。調整側が直接検証できるのはthread/start応答とReaderに到達した要求・返却。サーバー内部の全ツール呼出を網羅したログは得られていない。設定値だけ、またはWorker報告だけで全経路隔離を合格にしない。

## 保存物

- `probe1.py` / `probe2.py` / `probe3.py`：実際の診断用起動・Readerコード。制作OSの実装や採用済みランナーではない。
- `probeN-thread.json`：各試行の実行設定応答。
- `probeN-events.jsonl`：送信メッセージ、初期化/開始応答、Reader要求、完了回答の抜粋。順序は元ログ順。重複delta、空reasoningイベント、アカウント利用量等は省略。全ツール操作の完全ログとは呼ばない。
- `SHA256.json`：上記保存物のハッシュ。README自身は対象外。

## 次の判断に必要なこと

専用Reader経由の読取は成立した。残りは、追加のSkill/委譲を含む全資料取得経路を制限・監査できるランタイム条件の確認である。現設定で本試験を開始する根拠には不足する。

新しい案：環境担当が実効ツール一覧・各取得経路の制限・ログを検証できる構成を確定してから、ダミー事前確認を行う。別Runtimeへ変更する場合は、Actor/Model/設定と送信先を具体化してHuman判断へ渡す。これは既存方針の変更・採用決定ではない。入力隔離条件を緩和したり、一般会話での説明成功をB-12合格と読み替えたりしない。

参照：インストール済みschemaの `ThreadStartParams` / `TurnStartParams` / `ThreadStartResponse` / `DynamicToolCallResponse`。一般仕様の入口は [Codex App Server](https://learn.chatgpt.com/docs/app-server)。本判定は上記実測と保存物に基づく。
