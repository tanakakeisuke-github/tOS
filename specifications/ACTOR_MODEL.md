# tOS — Actor Model

状態：Draft。概念分離と交換可能性は指定原則。以下の用語境界と記録項目は文書化案。

## 四つの概念

| 概念 | 意味 | 交換時に保つもの |
|---|---|---|
| Role | 責務・成果・判断範囲を定める役割 | 責任と受入条件 |
| Actor | Roleを担う主体。Human / Cloud AI / Local AI | Task契約と権限境界 |
| Agent | AIがContext・指示・tool・実行制御を使って働く仕組み | 入出力、承認、証跡 |
| Model | Agent等が利用する推論モデル | Taskに必要な能力と品質条件 |

RoleにActorを割り当て、AI ActorはAgentを介してModelを利用できる。Human ActorにModelの指定は必要ない。実際のAgent構成・複数Modelの利用・Actor識別方法は未決定。

Role名を製品名やModel名にしない。同じRoleを人間、Cloud AI、Local AIが担う可能性を持たせる一方、能力・権限・利用可能なtoolが同一とは仮定しない。交換時には対象Taskへの適性を検証する。

## 権限と責任

Human Approval before Ready and Doneは人間に留保する。Actorとして共通に扱うことは、人間の承認権限をAIへ委譲することではない。

Workerは承認範囲のArtifactと証跡を作る。Reviewerは受入条件に照らして評価する。可能なら別Actor・別Contextで担当し、別Modelの利用も評価候補とする。分離できない場合は自己レビューと明記し、人間の判断に必要な限界を提示する。

OrganizationはRoleの組合せと担当を変更できる。Knowledgeは特定の部門Chatや担当者の記憶に閉じ込めず、対象と根拠で参照できる形を保つ。

## Routingと能力評価（将来候補）

Capability RegistryとTask Routerは構想段階。品質、費用、応答時間、必要tool、素材へのアクセス、機密性、利用可能な計算資源などを判断材料とする案がある。Cloud / Localだけで性能や安全性の優劣を決めない。

採用するAgent、Model、Local hardware、routing policy、fallback条件は未決定。担当を交換する際はContext Package、権限、版、Outcome形式を引き継ぎ、適合しなければSTOPする。

Runtime / Orchestrator / Vendorの選択はこのモデルより下位に置く。技術候補は[Technology Radar](../research/TECHNOLOGY_RADAR.md)で扱う。
