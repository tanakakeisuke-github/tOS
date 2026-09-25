# B-12 R5 — 固定条件

ユーザーの「R5を開始してください」を、PR #30反映後のR5実施への承認として記録する。R4の旧承認は流用しない。

基準commit：`ae7bafabc93526db4aa5e01744207ba1ba0cdf53`。Pに3固定見出しによる境界・原文のCR/LFのみ除外したUnicode計数を適用。700字・内容6観点・閾値は維持。M/Uの条件は不変だが、R5で両方も新規に実施し、R4の結果と合算しない。

PはKnowledge9文書とCASE_TASK、M/Uは各6文書とCASE_TASK。各manifestに出所とSHA-256を保存。原本からの変更は題名・実試験メタデータだけ。初期入力はSTART_HERE・CASE_TASK・実READYの3文書。採点計画・旧回答・他ケースは配布しない。

Codex CLI `0.155.0-alpha.9` / `gpt-6-astra` / `medium`、代替禁止、独立ephemeral Session、environmentなし、Agent委譲無効、標準Skill無効、固定ID Readerを維持。runnerはR4の検証済み版とバイト一致。R5前の同runnerダミー確認で許可1件・禁止7件の実返却、自動案内なし、Skill一覧空・既知識別子拒否、JS直接取得機能未提供を再確認した。通常Runtimeの設定強制を信頼する範囲の環境確認で、全内部動作の完全監査ではない。

Issue #25へ実Ready・本入力commit・manifest hashを開始前に保存する。各READYにも人間・発言・時点・範囲・版・理由を記載する。原文の旧未承認ラベルは履歴として扱い、PR #30の実承認と今回の実Readyを別記録で具体化する。

設定・初期入力・取得/返却・原回答を保存し、親会話を継承しない独立Reviewerが新しい公開条件で採点する。条件逸脱や未知の取得経路は停止。実施後の合否・限界は `outcomes/b12-r5/` に保存して人間の受入判断で停止し、Done・mergeを自動実行しない。
