# tOS

人間・Cloud AI・Local AIが、Game / Film / Music / Publishing / Appなどの制作を長期的に協働するための共通基盤。tOSは制作の目的、知識、仕事の境界、承認、学習を扱います。

**Knowledge Bootstrap — Draft / Human Review待ち（2026-09-24）。** このRepositoryにあるのは設計Knowledgeです。OSのリリース、運用開始、実装完了を表しません。入口は[START_HERE](START_HERE.md)です。

## このDraftの扱い

- **原則（依頼で指定）**：今回の依頼に明示された設計方針。本Draftはその文書化であり、新しい実装承認ではありません。
- **構想（依頼で指定）**：残すべき設計意図。機能の存在・採用・稼働は未確認です。
- **提案**：理解をつなぐために本Draftで具体化した手順・記録項目・検証方法。Human Review対象です。
- **未決定**：選択・範囲・運用責任・方式がまだ定まっていない項目。
- **観察 / 仮説**：元の議論での報告と、その説明や改善予想。検証結果と区別します。

文書全体はDraftです。原則を記述したことと、この文章が承認されたことは別です。承認後も「提案」「未決定」は個別に決着するまでその状態を保持します。文書の存在、merge、TaskのDone、OSリリースはそれぞれ別の判断です。

## 文書案内

| 関心 | 文書 |
|---|---|
| 最小の入口と原則 | [START_HERE](START_HERE.md) / [CONSTITUTION](CONSTITUTION.md) |
| 目的と構造 | [Purpose](specifications/PURPOSE.md) / [Core Architecture](specifications/CORE_ARCHITECTURE.md) |
| 永続知識とContext Compiler | [Knowledge Architecture](specifications/KNOWLEDGE_ARCHITECTURE.md) |
| 仕事・Session・担当 | [Work Model](specifications/WORK_MODEL.md) / [Session Model](specifications/SESSION_MODEL.md) / [Actor Model](specifications/ACTOR_MODEL.md) |
| 技術更新とVersion | [Technology Evolution](specifications/TECHNOLOGY_EVOLUTION.md) |
| 探索・実行・新規発見 | [Discussion](protocols/DISCUSSION.md) / [Task](protocols/TASK.md) / [Triage](protocols/TRIAGE.md) |
| 引継ぎ・評価・Context | [Handoff](protocols/HANDOFF.md) / [Review](protocols/REVIEW.md) / [Fresh Context](protocols/FRESH_CONTEXT.md) |
| Decisionと結果の残し方 | [Decisions](decisions/README.md) / [Outcomes](outcomes/README.md) |
| 観察と技術候補 | [Findings](research/FINDINGS.md) / [Technology Radar](research/TECHNOLOGY_RADAR.md) |
| 経緯と不確実性 | [History](bootstrap/HISTORY.md) / [Assumptions](bootstrap/ASSUMPTIONS.md) / [Open Questions](bootstrap/OPEN_QUESTIONS.md) |
| 出典・検証 | [Sources](bootstrap/SOURCES.md) / [Acceptance](bootstrap/ACCEPTANCE.md) / [Self Review](bootstrap/SELF_REVIEW.md) |

推奨構造に、知識の格納先を説明する`decisions/`・`outcomes/`と、出典・受入検証・自己レビュー文書を加えています。確定Decisionや実行Outcomeはまだ登録していません。各文書は関連部分だけ参照できる単位です。

## 今回の成果物の境界

KnowledgeをDraft PRとして提出し、Human Reviewで停止します。Issue、GitHub Projects、Agent設定、Automation、実装コードは本成果物に含めません。後続の実装、運用設定、Fresh Workerによる受入実行には別の承認範囲が必要です。

GitHubを将来のSource of Truth / Project Memory / Work Managementの中心とします。正式な採用状態は承認証跡と適用版から判断します。Discussionの会話や外部Human Viewは、その代わりになりません。
