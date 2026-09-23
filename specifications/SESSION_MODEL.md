# tOS — Session Model

状態：Draft。Fresh ContextとDiscussion / Task分離は指定原則。Session記録と更新条件は提案。

## Sessionの役割

Sessionは、ある目的・Context・担当Actorで対話または作業する期間。Knowledgeの恒久的な所有者ではない。ChatGPTでのDiscussion / Planning / Directionも、Cloud AIやLocal AIの作業も、成果と理由を正本へ渡すことで継続できる。

Discussion Sessionでは選択肢と未決定事項を扱う。Task Sessionでは一つの承認済みTaskを扱う。一つのTaskが中断・引継ぎにより複数Sessionへまたがることは許容するが、各Sessionで同じ適用版と承認範囲を確認する。複数Taskを一つの長期Sessionへ無制限に積み上げない。

Review / Research / Incident等を独立したSession種別にするかは将来の設計事項。現段階では新しい分類体系やRegistryを実装しない。

## 開始・更新・終了（提案）

開始時はSessionの目的、関連Task / Discussion、Actor、Required Context、適用版、承認状態を確認する。作業前に理解・不足・停止条件を短く説明する。

目的変更、Contextの混在、根拠不明の判断、何度も同じ修正を繰り返す、担当Actor変更、参照版変更はFresh Sessionへの切替候補となる。固定のメッセージ数やtoken閾値は未決定。切替前に正本候補と未完了状態を整理する。

終了時には成果の所在、行った検証と未実施検証、判断理由、未決定事項、承認待ち、次に許可された行動を[Handoff](../protocols/HANDOFF.md)として残す。引継ぎを作っただけでは次のTaskは発生しない。

## Session Registry構想

SessionとTask / Artifact / Outcomeの対応を追跡する薄い索引を将来検討できる。記録候補は目的、担当、開始・終了、参照版、成果の所在、次の状態。恒久的なチャット人格を業務責任の前提にしない。

Registryの保存先、schema、自動収集、Transcript保存方法は未決定。Transcriptは任意の履歴資料であり、Fresh Workerの必読にはしない。必要Contextの選別については[Knowledge Architecture](KNOWLEDGE_ARCHITECTURE.md)を参照する。
