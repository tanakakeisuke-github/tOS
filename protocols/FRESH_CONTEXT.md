# tOS — Fresh Context Protocol

状態：Draft。Fresh Context by defaultは指定原則。Packageと確認手順は提案。

## 目的

長い会話の再利用に頼らず、Taskに必要なKnowledgeと承認範囲から作業を開始する。Freshとは、必要な知識を捨てることではなく、正本から意図的に選び直すこと。品質向上の程度は今後検証する。

## Packageの構成（案）

入口とConstitution、assigned Task、目的・範囲・受入条件、Human Approval、適用OS Version、関連Specification / Decision、必要Artifact / code、既知の制約、未決定事項、停止条件を含める。ファイル全体が不要なら、節の参照と前提が分かる範囲に限定する。

優先順位はSpecification → Decision → Outcome → Transcript。HISTORYとTranscriptは経緯の調査が必要なときだけ追加する。会話にあった未採用案を規範へ混入させない。

## 手順

1. 対象Taskと参照版を固定する。割当がなければ理解の説明までに留める。
2. 必要な参照を選び、承認と適用範囲を確認する。
3. Fresh Workerが目的、根拠、成果、停止条件、未決定を説明する。
4. 欠落や矛盾があればPackageや正本の不足として返す。
5. 承認済み範囲だけ実行し、OutcomeとHandoffを正本候補へ戻す。

Contextの混在や目的変更があれば、[Session Model](../specifications/SESSION_MODEL.md)に従って切替を検討する。Cloud AI / Local AIとも同じ原則で扱う。

## Context Compilerとの関係

当面は人間または承認された担当がRequired Contextを手動で選ぶ方式を検討できる。自動Compilerは[構想](../specifications/KNOWLEDGE_ARCHITECTURE.md)であり未実装。Packageの短さだけで成功と判断せず、必要情報の欠落と誤解を評価する。

容量制約で必要情報が入らない場合は、段階的な参照またはTask分割を提案する。承認や制約を黙って削って作業を続けない。
