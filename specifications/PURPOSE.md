# tOS — Purpose

状態：Draft。目的と設計原則は依頼で指定。成功指標は検証方法の提案。

## 目的

tOSは、人間と多様なAIが、知識を失わず、承認された小さな仕事を積み重ね、制作から学び続けるための共通基盤である。Game / Film / Music / Publishing / Appなど、媒体が変わっても共通する知識・仕事・承認・学習を扱う。

個々のSessionの記憶力や特定Actorの継続利用に依存せず、Fresh Workerが正本を参照して「何を、なぜ、どこまで行うか」を説明できる状態を目指す。人間はDirection、トレードオフ、ReadyとDoneの承認に関与し、判断根拠を残す。

## 解決したい問題と設計意図

| 問題・懸念 | 設計上の応答 | 評価すべき点 |
|---|---|---|
| 長い会話で古い前提や探索案が混ざる | Fresh Contextと永続Knowledge | 誤った前提の混入、情報欠落、再説明の負担 |
| 新しいWorkerに設計理由が伝わらない | Taskごとの参照とContext Package | 根拠を伴う理解、未決定の識別 |
| 探索中に実装範囲が膨らむ | Discussion / Task分離とTriage | 範囲外実行、独立成果の混在 |
| 組織・技術が変わるたびに知識を失う | Role分離と交換可能なExecution | 同じ仕様・承認を維持した引継ぎ |
| 新技術導入が制作を中断する | Radar、Version、Freeze | 制作の安定性と改善の検証可能性 |

これらは設計上の応答であり、効果が実証済みという意味ではない。[Findings](../research/FINDINGS.md)に観察と仮説を分けて残す。

## 成功の捉え方（提案）

Fresh WorkerがRepositoryだけから目的・境界・判断理由・未決定事項を説明できることを最初の検証対象とする。将来の運用では、成果の品質、修正回数、人間の介入時間、費用、引継ぎ時の欠落、停止すべき場面で止まれるかを評価する。数値閾値や最初の制作対象は未決定。

「最新であること」を完成条件にせず、承認した目的に十分なbaselineを定義してFreezeする。OSを育てる作業とCreative Projectの制作は別々に範囲を管理する。

今回の受入対象はKnowledge Bootstrapのみ。[Core Architecture](CORE_ARCHITECTURE.md)は設計の境界を、[Acceptance](../bootstrap/ACCEPTANCE.md)は文書検証と将来のFresh Workerテスト案を扱う。
