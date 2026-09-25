# tOS — Bootstrap Knowledge v0.1 Issue Map

**状態：B-01〜B-12は人間の受入承認済み。B-12はR5全ケース合格を受けDone承認済み。**

B-01〜B-11とPR #28・#30は承認・反映済み。B-12は[R5結果](../outcomes/b12-r5/README.md)を人間が受け入れ、[Done・merge・closeを承認](../outcomes/b12-r5/HUMAN_ACCEPTANCE.md)した。実施状態の正本は[Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)と[PR #26](https://github.com/tanakakeisuke-github/tOS/pull/26)。過去試験の原結果は維持する。次のTaskは個別のReadyを必要とする。

これはBootstrap Knowledgeを作るための作業分解案です。下記の成果物パスと検証手順も提案であり、現在存在するファイルと将来の成果物を区別します。初回の保存作業はこのMapまでとし、PR #2の承認後、個別に承認されたB-01へ進みました。

## 粒度と進め方の提案

一つの明確な目的について、Fresh AIが一度のSessionで理解→作成→自己確認できる認知負荷を基準にします。Protocolsは「仕事を着手可能にする」と「成果を受け渡し評価する」の二目的に分割しました。受入に複数の独立した判断が必要になった場合はSPLITを提案し、人間が分割を確認します。

各候補のInput Contextは限定した読み取り一覧です。依存Issueが承認され、その成果物が利用可能になってからReady判断を行います。Dependenciesは実行順序であり、依存先の入力を再帰的に全読する指示にはしません。承認済み成果物は登録時にcommitまたは版を固定する案です。

共通入力は「割り当てた候補の本文と承認記録」「B-01完了後のSTART_HERE」「B-02完了後のCONSTITUTION」です。以下にはそれ以外の入力を列挙します。B-01はこのMapの共通規約を入口にし、将来のSTART_HEREへ依存しません。History / Transcript / 旧Draft PRは理由調査が必要な場合の追加参照とし、標準入力に含めません。

## 依存順

| 順番の目安 | ID / Title | 直接のDependencies |
|---|---|---|
| 1 | B-01 — Purposeと入口 | この保存PRとMapのHuman Review、B-01の着手承認 |
| 2 | B-02 — Constitution | B-01 |
| 3 | B-03 — Core Architecture | B-02 |
| 4 | B-04 — Knowledge Architecture | B-03 |
| 5 | B-05 — Work Model | B-03、B-04 |
| 6 | B-06 — Session Model | B-04、B-05 |
| 7 | B-07 — Actor Model | B-03、B-05、B-06 |
| 8 | B-08 — Discussion / Task / Triage Protocols | B-04、B-05、B-07 |
| 9 | B-09 — Fresh Context / Handoff / Review Protocols | B-06、B-07、B-08 |
| 10 | B-10 — Technology Evolution | B-03、B-08、B-09 |
| 11 | B-11 — Integration Review | B-01〜B-10すべて |
| 12 | B-12 — Fresh Worker Acceptance Test | B-11の指摘解消とテスト入力の承認 |

まずこの順で逐次実施する案です。自動実行・一括登録の計画ではありません。各IssueのReady前・Done前にHuman Gateを置きます。Mapの承認だけで全候補がReadyになる扱いにはしません。

## B-01 — Purposeと入口

- **ID / Title**：B-01 / Define tOS Purpose and Bootstrap Entry
- **Purpose**：tOSが何のためにあるか、Fresh Workerがどこから読むかを定義する。
- **Why it matters**：目的と入口を最初に固定することで、各仕様の判断軸を共有できる。
- **Input Context**：[Future Vision](../vision/FUTURE_VISION.md)、[Creation Lifecycle](../vision/CREATION_LIFECYCLE.md)、[READMEの位置づけ・停止点](../README.md)。後続候補の概略は上表のみ。
- **Deliverable**：将来の `specifications/PURPOSE.md` と短い `START_HERE.md`。READMEは入口へのリンクに整理し、Purpose本文を重複保持しない。
- **Acceptance Criteria**：目的・対象媒体・保持する価値を説明できる。v0.1の範囲と将来構想を区別する。START_HEREから担当Issueと必要情報へ到達でき、未作成の文書を必読にしない。割当や承認がない場合の停止点が分かる。
- **Dependencies**：今回のKnowledge保存・MapのHuman ReviewとB-01の着手承認。
- **Human Approval Point**：Ready前にPurposeの範囲と入力を確認。Done前に目的の再構成と入口の分かりやすさを承認。
- **Reviewer expectation**：可能ならFresh Reviewerがこの限定入力から目的・現在地・次の判断を言い直し、入力にない範囲が追加されていないか確認する。

## B-02 — Constitution

- **ID / Title**：B-02 / Define Constitution
- **Purpose**：変わりにくいPrinciplesと、人間が判断する境界を定義する。
- **Why it matters**：以後の設計・変更判断を一貫させる。
- **Input Context**：承認済み `specifications/PURPOSE.md`、[Operating Model](../vision/OPERATING_MODEL.md)、[Future Visionの協働・保持対象](../vision/FUTURE_VISION.md)。
- **Deliverable**：将来の `CONSTITUTION.md` と `START_HERE.md` の読み順更新。
- **Acceptance Criteria**：Human Gate、Scope管理、Knowledge保持、交換可能性を原則として説明する。原則と手段・仮説を区別する。詳細Protocolをここに複製しない。仕様との矛盾時の停止・判断先を定義する。
- **Dependencies**：B-01。
- **Human Approval Point**：Ready前に原則化する範囲を確認。Done前に原則と例外の扱いを承認。
- **Reviewer expectation**：特定媒体・Project・Vendorへの固定や、未検証仮説の規則化がないか照合する。

## B-03 — Core Architecture

- **ID / Title**：B-03 / Define Core Architecture Boundaries
- **Purpose**：tOS / Studio Template / Projectと交換可能な実行層の境界を定義する。
- **Why it matters**：共通の制作基盤を保ちつつ、媒体と技術の変更を局所化する。
- **Input Context**：承認済み `specifications/PURPOSE.md`、[Future Vision](../vision/FUTURE_VISION.md)、[Creation Lifecycle](../vision/CREATION_LIFECYCLE.md)。
- **Deliverable**：将来の `specifications/CORE_ARCHITECTURE.md`。
- **Acceptance Criteria**：各層の責務・入出力・依存方向が説明できる。Runtime / Orchestrator / Vendorの交換箇所と保持する契約を示す。Project Bootstrapを将来構想として位置づける。媒体固有の制作段階はTemplate側へ置く。
- **Dependencies**：B-02。
- **Human Approval Point**：Ready前に扱う境界を確認。Done前にCoreの最小範囲と拡張点を承認。
- **Reviewer expectation**：二つの媒体を例に責務を追い、Coreに作品固有の前提が入らないか、実装選定を先取りしていないか確認する。

## B-04 — Knowledge Architecture

- **ID / Title**：B-04 / Define Canonical Knowledge and Reading Routes
- **Purpose**：Fresh WorkerがTaskに必要な正式情報へ到達する構造を定義する。
- **Why it matters**：Contextの肥大化と正本の重複を防ぎ、承認状態と理由を復元できるようにする。
- **Input Context**：承認済み `specifications/CORE_ARCHITECTURE.md`、[Operating Modelの知識・Context Compiler](../vision/OPERATING_MODEL.md)、[FindingsのF-02〜F-04](FINDINGS.md)、[READMEの記録の位置づけ](../README.md#記録の位置づけ)。
- **Deliverable**：将来の `specifications/KNOWLEDGE_ARCHITECTURE.md`。必要な範囲で `START_HERE.md` の参照順を更新。
- **Acceptance Criteria**：Specification → Decision → Outcome → Transcriptの優先度、適用版・承認状態・矛盾の扱いを定義する。Principles / Requirements / Decisions / Learnings / Failures / Benchmarks / Project Historyの保存先を対応づける。One concept, one canonical homeを保ち、visionと将来仕様の境界・移行方法を示す。TranscriptとHistoryを標準全読から外し、Task別入力選択とOpen Questionの管理を定義する。
- **Dependencies**：B-03。
- **Human Approval Point**：Ready前に情報分類の範囲を確認。Done前に正本・状態・読み順・競合解決を承認。
- **Reviewer expectation**：架空のTaskを一つ選び、必要情報までの参照と、仕様・Decisionの不一致時の停止を文書上で追えるか確認する。

## B-05 — Work Model

- **ID / Title**：B-05 / Define Discussion and Small Task Model
- **Purpose**：検討から着手・完了に至る仕事の単位と状態を定義する。
- **Why it matters**：会話の継続と、実行・完了承認の境界を明確にする。
- **Input Context**：承認済み `specifications/CORE_ARCHITECTURE.md`、`specifications/KNOWLEDGE_ARCHITECTURE.md`、[Operating Modelの仕事・Gate](../vision/OPERATING_MODEL.md)、[Creation LifecycleのPhase 4〜5](../vision/CREATION_LIFECYCLE.md)。
- **Deliverable**：将来の `specifications/WORK_MODEL.md`。
- **Acceptance Criteria**：Discussion / Task / Issueの関係を定義する。1 Task = 1 small objectiveと分割判断を示す。TriageとReady前・Done前Human Gateの位置、未決定・Blockedの扱いを記す。状態の遷移条件と承認記録の参照先を説明する。
- **Dependencies**：B-03、B-04。
- **Human Approval Point**：Ready前に扱う仕事の状態を確認。Done前に着手・完了条件と承認境界を承認。
- **Reviewer expectation**：DiscussionからSmall Taskへの移行例と、未承認のTaskが止まる例を照合する。ツール上の状態変更を承認の代用にしていないか確認する。

## B-06 — Session Model

- **ID / Title**：B-06 / Define Fresh Session and Continuity
- **Purpose**：短命なAI Sessionをまたいで、長寿命の仕事を再開できるようにする。
- **Why it matters**：会話全文に依存せず、必要なContextと残課題を受け渡すため。
- **Input Context**：承認済み `specifications/WORK_MODEL.md`、`specifications/KNOWLEDGE_ARCHITECTURE.md`、[Operating ModelのSession・Context Compiler](../vision/OPERATING_MODEL.md)、[FindingsのF-01・F-02・F-05](FINDINGS.md)。
- **Deliverable**：将来の `specifications/SESSION_MODEL.md`。
- **Acceptance Criteria**：1 Issue = 原則1 Fresh Workerの適用、Session開始・終了・中断・再開の必要情報を定義する。Worker / Reviewer分離と例外の記録を定義する。入力不足・矛盾時の停止、成果・残課題の保存先を示す。Context Compilerは将来構想として区別する。
- **Dependencies**：B-04、B-05。
- **Human Approval Point**：Ready前にSessionの対象場面を確認。Done前にFreshの条件・継続例外・再開条件を承認。
- **Reviewer expectation**：途中終了したTaskを新しいSessionへ渡す例で、Scope・承認・未解決事項が残るか確認する。

## B-07 — Actor Model

- **ID / Title**：B-07 / Define Role, Actor, Agent and Model
- **Purpose**：責任と実行主体・技術の関係を分けて定義する。
- **Why it matters**：人間の承認責任を保ち、Cloud AI / Local AIや実行技術を交換できるようにする。
- **Input Context**：承認済み `specifications/CORE_ARCHITECTURE.md`、`specifications/WORK_MODEL.md` のGate、`specifications/SESSION_MODEL.md` の実行・Review関係、[Future Visionの協働](../vision/FUTURE_VISION.md)。
- **Deliverable**：将来の `specifications/ACTOR_MODEL.md`。
- **Acceptance Criteria**：Human / Cloud AI / Local AIとRole / Actor / Agent / Modelの関係、責務、割当変更を定義する。Human承認とAI Reviewを区別する。Runtime等との境界をB-03へ参照で結ぶ。具体Vendor選定を必須にせず交換例を説明できる。
- **Dependencies**：B-03、B-05、B-06。
- **Human Approval Point**：Ready前に責務・権限の範囲を確認。Done前にActor分類・割当・承認責任を承認。
- **Reviewer expectation**：同じRoleのActorまたはModelを交換する例とHumanが担う例を追い、関係の混同を確認する。

## B-08 — Discussion / Task / Triage Protocols

- **ID / Title**：B-08 / Define Work Intake Protocols
- **Purpose**：検討事項を、承認判断できる小さな仕事へ整える手順を作る。
- **Why it matters**：Discussionから暗黙に実行へ進まず、目的と範囲を確認できるようにする。
- **Input Context**：承認済み `specifications/WORK_MODEL.md`、`specifications/ACTOR_MODEL.md` の責任、`specifications/KNOWLEDGE_ARCHITECTURE.md` の状態・記録先、[Operating ModelのSTOP / SPLIT / PROPOSE](../vision/OPERATING_MODEL.md)。
- **Deliverable**：将来の `protocols/DISCUSSION.md`、`protocols/TASK.md`、`protocols/TRIAGE.md`。各文書は一つの入口手順に限定。
- **Acceptance Criteria**：各Protocolに入力・担当・手順・出力・停止条件を記す。問い→選択肢→Task案→Ready前承認を追える。STOP / SPLIT / PROPOSEとCurrent / Next / Labへの振分けの接続点を示す。モデルの定義は参照し、重複しない。
- **Dependencies**：B-04、B-05、B-07。
- **Human Approval Point**：Ready前に三つの手順を一つの認知負荷で扱えるか確認。Done前に着手までの手順を承認。
- **Reviewer expectation**：入力不足、複数目的、OS改善提案の三例について、それぞれの停止・分割・振分け先を追う。

## B-09 — Fresh Context / Handoff / Review Protocols

- **ID / Title**：B-09 / Define Delivery and Review Protocols
- **Purpose**：限定Contextで開始し、成果を次の担当と人間へ受け渡す手順を作る。
- **Why it matters**：作成・自己確認・独立Review・完了承認を根拠でつなぐため。
- **Input Context**：承認済み `specifications/SESSION_MODEL.md`、`specifications/ACTOR_MODEL.md` のWorker / Reviewer / Human責任、`protocols/TASK.md` の受入条件、`specifications/KNOWLEDGE_ARCHITECTURE.md` の入力選択・記録先。
- **Deliverable**：将来の `protocols/FRESH_CONTEXT.md`、`protocols/HANDOFF.md`、`protocols/REVIEW.md`。
- **Acceptance Criteria**：開始時のContext確認と不足時停止、成果・実施検証・未実施検証・残課題の引き継ぎ、PR→Reviewer→Humanの順序を示す。可能な限りFresh / 分離したReviewと例外記録を定める。Done前Human Gateと差戻しを追える。
- **Dependencies**：B-06、B-07、B-08。
- **Human Approval Point**：Ready前に対象となる受渡し場面を確認。Done前に完了証拠と差戻し・再開の手順を承認。
- **Reviewer expectation**：合格例と検証未実施の例を文書上で追い、後者が完了扱いにならないことを確認する。

## B-10 — Technology Evolution

- **ID / Title**：B-10 / Define Evolution, Freeze and Rebuild Policy
- **Purpose**：探索・実験・採用・版固定・撤回の判断過程を定義する。
- **Why it matters**：制作中の安定性と技術更新を両立し、再構築時にも知識を残すため。
- **Input Context**：[Evolution Model](../vision/EVOLUTION_MODEL.md)、[Future Visionの保持対象](../vision/FUTURE_VISION.md)、承認済み `specifications/CORE_ARCHITECTURE.md` の交換境界、`protocols/TRIAGE.md`、`protocols/REVIEW.md`。
- **Deliverable**：将来の `specifications/TECHNOLOGY_EVOLUTION.md` と `research/TECHNOLOGY_RADAR.md`。Radarは候補・未評価状態の記録構造まで。
- **Acceptance Criteria**：WATCH / TRIAL / ADOPT / HOLDとCurrent / Next / Labを別軸で定義する。評価→承認→次版→測定→継続/撤回、Freeze、Current例外、Rebuild時の保持・比較を説明する。既存の候補を採用済みと扱わず、未評価を表現できる。文書作成と実際のPoC・導入を区別する。
- **Dependencies**：B-03、B-08、B-09。
- **Human Approval Point**：Ready前に扱う進化方針を確認。Done前に採用・Freeze・例外・Rollbackの判断条件を承認。
- **Reviewer expectation**：新技術の発見だけでCurrentが変わらないこと、採用後に失敗を記録し戻せる判断経路を確認する。

## B-11 — Integration Review

- **ID / Title**：B-11 / Review Bootstrap Knowledge Integration
- **Purpose**：承認済み文書間の整合性と、Fresh Worker受入の準備を確認する。
- **Why it matters**：個別文書の妥当性だけでは、読み順・責任・状態の不一致を見落とすため。
- **Input Context**：承認済み `START_HERE.md` を入口としたB-01〜B-10の成果物、当Mapの受入条件とOpen Questions。必要な設計意図の照合には該当vision節だけを選ぶ。
- **Deliverable**：将来の `bootstrap/INTEGRATION_REVIEW.md`、`bootstrap/ACCEPTANCE_PLAN.md`。指摘・解消証拠・未解決事項と、B-12の限定入力・期待回答・採点条件を記録する。
- **Acceptance Criteria**：名称・責務・Gate・Knowledge優先度・版・参照先・正本の重複を横断確認する。必須文書一覧ではなく用途別読み順を確認する。Open Questionのblocking / deferred判断を人間に提示する。B-12の合否条件を実施前に固定する。
- **Dependencies**：B-01〜B-10すべて。
- **Human Approval Point**：Ready前にReview対象版を固定。Done前に指摘解消、残課題の扱い、B-12の入力と合格基準を承認。
- **Reviewer expectation**：横断Reviewは仕様変更を混ぜず、指摘を参照先付きで出す。大きすぎる場合は観点別Reviewと統合判断へのSPLITを提案し、修正は該当の小さなTaskへ戻す。

## B-12 — Fresh Worker Acceptance Test

- **ID / Title**：B-12 / Test Fresh Worker Onboarding
- **Purpose**：元の会話を継承しないFresh Workerが、GitHubのKnowledgeだけでTaskを理解できるか実測する。
- **Why it matters**：文書を書いたことと、引き継げることを区別するため。
- **Input Context**：試験担当は承認済み `bootstrap/ACCEPTANCE_PLAN.md` と対象commitを使用。受験Workerには `START_HERE.md` と承認された小さな試験Taskを渡し、入口から指定されたKnowledgeだけを読む。期待回答は採点担当が保持する。
- **Deliverable**：将来の `outcomes/BOOTSTRAP_ACCEPTANCE.md`。入力版、使用したActor / Agent / Model、渡したContext、質問・回答、採点、指摘、未実施項目を記録する。
- **Acceptance Criteria**：目的・制作フロー・CoreとTemplateの境界・担当Taskの範囲・Human Gate・未決定事項を出典付きで説明する。不足入力と未承認Taskで止まる例を試す。実際の出力を計画の基準で採点し、失敗は修正・再試験へ戻す。未実施は未実施と記し、合格を推定しない。
- **Dependencies**：B-11の指摘解消と試験計画のHuman Approval。
- **Human Approval Point**：Ready前に実施条件・入力・採点者を確認。Done前に証拠と結果を確認し、Bootstrap Knowledgeの受入可否を判断。
- **Reviewer expectation**：作成Sessionと分離した評価を行い、会話履歴の混入、期待回答の先渡し、出典のない補完を確認する。受入合格をtOS本体の稼働・完成・Freezeと同一視しない。

## Open Questions — Human Reviewで判断する事項

以下が未決定事項の今回の集約先です。解決時は判断理由・承認記録・反映先を残す提案です。Owner Issueは整理担当の候補であり、AIに決定権を与える意味ではありません。

| ID | 未決定事項 | 整理担当 / 判断が必要な時点 |
|---|---|---|
| OQ-01 | Bootstrap Knowledge受入後、tOS v0.1の実際の範囲・完成条件をどこまでにするか | B-01 / v0.1範囲の承認前。B-12完了だけでは解決しない |
| OQ-02 | Human Gateの担当・記録形式、mergeとDoneの関係 | B-02・B-05でHuman判断とmerge・Doneの区別、承認記録の要件を承認済み。具体的な担当者・記録先はTaskごとに指定 |
| OQ-03 | Role / Actor / Agent / Modelの関係、割当と権限 | B-07のActor Modelを承認済み。具体的な記録形式や交換可能性の検証は未決定・未実施 |
| OQ-04 | Session継続・Reviewer兼任を許す条件と記録 | B-06・B-09で例外記録とHuman判断を承認済み。具体的な許容条件はTaskごとに確認 |
| OQ-05 | 承認済みSpecificationと新Decisionが競合したときの優先・更新手順 | B-04のKnowledge Architectureで衝突時の停止・人間の判断・正本改訂手順を承認済み。個別の衝突はその手順で判断 |
| OQ-06 | Freeze条件、Currentの例外変更、Projectの版移行・Rollback | B-10で判断条件を承認済み。対象Projectの具体的な移行・Rollback可否は個別判断 |
| OQ-07 | Project Bootstrapの入力・生成物・承認・自動化範囲 | B-03で境界を整理 / 機能の計画前。後続へ保留可能 |
| OQ-08 | Context CompilerとHuman Viewの実装時期・評価方法 | B-04・B-06で構想境界を整理 / 実装計画前。後続へ保留可能 |
| OQ-09 | Fresh Worker試験契約はPR #28で改訂承認済み。追加検証でランタイムのModel応答を取得したが、全取得経路の隔離・監査は未成立 | 環境成立後、改訂後の入力版・条件・Readyを固定して再試験 |
| OQ-10 | 分解案はPR #2で承認済み。個別候補は着手時に粒度を確認する | B-01〜B-12受入承認済み。次のTaskは個別のReadyが必要 |
| OQ-11 | PR #2を採用しmainへ反映済み。旧Draft PR #1を閉じるかは未決定 | B-01はPR #2の成果を入力とする。旧案は変更せず保持 |

## 正本の重複とContext量への対策案

後続Issueは担当概念の正式な保存先を一つ選び、visionを意図・履歴・参照へ整理します。Findingsは観察・仮説の記録として残し、検証された結果はOutcomeへ、採用した規則は仕様へリンクで結びます。

Issue登録時にこのMapの担当候補だけを渡し、入力を具体的な版・必要な節へ限定します。Mapは計画の索引、実際の着手条件・承認・進捗は登録したIssueを参照する構成へ更新する案です。読めない入力や未承認の依存があればReadyにせず、Human Reviewへ戻します。
