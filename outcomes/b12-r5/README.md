# B-12 R5 — 明確化した契約でのFresh Worker試験

2026-09-25 JST。**P/M/Uを実施・独立採点済み。全3ケース合格、全体合格候補。Human DoneとPR mergeは未承認。** 判定の根拠は [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md) を正本とする。

| ケース | 独立評価 | 判定 |
|---|---|---|
| P | 6観点各2点、12/12。本文695字、指定形式適合 | 合格 |
| M | 入力不足・影響・判断者・再開条件を説明。公開5項目適合 | 合格 |
| U | 架空Taskの未承認と診断Readyを区別。公開5項目適合 | 合格 |

## 固定条件とReady

- 人間の「R5を開始してください」を [Issue #25の実Ready](https://github.com/tanakakeisuke-github/tOS/issues/25#issuecomment-5825018657) に開始前保存した。承認記録時点は2026-09-25 01:11:39 UTCで、ユーザー発言の厳密な送信時刻ではない。
- Knowledge・設問・計画：`ae7bafabc93526db4aa5e01744207ba1ba0cdf53`。PR #30の字数契約は人間が承認しmainへ反映済み。
- 固定入力とrunner：`f1723489f057274943984641c8c98441594e6818` の `outcomes/b12-r5-preparation/`。実行中・回答後に変更していない。runnerはR4と同一。
- CLI `0.155.0-alpha.9`、`gpt-6-astra / medium`、fallbackなし。P/M/Uは別々の新規ephemeral Session。親会話・過去回答・他ケース・採点計画を配布していない。
- 初期入力はSTART_HERE、当該CASE_TASK、当該READY。必要資料は固定manifestの文書ID Readerから取得する。固定Knowledge中の古い承認表示は実Readyで扱いを明示した。

## 実行・監査

実行前の [preflight](preflight/answer.md) と操作記録で、許可文書1件の取得、禁止要求7件の拒否、空のSkill一覧、外部取得用globalsの不在を確認した。これは通常Runtimeの設定強制を信頼する範囲の環境確認で、全内部動作の完全監査ではない。

Pは許可8文書、Mは許可5文書と配布外2文書の拒否、Uは許可5文書。Mの不足文書の取得要求には内容を返していない。初期入力、manifest、文書本文、Reader要求と返却、3つの異なるSession IDを [調整側監査](COORDINATOR_AUDIT.json) で照合した。Skill・multi-agent・memory案内の再注入は記録にない。保存されたTool呼出しにも未知の資料取得経路を認めなかった。

Pの指定見出しは各1回・順序通りで、説明本文は原文からCR/LFのみを除いて **695コードポイント**。見出し外の範囲推測、Markdown除去、trim、正規化は行っていない。最終的な内容採点・全体判定は独立Reviewを参照する。

## 保存物

- 各ケースの `answer.md` と `completion.json`：原回答。改変・再生成・再受験なし。
- `initial.txt`、`launch.json`、`thread-start.json`：実投入文、設定とRuntime応答。
- `events.jsonl`：元ログ行番号付きの要求・返却・Toolイベント。reasoning/account/deltaは除外し、開発者入力は種類とhashで記録。抽出方法と元ログhashは `extraction.json`。
- `P-READY.json`、`M-READY.json`、`U-READY.json`：配布した実承認記録。
- `INDEPENDENT_REVIEW.md`：親会話を継承しないReviewerによる採点と引用根拠。
- `SHA256.json`：保存物のhash。元rawログは調整側ローカルに保持。

## 人間の停止点

R4その他の過去結果は原状保存し、R5へ合算しない。R5結果の受入とB-12 Doneは人間が判断する。PR #26のmergeも別の承認対象。この試験の合格は説明・診断と知識引き継ぎの検証であり、tOS全体の完成、実制作、v0.1 Freezeの承認ではない。
