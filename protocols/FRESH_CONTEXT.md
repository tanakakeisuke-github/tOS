# Fresh Context Protocol — 指定入力からTaskを開始・再開する

状態：B-09としてHuman Review承認済み（[PR #20](https://github.com/tanakakeisuke-github/tOS/pull/20)）。本手順は[Session Model](../specifications/SESSION_MODEL.md)の開始・再開を具体化する。Taskの状態とReady判断は[Task Protocol](TASK.md)、入力の正本・版・承認状態は[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md)を参照する。

## 入力

担当Issue、対象TaskのReady承認記録、基準版、指定Input Context、目的・範囲・受入条件・依存・停止点。再開時は前Sessionの[引き継ぎ](HANDOFF.md)と人間の解決判断も入力とする。Reviewerの開始時は、Review対象の成果と版、Workerの確認結果・未実施の検証、独立確認の観点と例外記録も受け取る。

## 担当・手順

着手・再開するWorker、または新しくReviewを始めるReviewerが照合する。Roleと担当Actorの割当は[Actor Model](../specifications/ACTOR_MODEL.md)に従い、Readyの承認者は人間である。Reviewerの独立確認は[Review Protocol](REVIEW.md)で行う。

1. 担当Issueで対象Task、現在の担当、Ready承認の対象・範囲・記録先を確認する。Issueの作成や状態表示だけからReadyを推定しない。
2. 基準版と各指定入力の所在・出所・適用版・承認状態を照合し、そのTaskに必要な節だけを読む。会話の記憶や未指定の履歴を承認済み入力に加えない。入力の選択と衝突時の扱いは[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md#taskごとの入力とopen-question)に従う。
3. 目的・範囲・受入条件・依存・停止点を自分の作業境界として確認する。再開時は引き継がれた成果版、済んだ作業、未実施の検証、残課題、停止理由、解決判断と適用版を照合する。Reviewerはさらに対象成果の版、Workerの確認結果、未実施の検証、独立確認の観点、Workerとの分離または例外判断を確認する。
4. 不足・矛盾・承認範囲外の判断があれば、箇所と版、影響、必要な判断者、再開条件を担当IssueまたはReviewに残し、影響する作業を止める。目的・範囲・入力・受入条件が変わる場合はReady前Human Gateへ戻す。妨げないUnknownは問いと次の判断点を残して進める。

## 出力

担当Issueから辿れる開始・再開時の照合結果。対象Task、Ready承認、基準版と実際に用いた入力、作業境界、不足・矛盾・Unknownと停止範囲を示す。これ自体は成果の検証やDone承認ではない。

## 停止条件

Ready承認、指定入力の適用版・承認状態、依存の成立、受入条件または停止点を確認できないときは、影響する作業を開始・再開しない。Reviewerは対象成果・確認結果・独立性の条件を確認できなければReviewを開始しない。矛盾の解消を推測せず、人間の判断とその記録を待つ。
