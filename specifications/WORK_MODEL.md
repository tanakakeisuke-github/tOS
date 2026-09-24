# tOS — Work Model

状態：B-05としてHuman Review承認済み（[PR #12](https://github.com/tanakakeisuke-github/tOS/pull/12)）。本書の状態名と遷移は仕様上の語彙であり、既存の自動化やGitHub Projectの設定・運用実績を示さない。

目的と判断原則は[Purpose](PURPOSE.md)・[Constitution](../CONSTITUTION.md)、知識の正本と承認状態は[Knowledge Architecture](KNOWLEDGE_ARCHITECTURE.md)、媒体間の責務は[Core Architecture](CORE_ARCHITECTURE.md)を参照する。本書は検討から着手・完了までの仕事の単位と境界を定める。

## 仕事の単位

| 単位 | 役割と境界 |
|---|---|
| **Discussion** | 問い、選択肢、未決定事項を検討する場。長く継続できるが、発言や合意らしい表現だけでTaskの着手・完了を承認しない。 |
| **Task** | 一つの小さな目的、範囲、入力、受入条件、依存、停止点を持つ実行単位。Discussionから提案できるが、TriageとReady前Human Gateを経て初めて着手できる。 |
| **Issue** | Taskの条件、状態、根拠、承認への参照を引き継ぐ記録単位。原則として一つの実行Issueを一人のFresh Workerが担当する。Issueの作成自体はTaskのReady承認ではない。 |

**1 Task = 1 small objective**。Fresh Workerが指定入力を一度のSessionで理解し、成果を作り、受入条件に照らして自己確認できる認知負荷を目安にする。ファイル数や所要時間だけでは決めない。目的が複数ある、入力・検証・承認の境界が異なる、または一度に把握できない場合は、依存関係と各成果を明示してTriageで分割する。Sessionは短命でも、Issueと成果・判断記録から仕事を再開できるようにする。WorkerとReviewerの分離とSessionの再開はB-06以降、制作全体の流れは[Creation Lifecycle](../vision/CREATION_LIFECYCLE.md)で扱う。

## Triage、状態、Human Gate

以下の状態名はB-05で承認された仕様上の語彙である。Discussionの案をTriageし、Task化、追加検討、将来版での評価、または却下を人間に見える形で選ぶ。Task化を選んでもReadyにはならない。

| 遷移 | 必要な判断・根拠 |
|---|---|
| **提案 → Triage → Ready待ち** | 一つの目的に絞ったIssueに目的・範囲・入力の版と出所・受入条件・依存・停止点を記す。分割したTaskはそれぞれ別に扱い、依存を結ぶ。 |
| **Ready待ち → Ready** | **Ready前Human Gate**。人間が上記の条件と着手可能性を確認し、対象Taskと適用版を指定して着手を承認する。未承認または却下ならReadyへ進めない。 |
| **Ready → 作業中 → Review待ち** | 承認範囲内で成果を作り、実施した確認、残課題、参照した版を記す。Reviewerが成果と受入条件・根拠を独立に確認できる形で渡す。 |
| **Review待ち → Done待ち → Done** | Reviewの結果、必要な検証、未解決事項を提示する。**Done前Human Gate**で人間が成果と完了条件を確認し、完了を明示的に承認した場合だけDoneとする。差戻しは理由と再作業範囲を記してReview待ちまたは作業中へ戻す。 |

入力不足・矛盾・承認範囲外の判断が見つかれば、影響する作業を**Blocked**として停止し、理由、影響範囲、必要な判断、再開条件をIssueまたはReviewに残す。条件の解消後も、目的・範囲・入力・受入条件を変えるならReady前Human Gateへ戻す。未解決だが現在のTaskを妨げない問いは**Unknown**として問いと担当判断者・次の判断点を記録し、承認済み条件を推測で補わない。Unknownが受入条件や着手・完了判断を妨げる場合は、その範囲をBlockedにする。

承認外の追加作業は着手せず、分割案または別提案としてTriageに戻す。ツール上のラベル変更、Issueのクローズ、PRの作成・マージ、CI成功、AIの自己確認はいずれも人間のReady・Done承認の代用にならない。

## 記録と照合例

担当IssueをTaskの条件・状態・依存・停止点の参照先とし、成果とReviewの根拠はReview記録から辿れるようにする。各Gateの承認記録は、対象Issue、判断した人間、時点、承認または却下した範囲と版、理由、根拠へのリンクを持つ。判断理由と承認記録の正本は[Knowledge Architecture](KNOWLEDGE_ARCHITECTURE.md#正本と分類)に従い、担当IssueまたはReviewの**一方**を指定して相互参照する。記録先や状態が不明なら承認を推定せず停止する。

例えば、Discussionで「試作品の操作感と画面表示を改善する」と提案されたとする。Triageで評価方法と成果が異なると分かれば、「操作感を一つのテストで測る」と「結果を踏まえて画面表示案を作る」を依存付きの二つのTaskに分ける。前者のIssueに入力版・テスト条件・受入条件を記し、人間がその範囲を承認した記録を結んでからReadyにする。後者は別のReady承認まで着手しない。

逆に、Issueだけ作られた「画面を全面改修する」案で、対象画面、入力、受入条件が揃っていない場合はTriageに留める。WorkerがラベルをReadyに変えたり試作PRを出したりしても着手承認にはならない。Triageで範囲の分割と不足情報を整理し、Ready待ちに必要な条件を揃えてから人間の着手判断を待つ。
