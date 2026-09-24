# Triage Protocol — Task案の行き先を決める

状態：B-08提案。Human Review・Done承認前。Triageの位置と状態遷移は[Work Model](../specifications/WORK_MODEL.md#triage状態human-gate)を参照する。

## 入力

[Discussion Protocol](DISCUSSION.md)の問い・選択肢と[Task Protocol](TASK.md)のTask案、出所・適用版・承認状態、依存と未知、必要な人間の判断。制作中のOS改善提案では現行Taskへの影響と検証案も受け取る。

## 担当・手順

Triage担当Actorが判断材料と振分け案を整え、人間が採否とReadyを判断する。ActorとHuman Gateの境界は[Actor Model](../specifications/ACTOR_MODEL.md)と[Constitution](../CONSTITUTION.md#変わりにくい原則)に従う。

1. 問いから選択肢、選んだTask案までの参照を照合し、目的が一つか、入力・受入条件・依存・停止点が揃うかを確認する。欠けるか競合する場合は**STOP**し、必要な情報、判断者、再開条件を記録する。複数目的なら**SPLIT**案と順序・依存を示す。
2. 各案について「Task化してReady待ち」「Discussionへ戻して追加検討」「将来版で評価」「却下」の振分けを人間に提示する。理由、影響、未決定事項、次の判断点を残す。Task化はReady承認ではない。
3. 現行の制作Taskから見つかったOS改善は**PROPOSE**として別案にし、現行Taskの承認範囲へ加えない。影響を受ける範囲を示し、[Evolution Model](../vision/EVOLUTION_MODEL.md#technology-radarと版の区分)の **Current / Next / Lab** を振分け先の候補として提示する。Currentへの適用、Nextでの検討、Labでの限定評価のどれを選ぶかは人間の判断に残す。候補の発見や分類、評価案だけでCurrentの版・進行中の制作条件は変わらない。
4. Task化を選ぶ場合は担当Issueへ条件・版・出所・Triage結果を引き継ぎ、Ready待ちに置く。人間が対象Taskと適用版を指定して着手を承認した記録を確認してからReadyにする。AI ReviewやIssue作成を承認と読み替えない。

## 出力

案ごとの振分け、理由、担当判断者、出所と状態への参照、分割時の依存、停止時の再開条件、およびReady前Human Gateへ渡すTask条件。判断と理由の正本・承認状態は[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md#正本と分類)に従う。

## 停止条件

出所・適用版・承認状態や所有先が不明、仕様と案が競合、または制作中の変更が既承認範囲を越えるなら影響する判断を止める。人間の振分け判断がない場合はTask化・Current適用を確定しない。B-10が扱う採用・Freeze・例外・Rollbackの規則はこの入口で確定しない。

## 照合例

制作中に「新しい実行方式でOSを改善したい」と提案された場合、現行Taskの成果から改善案を切り離し、根拠・影響・比較方法を付けてTriageへ送る。Labで限定評価する案、Nextで検討する案、Currentへの変更判断が必要な案を人間に示す。人間の判断前には方式を採用済みとせず、現行Taskの範囲も変えない。
