# Discussion Protocol — 問いを選択肢へ整える

状態：B-08としてHuman Review承認済み（[PR #18](https://github.com/tanakakeisuke-github/tOS/pull/18)）。Discussionの単位とTaskとの境界は[Work Model](../specifications/WORK_MODEL.md#仕事の単位)を参照する。

## 入力

- 検討したい問い、発言または観察。その出所・対象・適用版・承認状態が分かる参照。
- 既に分かっている目的、制約、未決定事項、および判断が必要な時点。これらが未提示なら「不明」と明記する。

## 担当・手順

Discussionを進める担当Actorが、問いと選択肢を整理する。ActorのRoleと権限は[Actor Model](../specifications/ACTOR_MODEL.md)に従い、AIによる整理を人間の着手判断と混同しない。

1. 問いを一文にし、何を決めるための検討かを記す。事実、仮説、提案、既承認の条件を出所と状態で分ける。正本と読み順は[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md#版状態出所)を参照する。
2. 進める、保留・追加調査、採らないなどの選択肢を検討し、該当する各案の根拠、影響、未知、判断に必要な入力を簡潔に示す。比較できない場合は不足点を先に列挙する。
3. 実行が必要な選択肢は、期待する成果と判断者を示して[Task Protocol](TASK.md)へ渡す。実行しない選択肢と未決定事項も出所付きで残す。発言や賛同だけをTaskのReady承認と解釈しない。

## 出力

問い、比較できる選択肢、根拠と未知、推奨の有無、判断者、次の判断点、Task案へ渡す参照。記録先と状態は[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md#正本と分類)に従う。

## 停止条件

目的・出所・適用版が不明で選択肢を比較できない、または承認済み資料が矛盾する場合は**STOP**。不足・矛盾・影響と再開に必要な判断を記録し、その部分を進めない。問いの中に異なる目的が混じる場合は**SPLIT**案として問いと依存を分ける。検討中に別の改善を見つけた場合は**PROPOSE**として現行の問いから分け、[Triage Protocol](TRIAGE.md)へ渡す。これらの扱いは[Operating Model](../vision/OPERATING_MODEL.md#stop--split--propose)を参照する。

## 照合例

「評価結果が足りないが方式を選びたい」という問いでは、欠けた評価条件と出所を示し、方式の採用判断をBlockedとして止める。比較条件を決める小さなTask案だけを別に渡す。そのTask案もTriageとReady前Human Gateを通る。
