# Project Context Revision — Fresh Worker Consistency Outcome

状態：Revision後の内容整合確認を実施済み / 初回Fresh Worker試験と同じく、期待した理解が得られた結果であり、Project Contextの有効性の証明またはHuman Acceptanceではない。B-12の契約・結果・Acceptance evidenceを変更または再採点しない。

## Conditions

| 項目 | 実施内容 |
|---|---|
| 対象commit | `c8f0c4620ac4905f8952689b7538d1934821ebfc` (`docs/project-context-model`) |
| Worker | 元会話を渡さない独立Fresh Worker / 別Session |
| 初期入口 | `PROJECT_CONTEXT.md`、`START_HERE.md` |
| 参照範囲 | GitHubから新規cloneした対象branch。既存local checkoutと他資料の参照を禁止 |
| Revision観点 | 質問4でOpen Questionsと未設計Architecture領域を識別し、採用済み仕様・Ready Taskと区別できるか |

## Recorded Worker Response Summary

以下はWorker回答の意味を変えず、Revision Outcome用の文体に整理した要約である。逐語のToolログではない。

### 1. tOSとは何か

tOSは、人間とAIがSessionをまたいで作品制作を継続するための、AI-native制作OSを目指すRepositoryである。会話だけに残りがちな目的、仕様、意思決定、受け渡し、検証結果、失敗や学びを、版・出所・承認状態とともにGitHub上へ保存し、次の人間やAIが復元できるようにする。

採用済みの基本構造はtOS Core、Studio Template、Projectの三層である。tOS Coreは媒体に依存しない仕事・知識・Review・Human Gateの共通枠組み、Studio Templateは媒体固有のRole・成果物・Workflow・評価方法を具体化する層、Projectは個別作品の目的・体験・制約・優先順位・制作範囲・完成判断を所有する層である。三層の責務と依存方向は承認済みだが、Studio Templateや実制作システムが実装済みという意味ではない。

### 2. なぜ存在するか

短命なAI Sessionや長いChatだけに制作判断を依存すると、次のSessionや担当者が「何を、なぜ、どの承認範囲で進めていたか」を復元しにくいためである。目的、要件、判断理由、結果、検証、未決定事項をSession外へ残し、Fresh Workerが限定された正本からTaskを安全に再開できるようにする。人間が開始と完了を判断し、制作経験を次の作品と制作環境の改善へ戻し、実行技術を変更しても責任と知識を引き継げる方向を目指す。技術交換の容易さやAIによる再構築コスト低下は、現時点では将来方向または検証前の仮説である。

### 3. 現在どこまで進んでいるか

Bootstrap KnowledgeのB-01〜B-12は人間の受入承認済みである。Purpose、Constitution、Core Architecture、Knowledge / Work / Session / Actor Model、Protocol、Technology Evolution、Integration Review、Fresh Worker Acceptance Testまでの土台が整っている。

B-12のR5はP 12/12・695字・形式適合、M/U合格で、人間が結果を受入れ、B-12をDone承認し、PR #26のmergeとIssue #25のcloseを承認済みである。ただし、B-12とBootstrap Knowledgeの受入は、tOS全体の完成、v0.1 Freeze、Creative ProjectのReadyを意味しない。次のProject-wide Milestoneも`N/A`で未承認である。

このbranchのProject Context Model、Layered Context、rootのProject Context instanceはProposal / Revision・Human Review待ちであり、B-01〜B-12の承認済みSpecificationと混同できない。

### 4. 次に何が未設計・未決定か

Open Questionsは、OQ-01（tOS v0.1の実際の範囲と完成条件）、OQ-07（Project Bootstrapの入力・生成物・承認・自動化範囲）、OQ-08（Context CompilerとHuman Viewの実装時期・評価方法）である。Actor割当の具体形式、Actor交換時の同等性、Session例外のTask別条件、Projectごとの移行・Rollbackも個別判断または未検証である。

Open Questions以外の未設計Architecture領域は次のとおりである。Architecture Roadmapは未設計領域を見失わないための地図であり、採用済みSpecification、確定した実装順、着手承認ではない。

- **tOS Core**：Purpose、原則、三層境界、Knowledge、Small Task、Session、Actor、Protocol等の土台は採用済み。v0.1全体の必須範囲・完成条件と具体的実装・運用基盤は未決定。
- **Studio Template Model**：Coreを媒体固有制作へ具体化する責務と境界は採用済み。媒体横断のTemplate基本構造、Role、責任、Workflow、Production Stage、Artifact、Quality Gateは未設計で、具体的Template仕様やReady Taskではない。
- **Organization / Cross-role Collaboration**：Role / Actor / Agent / Modelの区別とHuman Gateとの境界は採用済み。複数RoleがDiscussion・Decision・Taskを横断して協働する方法と統合判断の責任は未設計で、Cross-role Collaboration仕様として未採用。
- **Production Planning**：Small TaskのTriage、Ready、Review、Doneは採用済み。Creative ProjectをMilestone、Epic、Feature、Small Taskへ分解して上流計画と実行を接続するModelは未設計で、Planning Architectureとして未採用。
- **Project Bootstrap**：三層をまたぐ将来の入口としての位置づけはある。入力、生成物、Role、Repository、Knowledge、Milestone、承認、Automation範囲は未設計で、機能仕様・実装ではない。
- **Creative Project / Production**：企画から制作、評価、完成、振り返りまでの長期Lifecycleは保存済み。媒体別の実行方法、成果物、品質判断、完成条件は未設計で、現在はCreative Project Readyではない。
- **Layered Context / Project Context Model**：`OS → Studio → Project → Task → Relevant Knowledge` とBase SchemaはProposal / Revision・Human Review待ちであり、まだ承認済み契約ではない。
- **Context Compiler / Human View**：将来構想であり、自動抽出、承認判定、優先度判定、品質保証、実装時期は未決定。

### 5. Task開始前に何を確認するか

`PROJECT_CONTEXT.md`をGlobal Orientationとして読み、`START_HERE.md`、Purpose、Constitution、担当Issueへ進む。人間によるReady承認の対象Task・範囲・版・記録先、基準commit、指定Input Contextの所在・出所・適用版・承認状態、Taskの目的・範囲・受入条件・依存・停止点・担当Actorを確認する。

不足・矛盾・承認範囲外の判断があれば、箇所・版・影響・判断者・再開条件を記録して影響する作業を止める。割当またはReady承認がなければ開始せず、Issue、ラベル、PR、merge、CI、AI Review、B-12合格を別TaskのReady承認として扱わない。

## Files Reported as Read

1. `PROJECT_CONTEXT.md`
2. `START_HERE.md`
3. `specifications/PURPOSE.md`
4. `CONSTITUTION.md`
5. `specifications/CORE_ARCHITECTURE.md`
6. `vision/FUTURE_VISION.md`
7. `vision/CREATION_LIFECYCLE.md`
8. `bootstrap/ISSUE_MAP.md`
9. `specifications/WORK_MODEL.md`
10. `specifications/ACTOR_MODEL.md`
11. `protocols/DISCUSSION.md`
12. `protocols/FRESH_CONTEXT.md`
13. `specifications/KNOWLEDGE_ARCHITECTURE.md`
14. `outcomes/BOOTSTRAP_ACCEPTANCE.md`
15. `outcomes/b12-r5/README.md`
16. `outcomes/b12-r5/HUMAN_ACCEPTANCE.md`
17. `specifications/SESSION_MODEL.md`
18. `specifications/PROJECT_CONTEXT_MODEL.md`

## Consistency Review

| Revision criterion | Result | Evidence |
|---|---|---|
| Open Questionsを説明できる | Pass | OQ-01、OQ-07、OQ-08を識別した。 |
| 未設計Architecture領域を説明できる | Pass | Roadmapの各領域と未設計範囲を説明した。 |
| 採用済み境界と未採用の詳細を区別できる | Pass | 各領域で採用済み土台、未設計・未採用・非Readyを分離した。 |
| B-12完了とProject全体状態を区別できる | Pass | tOS全体未完成、v0.1未Freeze、Creative Project非Readyを示した。 |
| Task開始契約を維持する | Pass | Assigned Issue、Ready承認、固定版、Input Context、停止条件を示した。 |

## Limitations

WorkerはGitHubから新規cloneし既存checkoutを参照していないと報告したが、逐語のToolログと完全なTool isolationの証拠は取得しておらず、採点も独立Reviewerによるものではない。したがって本結果はRevision後の内容整合確認であり、Project Contextの有効性を証明する厳格な試験やHuman Acceptanceではない。
