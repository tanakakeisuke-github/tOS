# Project Context Model

状態：Proposal / Human Review待ち。これは媒体をまたぐProject Contextの責務とBase Schemaの提案であり、承認済みのProject固有仕様、TaskのReady条件、Studio Template、Context Compilerの実装を確定しない。

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
| Current Goals / Current Focus | 現在取り組むべき焦点 | TaskのReadyや着手を暗黙に承認しない。 |
| Scope | 対象と対象外の境界 | 上位のPurpose・Constitutionと矛盾させない。 |
| Constraints | 守る原則、停止条件、外部制約 | 詳細規則の正本を参照する。 |
| Key Decisions references | 重要な判断へ到達する入口 | 判断理由・承認の正本は一つに保つ。 |
| Open Questions | 未決定の問いと影響範囲の入口 | 未決定を承認済み要件として扱わない。 |
| Current Milestone or Current Focus | 現在の節目または焦点 | 状態の根拠を示し、完了とProject全体の完成を混同しない。 |
| What's Next | 次の判断・準備・候補への入口 | 個別のReady承認を代替しない。 |
| Knowledge Map | Taskに必要な正本へ進む読み道 | 全読を要求せず、Task別Input Contextへ戻す。 |

`Current Goals / Current Focus` と `Current Milestone or Current Focus` は、一方を同じ見出しに統合してよい。Projectに該当しないfieldは「該当なし」と短く記し、媒体固有の仮定で置き換えない。

## Extensions

Studio TemplateはBase Schemaの外側に、媒体固有のextensionを定義できる。たとえばGameなら体験目標・対応機種・Playtestの入口、Filmなら尺・撮影制約・試写の入口を追加できる。ただし、その詳細なfield、必須性、評価方法はTemplateまたはProjectが所有し、共通Base Schemaへ昇格させない。

extensionは、Base fieldと同じ概念を別の正本として複写せず、対象媒体・所有者・適用Template版・詳細の正本を明示する。ProjectがTemplateを使わない場合も、Base Schemaは利用できる。

## Maintenance and Use

Current State、Current Focus、Open Questions、What's Nextを変更するTaskは、参照先の版・承認状態・実施結果と照合する。情報が古い、根拠が不明、既存仕様と矛盾する場合は、Project Contextだけで解決せず、影響する作業を停止して人間の判断と正本の改訂を待つ。

Fresh WorkerはProject ContextをGlobal Orientationとして使い、その後はProjectの`START_HERE`、担当Issue、指定Input Contextに従う。Project ContextはTask固有の入力選択を置き換えず、長大なChatやContext Compilerの実装を前提にしない。
