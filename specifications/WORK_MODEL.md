# tOS — Work Model

状態：Draft。Discussion / Task分離、small objective、Triage、Human Gateは指定原則。状態遷移と記録項目は運用提案。

## 仕事の単位

Discussionは問題・選択肢・理由を探索する単位。Taskは承認された一つの小さな目的に対してArtifactと検証結果を作る単位。Sessionはそれらを扱う対話・実行の期間であり、仕事そのものとは区別する。

Issueは将来Taskを記録する器の候補である。Taskという概念とGitHub上の物理的なIssueを混同しない。GitHub Projectsのボード、状態名、field、Issue種別、採番規則は未決定。

「small」は固定した行数や時間を意味しない。一つの受入判断で目的達成を判定でき、担当・変更範囲・停止条件が明確な大きさを目指す。関連ファイルが複数あっても一つの成果なら同じTaskにできる。別々に承認・出荷できる目的が生じたらSPLITを検討する。

## Task契約（提案）

目的と背景、対象、範囲、期待Artifact、Acceptance Criteria、Required Contextと適用版、依存関係、Worker / Reviewer、実行権限、予算・時間等の制約、停止条件、Human Approvalの証跡を明示する。

担当未決定・受入条件不足・参照切れはReadyへ進める前に解消する。実行中に重要な前提が変わったら、元の承認を新しい範囲へ拡張解釈せず再評価する。

## 論理的な流れ（提案）

Discovery / Discussion → Triage → Task Draft → **Human Approval** → Ready → Work → Review → **Human Approval** → Done。

これはGitHub設定を作成する指示ではない。ReadyとDoneの意味、および二つのHuman Gateが原則であり、中間状態名や実装方式は未決定。

- Ready前：目的・範囲・受入条件・実行許可を人間が承認する。
- Review：Artifact、差分、検証証跡、未解決点を提示する。可能ならWorkerとReviewerを分ける。
- Done前：人間が対象版の成果と受入結果を承認する。テスト成功やPRの存在だけではDoneにしない。

レビュー差戻しは同じ目的の範囲内なら修正する。目的・権限・受入条件が変わるなら再承認へ戻す。Blocked、取消、再開の細かな状態設計は未決定だが、停止理由と再開条件は記録する。

## 新しい発見

承認範囲内の判断はTaskを進めるために行う。別目的の改善・新機能・未知の依存作業は[PROPOSE / Triage](../protocols/TRIAGE.md)へ送る。必要性を説明したことは、新規Issue作成や実行の承認にはならない。

ArtifactとOutcomeを残してSessionを終えても、TaskがDoneになったとは限らない。継続時は同じ契約を[Fresh Context](../protocols/FRESH_CONTEXT.md)で読み直す。
