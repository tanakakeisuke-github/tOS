# tOS

人間とAIが協働するAI-native制作OSの、設計思想と未来像を保存するRepository。

**状態：Knowledge保存とBootstrap Knowledge v0.1 Issue MapのDraft。Human Review待ち。**
現時点の成果は設計意図の記録と作業分解案です。tOS v0.1の完成・稼働・Freezeや、後続TaskのReadyを意味しません。

## 知りたいことから読む

| 問い | 保存先 |
|---|---|
| なぜ作るのか、将来どこへ向かうのか | [Future Vision](vision/FUTURE_VISION.md) |
| 設計から制作・完成・学習までどう流れるのか | [Creation Lifecycle](vision/CREATION_LIFECYCLE.md) |
| 人間とAIはどう仕事を進めるのか | [Operating Model](vision/OPERATING_MODEL.md) |
| 新技術をどう評価・採用し、OSを進化させるのか | [Evolution Model](vision/EVOLUTION_MODEL.md) |
| なぜこの設計へ至ったのか | [History](bootstrap/HISTORY.md) — 理由を調査するときに読む |
| 何が観察され、何がまだ仮説か | [Findings](bootstrap/FINDINGS.md) |
| 次に何を作るべきか、何が未決定か | [Issue Map](bootstrap/ISSUE_MAP.md) |
| 今回どこまで確認したか | [Self Review](bootstrap/SELF_REVIEW.md) |

全読は前提にしません。Fresh Worker用の入口と読み順はIssue MapのB-01/B-04で設計する予定です。

## 記録の位置づけ

- **依頼で指定された方針**：今回の依頼で明示された設計意図。vision文書に保存します。文書化の正確さはHuman Review待ちです。
- **将来構想**：到達したい状態。実装済み機能やv0.1の必須範囲とは区別します。
- **Finding / Hypothesis**：観察された経験・懸念と、検証を要する説明や改善案。
- **Proposal**：今回作成したIssueの切り方、成果物パス、検証方法などの提案。
- **Open Question**：未決定事項。承認や具体的仕様の代用として扱いません。

visionは設計意図の保存先、将来のspecificationsは承認された実行上の契約の保存先です。後続Issueで仕様化するときは、該当vision節を意図の説明と仕様参照へ整理し、同じ運用規則を二か所で管理しない案とします。

## 出典と確認範囲

1. 2026-09-24の本作業依頼：名称、保存内容、Issue Map要件、作業範囲を定める直接の入力。
2. [参照Discussion「[HQ][DISC] Studio Architecture 001」](https://chatgpt.com/c/6aa96c7c-da58-83ee-be94-c118cf99c5cb)：直近10ターンを確認。制作フロー、Small Issueへの切替、GitHubによるKnowledge保存、引き継ぎへの不安を照合しました。

参照Discussionの全履歴・添付画像・外部Notionは今回未確認です。会話へのアクセス権に依存せず概要を復元できるよう、必要な意味を各文書に保存しました。旧会話の提案を自動的に採用済み仕様へ昇格させず、本作業依頼を優先しています。履歴の順序は設計意図の整理であり、未確認の日時・実験結果は補っていません。

## 今回の停止点

KnowledgeとIssue MapをDraft PRとして提示し、Human Reviewを待ちます。次の判断は分解案・未決定事項を確認し、B-01を個別にReadyにできるかです。Issue登録、GitHub Project、Agent設定、Automation、本体実装は後続の承認対象です。
