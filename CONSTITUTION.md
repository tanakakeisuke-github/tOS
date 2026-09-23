# tOS — Constitution

状態：Draft。以下は今回の依頼で指定された原則の文書化です。詳細な運用方式は提案または未決定であり、この文書は実装を許可しません。

## 原則

1. **GitHub is the Source of Truth.** 将来の正本・Project Memory・Work ManagementをGitHub中心に構成する。承認済みSpecification、Decision、Outcomeと、その適用版・来歴を残す。ChatGPTはDiscussion / Planning / Directionを担う。正本化はレビューと承認を経る。
2. **Chat is disposable. Knowledge is permanent.** Sessionを交換しても、判断理由・要求・成果・学びを再利用できる状態にする。Transcriptの保存と、Fresh Contextへの投入は別の判断である。
3. **Discussion and Task are separate.** 探索・選択肢の比較と、承認済み成果の作成を別の単位にする。Discussionの提案はTaskの実行許可にならない。
4. **One Task = one small objective.** 一つの目的と判定可能な受入条件を持つ。独立した成果や承認が増える場合は分割を提案する。
5. **Fresh Context by default.** 永続知識から必要なContextを構成する。長寿命Sessionや暗黙の会話記憶に継続性を委ねない。
6. **AI may propose work, but Triage controls work creation.** 承認範囲外の発見は提案としてTriageへ。AIは新規Taskを勝手に作成・実行・Ready化しない。
7. **Human approval before Ready and Done.** 人間が目的・範囲・受入条件を承認してからReadyへ進める。結果と検証証跡を人間が承認してからDoneへ進める。AIレビューはHuman Approvalの代替にならない。
8. **Role / Actor / Agent / Model are independent.** 責任、担当主体、実行の仕組み、推論モデルを分ける。Human / Cloud AI / Local AIは共通の仕事契約を扱うActorとし、権限と適性は個別に確認する。Human Gateは人間に留保する。
9. **Organization is configurable. Knowledge is organization-independent.** 部門や役割が変わってもKnowledgeの意味・参照・履歴は保つ。知識の分類を現在の担当者や組織図へ固定しない。
10. **OS changes are versioned.** Projectが採用したOS Versionは原則Freezeする。改善は検証と承認を経て次版へ入り、既存Projectへの移行は別途判断する。
11. **Discover continuously, adopt deliberately.** 技術発見は継続する。WATCH / TRIAL / ADOPT / HOLDとCurrent / Next / Labを使い、発見と採用を区別する。
12. **Infrastructure is replaceable.** Runtime / Orchestrator / Vendorを交換可能な下位レイヤーとして扱う。上位のKnowledge・承認・仕事の意味を維持する。
13. **Do not inherit legacy structure without re-evaluation.** Greenfieldとして目的・原則・要求から構造を設計する。過去のRepository / Project / Issue構造を推測して再現しない。
14. **Prefer rebuildable systems over irreversible complexity.** 実装は将来再構築できる形にする。Principles / Requirements / Specifications / Decisions / Learnings / Failures / Benchmarks / Project Historyを継承資産として残す。

## 適用と変更

不明点・矛盾・権限不足ではSTOP、複数目的ではSPLIT、改善や新規作業はPROPOSEを使う。詳細は[Task Protocol](protocols/TASK.md)。WorkerとReviewerは可能なら分離し、同じ担当による自己レビューは明記する。

原則の変更も、理由・影響・代替案・適用版を示してHuman Reviewを受ける。下位の実装やTaskが原則を暗黙に変更することはできない。具体的な変更承認者とVersion付番は[未決定](bootstrap/OPEN_QUESTIONS.md)である。
