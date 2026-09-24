# tOS

設計意図・仕様・制作から得た知識を保存するRepository。

**状態：Knowledge保存・Issue Map・B-01はHuman Review承認済み。B-02は着手承認済みで、Constitutionの成果物はHuman Review待ちです。**
tOS v0.1全体の範囲・完成条件は未確定（OQ-01）です。完成・稼働・Freezeや、後続TaskのReadyを意味しません。

新しく参加する場合は[START_HERE](START_HERE.md)から、目的の確認は[Purpose](specifications/PURPOSE.md)から読んでください。現在の担当Issueは[B-02 / #5](https://github.com/tanakakeisuke-github/tOS/issues/5)です。

## 知りたいことから読む

| 問い | 保存先 |
|---|---|
| なぜ作るのか、何を引き継ぐのか | [Purpose](specifications/PURPOSE.md) — B-01で承認済み |
| 変わりにくい判断原則は何か | [Constitution](CONSTITUTION.md) — B-02案、Human Review待ち |
| 担当作業をどこから始めるか | [Start Here](START_HERE.md) |
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

visionは設計意図、specificationsは仕様を扱います。仕様案は人間の承認を経て実行上の契約となります。B-01のPurposeは承認済みです。B-02のConstitutionはHuman Review待ちの原則案です。Knowledge保存の承認を、仮説の実証や全仕様の承認として扱いません。仕様化する内容はvisionから仕様へ参照をつなぎ、同じ運用規則を二か所で管理しない方針です。

## 出典と確認範囲

以下は初回のKnowledge保存（PR #2）で確認した範囲です。B-01・B-02の入力と確認結果は各担当Issueと提出PRを参照してください。

1. 2026-09-24の本作業依頼：名称、保存内容、Issue Map要件、作業範囲を定める直接の入力。
2. [参照Discussion「[HQ][DISC] Studio Architecture 001」](https://chatgpt.com/c/6aa96c7c-da58-83ee-be94-c118cf99c5cb)：直近10ターンを確認。制作フロー、Small Issueへの切替、GitHubによるKnowledge保存、引き継ぎへの不安を照合しました。

参照Discussionの全履歴・添付画像・外部Notionは今回未確認です。会話へのアクセス権に依存せず概要を復元できるよう、必要な意味を各文書に保存しました。旧会話の提案を自動的に採用済み仕様へ昇格させず、本作業依頼を優先しています。履歴の順序は設計意図の整理であり、未確認の日時・実験結果は補っていません。

## 今回の停止点

B-02のConstitutionと入口の更新をDraft PRとして提示し、Human Reviewを待ちます。次の判断は、原則と人間が判断する境界を受け入れられるかです。B-03以降は個別の着手判断に従います。
