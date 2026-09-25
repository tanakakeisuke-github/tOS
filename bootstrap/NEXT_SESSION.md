# B-12 次Sessionへの引き継ぎ — R5結果のHuman Review

更新：2026-09-25 JST。調整担当向け。受験Workerへ配布しない。

## 正本と現在地

正本は [tanakakeisuke-github/tOS](https://github.com/tanakakeisuke-github/tOS)。[Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)、[Draft PR #26](https://github.com/tanakakeisuke-github/tOS/pull/26)、branch `docs/b12-fresh-worker-acceptance` を使う。mainだけには最新試験記録がない。

B-01〜B-11、PR #28、および字数契約を明確化した [PR #30](https://github.com/tanakakeisuke-github/tOS/pull/30) は人間の承認を経て反映済み。R4のPは形式不適合だったが、その原結果を改変・再採点していない。

ユーザーの「R5を開始してください」を新しい実Readyとして開始前に記録し、R5のP/M/Uを独立した新規Sessionで実施した。結果は [R5結果](../outcomes/b12-r5/README.md)、採点の正本は [独立Review](../outcomes/b12-r5/INDEPENDENT_REVIEW.md)。**B-12 DoneとPR #26 mergeは未承認。次は人間の受入判断で停止する。**

## 再開時の読む順番

1. Issue #25・PR #26の最新headとコメントを確認。既に人間が承認していれば同じ承認を再度求めない。
2. R5結果、独立Review、調整側監査、必要な原回答・操作記録を読む。
3. [固定R5入力](../outcomes/b12-r5-preparation/README.md) と実Readyを照合する。
4. 必要時に [環境確認と独立Review](../outcomes/b12-environment/explicit-controls/README.md)、[Acceptance Plan](ACCEPTANCE_PLAN.md)、[Purpose](../specifications/PURPOSE.md)、[Constitution](../CONSTITUTION.md) を参照する。

## 固定条件

Knowledge・計画・設問の基準は `ae7bafabc93526db4aa5e01744207ba1ba0cdf53`、固定入力・runnerは `f1723489f057274943984641c8c98441594e6818`。試験記録ブランチのheadとは別。PR #30の承認済み文書を記録ブランチへ取り込んだ。固定Knowledge中の歴史的な承認待ち表示は変更せず、実Readyで採用版と今回の診断のみへの承認を明記した。

R5はPの指定見出し間の原文からCR/LFだけを除いてUnicodeコードポイントを計数する契約。P/M/UすべてをR5で実施し、R4の合格と合算しない。受験者にはSTART_HERE・当該Task・実Readyを初期配布し、許可された必要資料だけをReaderで渡した。旧チャット、期待回答、採点計画、他ケースを渡していない。

環境は通常Runtimeの明示設定・文書Reader制御を信頼する範囲で確認済み。全内部操作の完全監査・無条件の隔離を主張しない。未知の取得経路や入力汚染を新たに認めた場合は、良い回答でも試験有効性を再評価する。

## 人間の停止点と履歴

独立採点はHuman Doneを代行しない。人間にR5結果をB-12の説明・診断試験として受け入れるかを具体的に確認する。mergeやIssue完了への承認範囲を区別する。未承認の再試験・原回答の修正・過去結果への遡及適用は行わない。

初回/R3の未達、R2中断、旧環境未成立、R4形式不適合は保存する。[結果入口](../outcomes/BOOTSTRAP_ACCEPTANCE.md)、[R4原結果](../outcomes/b12-r4/README.md)、[環境履歴](../outcomes/B12_ENVIRONMENT_CHECK.md)から辿れる。

tOSは実コンテンツ制作とフィードバックでリデザインし続ける。B-12の受入は現在の知識引き継ぎの検証であり、全体の最終完成・v0.1 Freeze・実制作開始を意味しない。

## ローカル補助

cloneは `/private/tmp/tos-b07-20260925`。使用前にremote・branch・statusを確認する。消失時はPR #26から復元可能。ChatGPT同期の `sources/` は読取専用。実行rawログは `/private/tmp/tos-b12-r5-execution`、事前確認は `/private/tmp/tos-b12-r5-preflight`。公開用の抜粋とhashはR5結果フォルダーに保存した。
