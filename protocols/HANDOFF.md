# Handoff Protocol — 成果と残課題を次の担当へ渡す

状態：B-09としてHuman Review承認済み（[PR #20](https://github.com/tanakakeisuke-github/tOS/pull/20)）。本手順は[Session Model](../specifications/SESSION_MODEL.md)の終了・中断時の情報を成果と結ぶ。記録の正本と状態は[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md)を参照する。

## 入力

担当IssueとReady承認、適用版、受入条件、指定入力、作業中または提出する成果、実際の確認結果、中断・失敗・判断・Unknownの記録。

## 担当・手順

作業を終える、または中断するWorkerが記録し、次のWorkerまたはReviewerが受け取る。担当変更の判断は[Actor Model](../specifications/ACTOR_MODEL.md#割当と交代)に従う。

1. TaskとReady承認の所在、基準版・実際に使った入力、成果物の所在と版、変更点を結ぶ。Draft PRまたは成果提出をReviewへの入口とし、提出した事実を完了の証拠にしない。
2. 受入条件ごとに、実施した検証の方法・条件・結果・証拠と、**未実施の検証**を区別する。自己確認の範囲、未確認の理由、結果への影響も示す。未実施を合格や失敗に読み替えない。
3. 残作業、既知の問題、失敗と原因仮説、判断と理由、Unknownを記録する。Unknownには問い、影響範囲、判断者、関連する版・出典、次の判断点を付ける。判断・承認の正本は担当IssueまたはReviewの一方に指定し、他方から参照する。
4. 中断・差戻しなら停止理由、止めた範囲、必要な判断者、解消と再開の条件を示す。次の担当は[Fresh Context Protocol](FRESH_CONTEXT.md)に従い、引き継ぎ内容を現行の入力・承認に照合してから続ける。

## 出力

担当IssueまたはReviewから辿れる引き継ぎ記録。次の担当が「何を受け取り、何が実施済みで、何が未実施・未解決か」を受入条件と版に照らして確認できる状態とする。成果の実測結果と提案・仮説を分ける。

## 停止条件

成果版、受入条件への対応、実施／未実施の検証、重要な残課題が不明なら、完了扱いや無条件のReview依頼をしない。不足を明記して補完または人間の判断へ渡す。承認範囲外の変更や入力矛盾があれば影響する作業を止め、必要に応じてReady前Human Gateへ戻す。
