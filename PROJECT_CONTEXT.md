# tOS — Project Context

状態：Project Contextのinstance / Revision・Human Review待ち。これはProject全体の短い地図であり、承認済みのPurpose、Constitution、仕様、Decision、Outcome、担当Issueの正本を再定義しない。

## Project Summary

tOSは、設計意図・仕様・制作から得た知識を保存し、人間とAIが制作をSessionをまたいで継続できるようにするRepositoryである。詳細な目的・現在の範囲は[Purpose](specifications/PURPOSE.md)を正本とする。

## Purpose

短命なAI Sessionを越えて、目的、意思決定、仕事の受け渡し、検証結果を復元可能にし、作品の制作経験を次の制作と制作環境の改善へつなぐ。対象媒体はGame / Film / Music / Publishing / App等を想定するが、全媒体対応や実装済み機能を意味しない。詳細は[Purpose](specifications/PURPOSE.md)を参照する。

## Background and Big Picture

長い会話だけに判断や経緯を残さず、GitHub上のKnowledgeとTaskを結び、人間とAIの協働を継続することが設計意図である。共通のtOS CoreをStudio Templateで媒体へ具体化し、Projectで作品・製品の目的と制約に適用する将来像を持つ。三層の責務と依存方向は[Core Architecture](specifications/CORE_ARCHITECTURE.md)、将来像は[Future Vision](vision/FUTURE_VISION.md)と[Creation Lifecycle](vision/CREATION_LIFECYCLE.md)を正本とする。

## Current State

- Bootstrap KnowledgeのB-01〜B-12は人間の受入承認済みである。
- B-12はR5のP/M/U全ケース合格を人間が受入れ、Done承認済みである。[Human Acceptance](outcomes/b12-r5/HUMAN_ACCEPTANCE.md)、[PR #26](https://github.com/tanakakeisuke-github/tOS/pull/26)、[Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)を参照する。
- これはBootstrap Knowledgeの受入であり、tOS全体の完成、v0.1 Freeze、実制作TaskのReadyではない。v0.1全体の範囲・完成条件はOQ-01として未決定である。

実施状態の詳細と過去試験の原記録は[Issue Map](bootstrap/ISSUE_MAP.md)および[outcomes](outcomes/BOOTSTRAP_ACCEPTANCE.md)を正本の入口とする。

## Architecture Roadmap — Future Design Areas

以下は、現在のtOSと今後必要になり得る中間層を把握するための**未設計領域の地図**である。採用済みSpecification、実装順、着手承認ではない。

`tOS Core → Studio Template Model → Organization / Cross-role Collaboration → Production Planning → Project Bootstrap → Creative Project → Production`

| 領域 | 現在地と未設計の境界 | 参照先 |
|---|---|---|
| tOS Core | B-01〜B-12でPurpose、原則、Core境界、Knowledge、Small Task、Session等の土台を受入済み。ただしtOS v0.1全体の完成条件は未決定。 | [Purpose](specifications/PURPOSE.md)、[Core Architecture](specifications/CORE_ARCHITECTURE.md)、[Issue Map](bootstrap/ISSUE_MAP.md) |
| Studio Template Model | Coreから媒体固有の制作へ具体化する境界と将来像はある。媒体をまたぐTemplateの基本構造、Role、責任、Workflow、Production Stage、Artifact、Quality Gateは未設計。 | [Core Architecture](specifications/CORE_ARCHITECTURE.md)、[Future Vision](vision/FUTURE_VISION.md) |
| Organization / Cross-role Collaboration | Role / Actor / Agent / Modelの区別は定義済み。複数RoleがDiscussion・Decision・Taskを横断して協働する方法と、統合判断の責任は未設計。 | [Actor Model](specifications/ACTOR_MODEL.md)、[Discussion Protocol](protocols/DISCUSSION.md) |
| Production Planning | Small TaskのTriage、Ready、Review、Doneは定義済み。Creative ProjectをMilestone、Epic、Feature、Small Taskへ分解し、上流計画と実行を結ぶModelは未設計。 | [Work Model](specifications/WORK_MODEL.md)、[Creation Lifecycle](vision/CREATION_LIFECYCLE.md) |
| Project Bootstrap | Core、Studio Template、Project固有の目的・制約から制作の入口を用意する将来構想。入力、生成物、Role、Repository、Knowledge、Milestone、承認、自動化範囲は未設計。 | [Core Architecture](specifications/CORE_ARCHITECTURE.md)、[Future Vision](vision/FUTURE_VISION.md)、[Issue Map OQ-07](bootstrap/ISSUE_MAP.md) |
| Creative Project / Production | 企画から制作、評価、完成、振り返りまでの長期方向はある。媒体別の実行方法・成果物・品質判断は将来のTemplateとProjectが所有し、現在はReadyではない。 | [Creation Lifecycle](vision/CREATION_LIFECYCLE.md) |

この並びは概念上の接続候補であり、確定した依存順ではない。各領域の正本、Task分割、受入条件、設計順は、個別のTriageとHuman Gateで決める。

## Current Focus

現在、B-12後の次Taskを自動的に開始できる状態ではない。次の制作・改善Taskは、一つの目的、範囲、入力、受入条件、依存、停止点を具体化し、個別のReady承認を得てから開始する。仕事の状態とHuman Gateは[Work Model](specifications/WORK_MODEL.md)、着手時の照合は[Fresh Context](protocols/FRESH_CONTEXT.md)を参照する。

## Current Milestone

`N/A` — B-12は完了済みだが、次のProject-wide Milestoneは承認されていない。B-12完了をtOS全体の完成・v0.1 Freeze・Creative Project開始のReadyとして扱わない。

## Scope and Constraints

- このRepositoryはKnowledgeと作業の境界を定める。特定のRuntime、Vendor、Automation、GitHub Project設定、Studio Template、作品制作を、この文書だけで開始または確定しない。
- Global Orientationは短く保つ。詳細規則の正本をここへ複写しない。
- 承認済みの規則と新しいDecisionが矛盾する、入力・版・承認状態が不明、または承認範囲を越える判断が必要な場合は、影響する作業を停止して人間に確認する。

## Key Decisions

- 変わりにくい原則とHuman Gate：[Constitution](CONSTITUTION.md)
- tOS Core / Studio Template / Projectの境界：[Core Architecture](specifications/CORE_ARCHITECTURE.md)
- 正本、優先度、矛盾時の扱い：[Knowledge Architecture](specifications/KNOWLEDGE_ARCHITECTURE.md)
- TaskのReady・Doneと状態：[Work Model](specifications/WORK_MODEL.md)
- Sessionをまたぐ引き継ぎ：[Session Model](specifications/SESSION_MODEL.md)

## Open Questions

- **OQ-01**：tOS v0.1の実際の範囲と完成条件。
- **OQ-07**：Project Bootstrapの入力・生成物・承認・自動化の範囲。
- **OQ-08**：Context CompilerとHuman Viewの実装時期・評価方法。

Architecture Roadmapに示したStudio Template Model、Cross-role Collaboration、Production Planningの正本・設計順・受入条件は未決定であり、まだ承認済みSpecificationやReady Taskではない。

問いの全一覧、影響、判断の入口は[Issue Map](bootstrap/ISSUE_MAP.md)を参照する。ここにない問いも、Taskの開始や受入を妨げる場合は担当IssueまたはReviewで扱う。

## What's Next

次に行う作業は、個別にReady承認された小さなTaskだけである。Project Context / Layered Context Proposalを採用するか、媒体別のextensionをいつ設計するか、Fresh Workerでの有効性をどう測るかは、この地図では決めない。

## Knowledge Map

1. Global Orientation：この文書
2. 目的・原則：[Purpose](specifications/PURPOSE.md) / [Constitution](CONSTITUTION.md)
3. 担当Taskの入口：[START_HERE](START_HERE.md) → 担当Issue → 指定Input Context
4. 正本・版・矛盾の扱い：[Knowledge Architecture](specifications/KNOWLEDGE_ARCHITECTURE.md)
5. Projectの履歴・観察・未決定事項：[History](bootstrap/HISTORY.md) / [Findings](bootstrap/FINDINGS.md) / [Issue Map](bootstrap/ISSUE_MAP.md)
6. 実施結果：[Outcomes](outcomes/BOOTSTRAP_ACCEPTANCE.md)

Project Contextを読むことは、担当TaskのReady承認やInput Contextを代替しない。Taskを開始する前の確認は[START_HERE](START_HERE.md)と担当Issueに従う。
