# tOS — Creation Lifecycle

状態：依頼で指定された制作フローの保存。各Phaseの詳細な完了条件は後続設計とHuman Reviewの対象。

## 設計から完成へ

| Phase | すること | 次へ渡すもの・判断 |
|---|---|---|
| 1 — tOSを設計 | Purpose、Principles、最小Architecture、仕事の進め方を整理 | 人間が方向性と範囲を確認 |
| 2 — tOS v0.1を作る | 承認されたSmall IssueごとにKnowledgeと必要な運用基盤を整え、Fresh AIへの引き継ぎを確認 | 制作を開始できる範囲と検証結果を人間が判断しVersion Freeze |
| 3 — Studio Templateを作る | 媒体に合わせた専門Role、成果物、Workflow、品質確認を用意 | 利用するTemplateと版を確認 |
| 4 — Creative Projectを企画 | 体験・目的・制約、Prototype範囲、Milestoneを整理しSmall Issueへ分解 | 人間が制作範囲・優先順位を承認 |
| 5 — 制作する | Small Issue → Fresh Worker → PR → Fresh Reviewer → Human Reviewを繰り返す | 必要な成果物評価を経てDone前Human Gate |
| 6 — 作品を育てる | 評価で見つかった問題をTriageし、改善と再評価を繰り返す | 媒体に応じた完成候補 |
| 7 — Release / Complete | 最終品質確認、作品体験の評価、人間の完成判断 | 公開または定義された納品・完成 |
| 8 — 振り返り | Project RetrospectiveとtOS Retrospectiveを分離 | LearningsをtOS vNextの検討へ戻す |

Phase 2の初回保存（PR #2）の到達点はKnowledge保存とIssue Map案です。表全体は長期の流れです。現在の着手範囲は[Issue Map](../bootstrap/ISSUE_MAP.md)から担当Issueを確認します。Bootstrap Knowledgeの受入と、tOS v0.1全体の完成判断は分けて定義します。

## Game TemplateでのPhase 6の例

`Prototype → Vertical Slice → Alpha → Beta → Release Candidate`

Playtestで作品体験を確かめながら品質と範囲を育てます。この段階名はGame Templateの例です。Film / Music / Publishing / App等では、その媒体に適した段階と評価方法をTemplate側で定義します。

## 制作中のOS改善

制作中に見つかったOS改善案はTriageへ渡し、原則としてNext / Labで評価します。制作で利用しているCurrentは安定させ、改善案と進行中の作品の作業範囲を分けます。Currentの例外変更・人間の承認・Rollbackの判断条件は[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md#freezeと変更の境界)で扱います（B-10仕様案、Human Review待ち）。

進化の設計意図は[Evolution Model](EVOLUTION_MODEL.md)、採用とVersion Freezeの判断条件は[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md)を参照します（B-10仕様案、Human Review待ち）。

## 完成後の二つの振り返り

- **Project Retrospective**：作品の体験、表現、品質、制作範囲、納品結果から学ぶ。
- **tOS Retrospective**：Context受け渡し、Task粒度、Review、Human Gate、Actorの割当など、制作システムから学ぶ。

作品固有の学びをCoreへ移す際は、他の媒体・Projectにも通用するか評価します。観察と仮説を分け、検証後に次版へ取り込む方針です。

## 循環

`tOS → Studio Template → Project → Production → Complete → Learnings → tOS Improvement → tOS vNext → Next Project`

この循環により、作品を完成させた経験を残し、次のProjectでより良い制作環境を使えるようにします。
