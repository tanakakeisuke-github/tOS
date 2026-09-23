# tOS — Review Protocol

状態：Draft。Worker / Reviewer分離とHuman Approvalは指定原則。チェック観点と返却形式は提案。

## 入力

対象Task、承認された範囲とAcceptance Criteria、適用Specification / Decision、対象Artifactの版、差分、検証証跡、Workerが申告した制約を受け取る。Reviewerは可能ならWorkerと別Actor・別Contextにする。

## 評価

1. 目的と範囲に一致しているか。別目的の仕事を混ぜていないか。
2. 指定原則と適用版の仕様に適合しているか。
3. 受入条件ごとに証拠があるか。未実施検証が明示されているか。
4. 原則、提案、仮定、未決定、観察、実証結果を区別しているか。
5. ArtifactとDecisionの来歴を追えるか。次のWorkerが理解できるか。
6. Knowledgeの場合は、特定作品へのアンカー、否定文が作る不要なアンカー、Vendor固定、未決定の断定、承認の自動昇格がないか。

欠陥は根拠・影響・修正に必要な条件を添える。好みと必須要件を分ける。合格を提案する場合も対象版と検証範囲を明示する。

## 出力とHuman Gate

結論候補は受入推奨、修正要求、証拠不足。残るリスクと未決定事項を含める。AI Reviewerの受入推奨はDone承認ではない。人間が対象版の結果を確認して最終判断する。

自己レビューの場合は独立レビューではないと明記する。別Actorを起動できたことだけでも独立性を保証しない。どのContext・入力で評価したかを記録する。

今回のKnowledge BootstrapはDraft PRで停止する。[Acceptance](../bootstrap/ACCEPTANCE.md)は将来のFresh Worker理解テスト案、[Self Review](../bootstrap/SELF_REVIEW.md)は今回の実際の検査記録である。
