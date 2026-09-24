# tOS — Evolution Model

状態：依頼で指定された進化方針と将来構想の保存。運用上の判断条件はB-10の仕様案でHuman Review待ち。

## 基本姿勢

**Discover continuously, adopt deliberately.**

新しい技術は継続的に調べ、採用は目的・検証結果・制作への影響を踏まえて判断します。

## Technology Radarと版の区分

Technology Radarの状態 **WATCH / TRIAL / ADOPT / HOLD** と、変更を扱う区分 **Current / Next / Lab** を分ける設計意図です。運用上の意味と適用の条件は[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md#二つの独立した軸)で扱います（B-10仕様案、Human Review待ち）。候補の記録構造は[Technology Radar](../research/TECHNOLOGY_RADAR.md)に置きます（同じくB-10案）。現時点のtOS Current版やFreeze日は未設定です。

## 評価から採用へ

`Discover → Triage → Evaluate → Benchmark/PoC → Human Approval → Next Version → Measure → Keep/Rollback` の循環を目指します。各段階で必要な証拠と人間の判断は[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md#探索から継続撤回まで)で扱います（B-10仕様案、Human Review待ち）。

## Technology候補の履歴

Herdr / Orca / Factory / Cursor / GitHub Agents / Local AI等は、Discussionで挙がったTechnology候補です。候補名はここに集約し、Coreの必須構成要素へ結び付けません。各候補の能力・提供状況・性能・採用状態は今回調査しておらず、比較評価の結果もありません。

Local AIはActorの分類としても扱います。個別のLocal AIのModel・Runtime等の選定は、同じ評価過程を経る対象です。

## Version FreezeとRebuild

Version Freezeは、制作を開始できると人間が判断した範囲・版・既知の制限を固定し、Projectで使う基準を安定させる考え方です。Freeze、Currentの例外、Project移行・Rollbackの判断条件は[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md#freezeと変更の境界)に具体化しました（B-10仕様案、Human Review待ち）。

Implementationの再構築も選択肢に含めます。[Future Vision](FUTURE_VISION.md)に記録した保持対象を引き継ぐ設計意図です。比較・移行・Human Approvalの判断条件は[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md#implementationを再構築する場合)で扱います（B-10仕様案、Human Review待ち）。
