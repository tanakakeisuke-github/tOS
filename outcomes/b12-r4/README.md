# B-12 R4 — 改訂後P/M/U結果

2026-09-25 JST。**3ケース実施・独立採点済み。全体合格候補にはしない。Human Review待ち、Done未承認。**

## 結果

| ケース | 独立評価 | 判定 |
|---|---|---|
| P | 内容6観点は各2点、12/12。六段落694字。先頭の見出しとMarkdown記号を含む説明ブロックは702字 | 700字上限の形式要件不適合 |
| M | 公開5項目と範囲遵守を満たす。模擬Readyと実診断Readyを区別し、不足資料を補完しない | 合格 |
| U | 公開5項目と範囲遵守を満たす。架空Taskの未承認を実診断Readyで代用しない | 合格 |

Pは「本文見出しを除外」と自己申告しているが、CASE_TASKは見出しを含め改行のみ除外と定める。Reviewerは提出された説明ブロックを対象とし、Markdown記号を除く追加規則を導入せず702字と計数した。表示上の見出し文字だけを加えれば698字になることも含め、[独立Review](INDEPENDENT_REVIEW.md)で境界と計数方法を明示する。原回答の見出しを削除したり、回答後に字数基準を変更したりして合格にしない。

## Ready・版・実行

- 人間の「試験を開始してください。」を [Issue #25の実Ready](https://github.com/tanakakeisuke-github/tOS/issues/25#issuecomment-5824774105) に開始前保存。記録時点2026-09-25 00:48:41 UTCは確認時刻で、ユーザー送信の厳密な時刻ではない。
- Knowledge/設問/計画基準：`7ab8b092544f6f00b8ca8d791ed6473cfef6cd43`。準備入力・runner：`ebdb73ef79e4e76ff3233dab00809fd2fb7f0e18`。回答前後で入力・runnerを変更していない。
- 各ケース別のephemeral Session。CLI `0.155.0-alpha.9`、応答 `gpt-6-astra / medium`、environmentなし。開始UTCはP 00:50:15、M 00:50:16、U 00:50:17。親会話・他ケース回答を配布しない。
- 初期入力はSTART_HERE、当該CASE_TASK、当該READYの3文書。各READYの依存解消・承認範囲は今回の診断だけを対象とする。

## 取得・監査

Pは許可8文書、Mは許可5文書と配布外2件の拒否、Uは許可5文書。Mが要求したstudio/EVALUATION.mdとproject/BRIEF.mdはsuccess falseで内容を返していない。取得要求と取得成功を分ける。初期入力・配布本文のhash、Readerの要求と返却、3つのSession IDの独立性を調整担当が照合した。

実入力の種類はpermissions、collaboration_mode、environment、user textで、host Skill・multi-agent・memory案内の再注入は記録にない。rawのexec呼出はReader取得とPの文字数計算で、未知の取得経路は観察されなかった。[調整側監査](COORDINATOR_AUDIT.json)と各ケースeventsを参照。通常Runtimeの制限制御を信頼する範囲の確認であり、全内部動作の独立監査の証明ではない。

実行前のReady生成用補助処理で文字エンコードエラーがあり、最初の起動要求はReadyファイル不在でモデル起動前に拒否された。Readyを作成・hash照合した後にのみ各ケースを起動した。回答を見た後の再受験や入力変更はない。

## 保存物

- P/M/Uのanswer.md、completion.json：原回答。変更・再生成しない。
- initial.txt、launch.json、thread-start.json：実投入全文、設定・hash、Runtime応答。
- events.jsonl：元行番号付きの要求/返却・raw Tool呼出/返却・完了の抜粋。reasoning/account/deltaを除外し、開発者入力は種類とhashを保存。抽出条件と元ログhashはextraction.json。元rawログは調整側ローカルに保持。
- P/M/U-READY.json：実際に配布した承認記録。runnerが整形した配布文字列のhashはlaunch.jsonに保存。
- INDEPENDENT_REVIEW.md：親会話を継承しないReviewerの採点と引用根拠。採点はHuman Doneではない。
- SHA256.json：保存物のhash。

## 次の判断

内容理解の不足やKnowledge不合格と、今回の字数形式不適合を分ける。次は、人間がこの結果・計数境界を確認し、字数の数え方（Markdown見出し・装飾記号を含む提出境界）を設問でさらに明確にする修正を行うか判断する。修正する場合は小さな契約改訂としてReview・承認・適用版固定を経て再試験へ進む。R4を遡及再採点せず、同じ入力の無断再試行もしない。

B-12 Done、PR merge、全体受入は未承認。tOS全体の完成・制作開始をこの結果から宣言しない。
