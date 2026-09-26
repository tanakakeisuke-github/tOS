# tOS — Project Context

状態：Project Contextのinstance / この導入ProposalとともにHuman Review待ち。これはProject全体の短い地図であり、承認済みのPurpose、Constitution、仕様、Decision、Outcome、担当Issueの正本を再定義しない。

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

## Current Focus and Goals

現在、B-12後の次Taskを自動的に開始できる状態ではない。次の制作・改善Taskは、一つの目的、範囲、入力、受入条件、依存、停止点を具体化し、個別のReady承認を得てから開始する。仕事の状態とHuman Gateは[Work Model](specifications/WORK_MODEL.md)、着手時の照合は[Fresh Context](protocols/FRESH_CONTEXT.md)を参照する。

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
