# tOS — Core Architecture

状態：Draft。レイヤー分離は指定された構想。下記の責務整理は文書化案であり、配備構成やRepository数の決定ではない。

## 論理レイヤー

| レイヤー | 責務 | 次へ渡すもの |
|---|---|---|
| Constitution | 正本、承認、知識継承、交換性の原則 | すべての判断の制約 |
| tOS Core | Discussion / Task / Triage / Knowledge / Session / Review / Learning | 共通の仕事と知識の契約 |
| Studio Template | 媒体ごとのRole、Workflow、Artifact、品質観点 | 制作種別に適した構成 |
| Creative Project | 作品の目的、要求、採用OS Version、固有Decisionと成果 | 承認済みTaskと受入条件 |
| Execution | Human / Cloud AI / Local AIによる作業と証跡生成 | Artifact、Outcome、発見 |

Runtime / Orchestrator / VendorはExecutionを支える交換可能な下位レイヤーである。TemplateはGame / Film / Music / Publishing / Appなどに展開できる。Templateの種類、初版の対象、具体的なファイル形式は未決定。

この分離は論理的な責務境界であり、各レイヤーにRepositoryやサービスを一つずつ作る指示ではない。物理構造は後続の設計で評価する。

## 情報と仕事の流れ

ChatGPTでDiscussion / Planning / Directionを行い、選択肢と理由を整理する。採用するKnowledgeはHuman Reviewを経てGitHubへ記録する。Triageが仕事候補を評価し、人間が範囲を承認したTaskに必要なContextを渡す。ExecutionからArtifact・検証結果・学びをGitHubの記録へ戻す。

GitHubは将来のSource of Truth / Project Memory / Work Managementの中心である。大きな映像・音声等の実体の保存先は未決定であり、GitHubには識別子・版・所在・関連Task / Decision・検証証跡を残す構想とする。正本の中心であることと、全バイナリを同じ場所へ置くことは分けて考える。

Human Viewは正本から作る派生表示として位置づける。表示媒体と同期方法は未決定。外部表示だけを変更して正本のDecisionを上書きしない。

## 部門横断Communication

Role間では依頼目的・期待するArtifact・依存関係・受入条件・根拠を共有する。特定の部門Chatにしか存在しない決定を作らない。責任の再配分後も同じKnowledgeを参照できるようにする。メッセージ配送や自動ルーティングの実装は未決定。

## 変更と学習の流れ

Projectの観察から共通するFindingを抽出し、OS Improvement ProposalとしてTriageへ送る。承認されたPrototypeとValidateを経てNext Versionに反映する。Creative Projectの採用版を自動更新しない。

API、データschema、起動方法、Runtime製品、Agent設定、GitHub Projects構成はこのDraftで確定しない。[Actor Model](ACTOR_MODEL.md)、[Knowledge Architecture](KNOWLEDGE_ARCHITECTURE.md)、[Technology Evolution](TECHNOLOGY_EVOLUTION.md)が各境界の意図を定義する。
