# B-12 — 改訂後の環境成立確認

状態：**明示設定と文書Reader移行を確認し、独立Reviewで限定付き採用可能。実Ready待ち。改訂後P/M/Uは未着手・未採点。** 対象は[Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)の開始前確認。承認済み改訂は[PR #28](https://github.com/tanakakeisuke-github/tOS/pull/28)、main `7ab8b092544f6f00b8ca8d791ed6473cfef6cd43`。修正Issue #27は完了している。以下の旧試行の未成立判定は履歴として維持する。

## 最新の到達点

[追加証拠・独立Review](b12-environment/explicit-controls/README.md)を保存。`agents.enabled=false` とSkillのSKILL.md単位無効化により実入力の案内が消失。Reader、Skill、JS直接取得経路を実測し、共通runnerのmanifest文書返却・拒否を検証した。通常Runtimeの設定強制を信頼する範囲で採用可能。全内部操作の完全監査の証明とはしない。具体的な [R4条件と入力](b12-r4-preparation/README.md)へのHuman Readyを求める段階に進んだ。受験はまだ開始していない。

## 確認したこと

会話を継承しない担当が、実際のtOS資料をモデルへ送らず、許可ファイルと禁止ファイルに無害な文字列を入れた事前確認を行った。既存のセキュリティ設定は解除していない。CLIは0.155.0-alpha.9。

| 方法 | 実測 | 判定 |
|---|---|---|
| Codexのcustom profileにroot-deny・個別denyを設定 | 許可ファイルと禁止ファイルの両方を読めた。exit 0。 | 不成立。設定だけで隔離を宣言できない。 |
| OS側で試験用ディレクトリを制限し、許可領域を追加 | 許可ファイルは読め、`fixture/../blocked.txt`は拒否された。exit 1。 | 部分的な制限の実証。他領域も遮断するWorker環境全体の証明にはならない。 |
| 全体の読取を制限し、実行に必要な領域を許可 | プロセスがexit 134で中断。 | 不成立。許可読取と禁止読取の両方を検証できない。 |
| 上記のread-data単位の別設定（調整担当の追加確認） | 同じくexit 134。 | 不成立。原因は未特定。 |

詳細な条件・結果・参照した公式資料は[検証記録](b12-environment/PROBE_EVIDENCE.md)。使用した3つのOS制限設定も同じフォルダへ保存した。これらは診断用の原記録であり、承認済み実行設定・制作OSの実装ではない。

当初は専用Readerを未実行だった。その後、下記の追加確認を実施した。これは新しいKnowledge不合格ではなく、受験前の環境要件の確認である。

## 追加確認：環境アクセスなしの専用Reader

Codex app-serverの `environments: []` と固定IDだけを返すReaderを使い、実際のtOS資料を送らず3回のダミー確認を実施した。[詳細・証拠](b12-environment/app-server/README.md)。

- 実行応答は `gpt-6-astra` / `medium`、environment・workspace root・読込instruction sourceは空。要求モデルの自動代替を禁止した。これはランタイムが報告するモデル名の確認であり、サービス内部の重みの検証ではない。
- Readerは許可IDで成功し、相対的な範囲外指定と絶対パス指定を拒否した。要求と返却は調整側ログで確認できる。
- Workerのツール一覧報告にはSkill取得と他Agentへの委譲が残った。これらの読取範囲・継承条件は検証できていない。Reader単体の制限から全経路の隔離を推定しない。
- 実行機能全体を止めた条件では必要なReaderも使えなかった。

**判定は環境未成立のまま。** 未解決点は全読取経路の制限と監査。改訂後P/M/Uは実施していない。

## 残っている仕事

1. 試験用資料だけを渡せる実行環境を成立させる。許可読取、ディレクトリ外参照・別ケース・期待回答の拒否、操作記録の取得とモデル設定を、実際に使うWorkerと同じ条件で確認する。単独のOS機能が動いただけで受験を開始しない。
2. 成立した環境、改訂版commit、確定したP/M/U入力、担当とReadyをIssue #25に固定してから、新しいSessionで受験する。
3. 独立Reviewerが記録と回答を照合し、人間が結果・残課題から受入を判断する。

同じ未成立の環境で試行回数だけを増やさない。次の環境担当には本書と承認済み計画の開始条件を渡す。受験者には本書・旧結果・採点者用資料を渡さない。B-12 Done、Bootstrap受入、v0.1 Freeze、制作開始は宣言しない。

## 再開時の追加監査（2026-09-25）

[rawイベントを使った追加記録](b12-environment/resume-audit/README.md)で、Skill一覧の実返却とダミー読取拒否を確認した。一方、instructionSources空でも標準Skill案内が実入力へ注入されていた。委譲の制約継承・全経路監査は未確認。環境未成立を維持し、現行Runtimeの制限解決を継続するか、別の隔離Runtime構成を評価するかを人間の判断へ返す。改訂後P/M/U・独立Reviewは未実施。
