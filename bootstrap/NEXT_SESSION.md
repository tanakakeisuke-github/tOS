# B-12 次Sessionへの引き継ぎ — R4結果のHuman Review待ち

更新：2026-09-25 JST。調整担当向け。受験Workerへ配布しない。

## 正本と現在地

正本は [tanakakeisuke-github/tOS](https://github.com/tanakakeisuke-github/tOS)。[Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)、[Draft PR #26](https://github.com/tanakakeisuke-github/tOS/pull/26)、branch `docs/b12-fresh-worker-acceptance` を使う。mainだけには最新の環境証拠がない。

B-01〜B-11とPR #28の修正は承認・反映済み。B-12は未完了。ユーザーの「ではb-12ををやりましょう」を受け環境確認を継続し、明示的な委譲無効化・Skillファイル単位の無効化、文書Readerへの移行を実測した。独立Reviewerは通常Runtimeの設定強制を信頼する範囲で採用可能と判断した。

**R4は人間の「試験を開始してください。」を実Readyとして開始前にIssue #25へ記録し、P/M/Uを実施・独立採点済み。現在は結果のHuman Review待ち。** P内容12/12だが見出し・Markdownを含む説明ブロック702字で上限700字に不適合、M/U合格。全体合格候補にはしない。原回答を変更せず保存した。完全なRuntime内部監査や無条件の隔離証明を主張しない。

## 再開時の読む順番

1. Issue #25・PR #26の最新headとコメントを確認。未保存変更があれば先に確認する。
2. [R4結果](../outcomes/b12-r4/README.md) → [独立採点](../outcomes/b12-r4/INDEPENDENT_REVIEW.md)を読む。[準備時に固定したR4条件](../outcomes/b12-r4-preparation/README.md)は履歴として参照する。
3. [今回の環境証拠](../outcomes/b12-environment/explicit-controls/README.md) → [独立Review](../outcomes/b12-environment/explicit-controls/REVIEW.md)。必要なコード・実記録だけ参照する。
4. [Acceptance Plan](ACCEPTANCE_PLAN.md)、[Purpose](../specifications/PURPOSE.md)、[Constitution](../CONSTITUTION.md)を照合する。

Knowledge・設問・計画の基準は `7ab8b092544f6f00b8ca8d791ed6473cfef6cd43`。試験記録ブランチのheadとは別。固定版の古い状態ラベルは書換えず、READYにPR #28の実承認・B-11依存解消・今回の診断のみへの着手を具体化する。

## 次の作業

**以下の旧開始手順はR4では実施済み。R4を再実行しない。** 次の判断は、人間が結果と字数境界を確認し、見出し・Markdownを含む計数の説明を明確化する契約修正を進めるかどうか。修正はReview・承認・適用版固定・新しい実Readyを経て別系列で再試験する。R4を遡及再採点しない。B-12 Done/mergeは未承認。

- ユーザーがR4の具体的条件へReady承認した場合だけ、承認者・実際の発言・時点・対象Task・範囲・版・理由・各manifest hashをIssue #25と各READY記録へ保存する。既に承認された場合は同じ承認を再度求めない。
- 準備フォルダーのP/M/Uは独立入力。READYは未作成。共通runnerは記録形式/hashを検査するが、人間の承認の真偽を自動認定しない。担当者が実承認と照合する。
- ケースごとの新規ephemeral Sessionで初期3文書だけを投入し、必要文書を固定ID Readerから取得させる。モデル・設定・自動入力・操作・原回答を保存。ケース間で回答を渡さない。
- 受験者へ旧会話、本書、採点計画、期待回答、他ケース、環境報告を渡さない。
- 未承認、設定差異、入力不整合、未知の取得経路・自動案内再注入・汚染は停止して記録する。回答が良くても逸脱を合格にしない。
- 作成担当・受験Sessionから分離したFresh Reviewerが原回答・入力・操作記録・公開基準を照合し、結果をDraft PR #26へ保存。人間の受入判断で停止する。

## 承認と履歴

OpenAI Codex `gpt-6-astra`へ試験資料を送ることは [R3再開前記録](https://github.com/tanakakeisuke-github/tOS/issues/25#issuecomment-5818091607)の承認範囲内。同一範囲の送信承認を重ねて求めない。別送信先・課金経路へ一般化しない。

初回/R3の未達、R2中断、旧環境の未成立は保存する。今回の判定で遡及再採点しない。旧履歴は [環境総括](../outcomes/B12_ENVIRONMENT_CHECK.md) と [前回監査](../outcomes/b12-environment/resume-audit/README.md) から辿れる。

B-12の受入は、最初の知識・引き継ぎ方法の検証。tOSは実コンテンツ制作とフィードバックによってリデザインし続けるもので、この試験を全体の最終完成・Freezeと扱わない。個別TaskのReady/Doneは人間が判断する。

## ローカル補助

作業cloneは `/private/tmp/tos-b07-20260925`。remote・branch・statusを確認して使用する。消失時はPR #26から復元可能。ChatGPT同期の `sources/` は読取専用。古い `/private/tmp/tos-b12-r4/` の入力は使わず、今回のR4準備フォルダーを正本とする。
