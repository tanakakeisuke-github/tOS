# tOS — Actor Model

状態：B-07仕様案。Human Review・Done承認前。本書の分類と割当規則は設計上の定義であり、Actorの稼働や交換の実証を示さない。

本書は制作上の責任と、それを担う主体・AIの実行構成・モデルを分ける。[Constitution](../CONSTITUTION.md)のHuman Gate、[Work Model](WORK_MODEL.md)のTaskと状態、[Session Model](SESSION_MODEL.md)のWorkerとReviewerを前提とする。媒体固有のRoleは[Core Architecture](CORE_ARCHITECTURE.md)に従いStudio Templateで具体化する。

## 四つの概念

| 概念 | 意味と境界 |
|---|---|
| **Role** | 制作上の責任、期待する成果と確認観点を表す役割。Taskの範囲と受入条件に照らして定める。Role名だけで着手・完了承認の権限を与えない。CoreはGameやFilm等の専門Role一覧を固定しない。 |
| **Actor** | Roleを割り当てられ、Taskで仕事を担う主体。分類は **Human / Cloud AI / Local AI**。Humanは人間、Cloud AIとLocal AIはそれぞれクラウド側・ローカル側でAIの仕事を担う主体を表す。分類から能力、利用可能性、権限を推定しない。 |
| **Agent** | AI Actorの仕事を実行するための構成単位。指定された入力、指示、利用可能な手段、出力の扱いを束ねる設計概念であり、RoleそのものでもHuman Gateの判断者でもない。Human ActorにAgentの利用を必須としない。 |
| **Model** | Agentが利用する推論等の能力を提供するモデル。Model単体にRole、Taskの責任、承認権限を割り当てない。同じAgentが使うModelの変更と、担当Actorの変更を区別して記録する。 |

関係は **TaskのRole → 担当Actor →（AIの場合）実行するAgent → 利用するModel** と読む。Roleは「何を担うか」、Actorは「誰／どの主体が担うか」、AgentとModelは「AI Actorがどう実行するか」を示す。AI Actorが成果やReviewを作っても、TaskのReady・Doneを決めるのは人間である。AI Reviewは受入条件と根拠を独立に照合する仕事であり、Human Gateの承認記録にはならない。

## 割当と交代

Roleの割当は対象Taskの目的・範囲・受入条件に結び、担当Issueを現在の担当Actor、適用版、引き継ぎ先を確認する入口とする。AI Actorを割り当てる場合は、仕事に用いるAgentとModel、利用条件を識別できるようにする。ただし製品名や実装設定を本書で選ばない。WorkerとReviewerの分離を原則とし、例外と独立確認への影響は[Session Model](SESSION_MODEL.md#sessionと担当の原則)に従う。

担当Actorを交代する、またはAgent・Modelを変更するときは、人間が対象Task、理由、変更前後の担当と実行構成、引き継ぐ入力・成果・未解決事項、既存のReady承認とReviewの独立性への影響を確認して判断する。判断理由と承認状態の正本は[Work Model](WORK_MODEL.md#記録と照合例)に従い担当IssueかReviewの一方に指定し、他方から参照する。担当Issueには現在の割当とその判断記録への参照を残す。交代だけでTaskをDoneにしたり、過去の検証を新担当が実施したことにしたりしない。

変更がTaskの目的・範囲・入力・受入条件を変えるならReady前Human Gateへ戻す。変更前の承認を同じTaskに適用できるか不明、引き継ぎに必要な情報が欠ける、または承認範囲を越える判断が必要な場合は影響する作業を止め、人間の判断と再開条件を記録する。担当変更後のSessionは指定入力と承認状態を読み直す。成果の独立ReviewとDone前Human Gateは交代後も必要である。

## 関係を確かめる例

例えば、あるStudio Templateが「評価項目を整理する」Roleを定め、ProjectのTaskが評価項目一覧を成果に指定したとする。最初のCloud AI ActorからLocal AI Actorへ同じRoleの担当を移す場合、Taskの範囲と受入条件を保ちつつ、担当Issueの割当、引き継ぐ入力と途中成果、実行するAgent・Model、既存承認への影響を人間が確認して記録する。両者が同じ結果を出せるとは仮定しない。

同じCloud AI Actorが担当を続け、Agentの利用Modelだけを変える場合も、適用Modelと変更理由、成果・検証への影響を記録する。これは担当Actorの交代とは別の変更であり、変更後の結果は必要な確認を受ける。反対にHuman Actorが同じRoleを担うなら、AgentやModelの割当は不要である。いずれの例でも、Role担当者の自己確認やAI ReviewerのReviewは人間のReady・Done承認を代行しない。

## 他の境界と未決定事項

Runtime / Orchestrator / Vendorの責務と交換時の受け渡しは[Core Architectureの「実行技術との交換点」](CORE_ARCHITECTURE.md#実行技術との交換点)を参照する。本書はRole・担当主体・AI実行構成の関係を定めるもので、その交換契約、API、製品選定、実装方法を重ねて定めない。

以上はB-07のHuman Reviewに提出する**仕様案**であり、OQ-03の結論や採用済みDecisionとして扱わない。OQ-03の判断、割当記録の具体形式、Actor交代時の同等性の判定、利用可能なAgent・Model、交換の実現性は別途人間のReviewと必要な検証を要する。
