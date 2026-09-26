# Project Context Model

状態：Human Review承認済み / Accepted Specification（[Project Context Human Acceptance](../outcomes/project-context-human-acceptance/README.md)）。これは媒体をまたぐProject Contextの責務とBase Schemaを定めるが、Project固有仕様、TaskのReady条件、Studio Template、Context Compilerの実装を確定しない。

## Purpose

Project Contextは、新しいChatやFresh Workerが、Taskの局所情報を読む前後にProject全体の目的・背景・現在地・次の論点を短時間で把握するための、小さなGlobal Orientationである。Project Context自体は地図であり、Purpose、Constitution、Specification、Decision、Outcome、担当Issueの新しい正本ではない。

本Modelは、Game / Film / Music / Publishing / Appその他のProject Repositoryで再利用できる共通部分だけを定める。媒体固有の制作段階、Role、成果物、評価基準はCore必須項目にしない。

## Layered Contextとの関係

Contextは `OS → Studio → Project → Task → Relevant Knowledge` の順に考える。OSとStudioは共通または媒体の前提を、ProjectはそのProjectの向きと現在地を、Taskは今回の仕事の条件を、Relevant KnowledgeはTaskに必要な正本と証拠を担う。

原則は **「Global Contextは小さく提供し、Local ContextはTaskごとに選択する」** である。Project Contextを読んでも、Task開始前には担当Issue、Ready承認、基準版、指定Input Context、目的、範囲、受入条件、依存、停止点を照合する。Relevant Knowledgeの選択と優先度、版・承認状態・矛盾の扱いは、対象ProjectのKnowledge Architectureに従う。

## Responsibilities and Boundaries

Project Contextは次を担う。

- Projectを一文で識別し、PurposeとBackgroundへ到達させる。
- Project全体のCurrent State、Current Focus、Open Questions、What's Nextを、状態と根拠を区別して示す。
- 詳細を所有する正本と、Task開始に必要な入口を結ぶ。
- Fresh Workerが「Projectは何か」「なぜ存在するか」「いまどこにいるか」「何が未決定か」「Task前に何を確認するか」を説明する足場を提供する。

Project Contextは次を担わない。

- 詳細な規則・Decision・Outcome・受入証拠の複写や再承認。
- Ready / Done、優先度、承認状態、矛盾の解決の自動判定。
- 全Projectに媒体固有の項目、Tool、保存形式、Automationを強制すること。

## Base Schema

各Projectは、以下を最小の見出しまたは同等の構造で持てる。値は簡潔に書き、詳細の正本へ参照を結ぶ。存在しない詳細を推測で埋めない。

| Base field | 役割 | 記載上の条件 |
|---|---|---|
| Project Summary | Projectを識別する短い説明 | 詳細な定義の正本へリンクする。 |
| Purpose | 存在理由と目指す価値 | Purposeの正本を再定義しない。 |
| Background | 成り立ち・必要になった文脈 | 現行規則と履歴を混同しない。 |
| Vision / Big Picture | 長期の方向と構造上の位置 | 将来構想と実装済み状態を区別する。 |
| Current State | 承認済み・実施済み・保留中の現在地 | 版、Issue、PR、Decision、Outcomeなど根拠へリンクする。 |
| Current Focus | 今、Projectが集中している焦点 | TaskのReadyや着手を暗黙に承認しない。 |
| Current Milestone | 現在の節目 | 該当しない場合は`N/A`とし、Project全体の完成と混同しない。 |
| Scope | 対象と対象外の境界 | 上位のPurpose・Constitutionと矛盾させない。 |
| Constraints | 守る原則、停止条件、外部制約 | 詳細規則の正本を参照する。 |
| Key Decisions references | 重要な判断へ到達する入口 | 判断理由・承認の正本は一つに保つ。 |
| Open Questions | 未決定の問いと影響範囲の入口 | 未決定を承認済み要件として扱わない。 |
| Future Design Areas / Architecture Roadmap | 目標へ至るために未設計の構造・中間層への入口 | Vision、Current State、Open Questionsと区別し、採用済み仕様や実装順として書かない。 |
| What's Next | 次の判断・準備・候補への入口 | 個別のReady承認を代替しない。 |
| Knowledge Map | Taskに必要な正本へ進む読み道 | 全読を要求せず、Task別Input Contextへ戻す。 |

Current Stateは「どこまで到達したか」、Current Focusは「今どこへ集中するか」、Current Milestoneは「現在の節目」を表し、相互に代用しない。Projectに該当しないfieldは`N/A`と短く記し、媒体固有の仮定で置き換えない。

## Extensions

Studio TemplateはBase Schemaの外側に、媒体固有のextensionを定義できる。たとえばGameなら体験目標・対応機種・Playtestの入口、Filmなら尺・撮影制約・試写の入口を追加できる。ただし、その詳細なfield、必須性、評価方法はTemplateまたはProjectが所有し、共通Base Schemaへ昇格させない。

extensionは、Base fieldと同じ概念を別の正本として複写せず、対象媒体・所有者・適用Template版・詳細の正本を明示する。ProjectがTemplateを使わない場合も、Base Schemaは利用できる。

## Maintenance and Use

Current State、Current Focus、Open Questions、What's Nextを変更するTaskは、参照先の版・承認状態・実施結果と照合する。情報が古い、根拠が不明、既存仕様と矛盾する場合は、Project Contextだけで解決せず、影響する作業を停止して人間の判断と正本の改訂を待つ。

Fresh WorkerはProject ContextをGlobal Orientationとして使い、その後はProjectの`START_HERE`、担当Issue、指定Input Contextに従う。Project ContextはTask固有の入力選択を置き換えず、長大なChatやContext Compilerの実装を前提にしない。

## Proposal Lifecycle and Adoption

本Proposalと[Knowledge ArchitectureのLayered Context](KNOWLEDGE_ARCHITECTURE.md#proposal--layered-context)は、既存の状態分類である「提案・Review中」から「承認済み」へ、次の手順で移行する。

1. **Proposal / Revision**：内容を編集し、状態は「提案・Review中」とする。この段階では実行上の契約にしない。
2. **Human Review**：Human Reviewerが対象commit、対象文書、修正要求と残課題を確認する。修正があればRevisionへ戻る。
3. **Human Approval**：人間が最終内容を承認し、正本となる承認記録をPRまたはReview記録の一方に指定する。承認は対象commitと範囲を明記する。
4. **Accepted Specification**：承認後、Merge前の状態更新で、本書を「Human Review承認済み / Accepted Specification」、Layered Context節を「追加ProposalとしてHuman Review承認済み」、rootのProject Context instanceを「Current / Human Review承認済み」へ変更し、同じ承認記録へリンクする。内容変更は行わない。
5. **Merge**：状態更新だけであることとリンク整合を確認してmainへ反映する。mainのmerge commitを適用版として辿れるようにする。

Human Approval後に本文へ実質的な変更が生じた場合は、状態更新やMergeを進めずRevision / Human Reviewへ戻す。このRevision Request自体はHuman Approvalとして扱わない。
