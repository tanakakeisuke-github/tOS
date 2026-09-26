# tOS

設計意図・仕様・制作から得た知識を保存するRepository。

**状態：Knowledge保存・Issue Map・B-01〜B-12はHuman Review承認済み。B-12はR5の全ケース合格を人間が受入れ、完了承認済みです。** [受入記録](outcomes/b12-r5/HUMAN_ACCEPTANCE.md)を参照してください。
tOS v0.1全体の範囲・完成条件は未確定（OQ-01）です。完成・稼働・Freezeや、後続TaskのReadyを意味しません。

新しく参加する場合は[START_HERE](START_HERE.md)から、目的の確認は[Purpose](specifications/PURPOSE.md)から読んでください。B-12 / [Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)は完了済みです。後続Taskは個別のReady承認を必要とします。

## 知りたいことから読む

| 問い | 保存先 |
|---|---|
| なぜ作るのか、何を引き継ぐのか | [Purpose](specifications/PURPOSE.md) — B-01で承認済み |
| 変わりにくい判断原則は何か | [Constitution](CONSTITUTION.md) — B-02で承認済み |
| 担当作業をどこから始めるか | [Start Here](START_HERE.md) |
| Project全体の目的・背景・現在地・次の論点を短時間で把握したい | [Project Context](PROJECT_CONTEXT.md) — 地図。Purpose・Constitution・Task入力の代用ではない |
| 媒体を問わずProject Contextをどう構成するか | [Project Context Model](specifications/PROJECT_CONTEXT_MODEL.md) — Proposal / Human Review待ち |
| tOS / Studio Template / Projectの境界は何か | [Core Architecture](specifications/CORE_ARCHITECTURE.md) — B-03で承認済み |
| 正式な知識はどこに置き、どう読むのか | [Knowledge Architecture](specifications/KNOWLEDGE_ARCHITECTURE.md) — B-04で承認済み |
| 検討をどうTaskへ分け、いつ着手・完了するか | [Work Model](specifications/WORK_MODEL.md) — B-05で承認済み |
| 短いAI Sessionをまたいで仕事をどう引き継ぐか | [Session Model](specifications/SESSION_MODEL.md) — B-06で承認済み |
| Roleと担当主体・AI実行構成をどう分けるか | [Actor Model](specifications/ACTOR_MODEL.md) — B-07で承認済み |
| 検討からTask案と着手判断へどう渡すか | [Discussion](protocols/DISCUSSION.md)・[Task](protocols/TASK.md)・[Triage](protocols/TRIAGE.md) — B-08で承認済み |
| 短いAI作業の開始・引き継ぎ・Reviewをどう進めるか | [Fresh Context](protocols/FRESH_CONTEXT.md)・[Handoff](protocols/HANDOFF.md)・[Review](protocols/REVIEW.md) — B-09で承認済み |
| 新技術をどう評価し、版を固定・移行・撤回するか | [Technology Evolution](specifications/TECHNOLOGY_EVOLUTION.md)・[Technology Radar](research/TECHNOLOGY_RADAR.md) — B-10で承認済み |
| 文書を横断して何を確認し、Fresh Workerをどう試すか | [Integration Review](bootstrap/INTEGRATION_REVIEW.md)・[Acceptance Plan](bootstrap/ACCEPTANCE_PLAN.md) — B-11で承認済み |
| Fresh WorkerがKnowledgeを引き継げたか | [Bootstrap Acceptance](outcomes/BOOTSTRAP_ACCEPTANCE.md) — 過去系列を保存。R5の全ケース合格は人間に受入れられ、B-12は完了 |
| 将来どこへ向かうのか | [Future Vision](vision/FUTURE_VISION.md) |
| 設計から制作・完成・学習までどう流れるのか | [Creation Lifecycle](vision/CREATION_LIFECYCLE.md) |
| 人間とAIはどう仕事を進めるのか | [Operating Model](vision/OPERATING_MODEL.md) |
| 新技術をどう評価・採用し、OSを進化させるのか | [Evolution Model](vision/EVOLUTION_MODEL.md) |
| なぜこの設計へ至ったのか | [History](bootstrap/HISTORY.md) — 理由を調査するときに読む |
| 何が観察され、何がまだ仮説か | [Findings](bootstrap/FINDINGS.md) |
| 次に何を作るべきか、何が未決定か | [Issue Map](bootstrap/ISSUE_MAP.md) |
| 初回のKnowledge保存でどこまで確認したか | [Self Review](bootstrap/SELF_REVIEW.md) — PR #2提出時の記録 |

全読は前提にしません。PurposeとConstitution、担当Issueを確認した後は、そのIssueで指定された入力を読みます。

## 記録の位置づけ

- **依頼で指定された方針**：Knowledge保存時の依頼で明示された設計意図。vision文書への保存はHuman Review承認済みです。
- **将来構想**：到達したい状態。実装済み機能やv0.1の必須範囲とは区別します。
- **Finding / Hypothesis**：観察された経験・懸念と、検証を要する説明や改善案。
- **Proposal**：今回作成したIssueの切り方、成果物パス、検証方法などの提案。
- **Open Question**：未決定事項。承認や具体的仕様の代用として扱いません。

visionは設計意図、specificationsは仕様、protocolsは手順を扱います。仕様・手順の案は人間の承認を経て実行上の契約となります。B-01〜B-12の各成果は承認済みです。B-12のR5 Fresh Worker試験は人間に受入れられ完了しましたが、試験の採点をtOS全体の完成やFreezeとして扱いません。具体化する内容はvisionから所有する仕様・手順へ参照をつなぎ、同じ運用規則を二か所で管理しない方針です。

## 出典と確認範囲

以下は初回のKnowledge保存（PR #2）で確認した範囲です。B-01〜B-11の入力と確認結果は各担当Issueと提出PRを参照してください。B-12の入力と承認状態は[Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)を参照してください。

1. 2026-09-24の本作業依頼：名称、保存内容、Issue Map要件、作業範囲を定める直接の入力。
2. [参照Discussion「[HQ][DISC] Studio Architecture 001」](https://chatgpt.com/c/6aa96c7c-da58-83ee-be94-c118cf99c5cb)：直近10ターンを確認。制作フロー、Small Issueへの切替、GitHubによるKnowledge保存、引き継ぎへの不安を照合しました。

参照Discussionの全履歴・添付画像・外部Notionは今回未確認です。会話へのアクセス権に依存せず概要を復元できるよう、必要な意味を各文書に保存しました。旧会話の提案を自動的に採用済み仕様へ昇格させず、本作業依頼を優先しています。履歴の順序は設計意図の整理であり、未確認の日時・実験結果は補っていません。

## 現在地と次の着手

B-12はR5の結果を人間が受入れ、PR #26のマージとIssue #25のクローズを承認済みです。これはBootstrap Knowledgeの一連の受入であり、tOS全体の完成・v0.1 Freeze・実制作TaskのReadyを意味しません。次の制作・改善Taskは、目的・範囲・入力・受入条件・依存・停止点を具体化し、個別のReady承認を経て開始します。Project全体の短い位置づけは[Project Context](PROJECT_CONTEXT.md)を参照します。
