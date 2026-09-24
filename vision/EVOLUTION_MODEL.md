# tOS — Evolution Model

状態：依頼で指定された進化方針と将来構想の保存。表の運用上の意味づけは具体化案、採用判断はHuman Review対象。

## 基本姿勢

**Discover continuously, adopt deliberately.**

新しい技術は継続的に調べ、採用は目的・検証結果・制作への影響を踏まえて判断します。

## Technology Radarと版の区分

Technology Radarの状態は **WATCH / TRIAL / ADOPT / HOLD** を使う方針です。

| 状態 | 意味づけ案 |
|---|---|
| WATCH | 情報収集し、用途と不明点を記録する |
| TRIAL | 限定したBenchmark / PoCで評価する |
| ADOPT | 人間が採用を認めた用途・条件・対象版を記録する |
| HOLD | 利用・採用を保留し、理由と再評価条件を記録する |

**Current / Next / Lab** は変更を扱う区分です。

| 区分 | 意味づけ案 |
|---|---|
| Current | 制作に利用する承認済みの版 |
| Next | 次版へ向けて検討・統合する変更 |
| Lab | 限定した実験と検証 |

Radarの採用状態とCurrentの適用版は別の情報です。TRIALやADOPTの記録だけで、進行中Projectの環境が変わることはありません。現時点のtOS Current版やFreeze日は未設定です。

## 評価から採用へ

`Discover → Triage → Evaluate → Benchmark/PoC → Human Approval → Next Version → Measure → Keep/Rollback`

評価では、何を改善したいか、比較対象、期待する結果、実測結果、失敗、移行影響を残す案とします。導入後の測定によって継続・撤回を判断し、その理由もKnowledgeへ戻します。数値基準やRollbackの具体手順は後続設計で決めます。

## Technology候補の履歴

Herdr / Orca / Factory / Cursor / GitHub Agents / Local AI等は、Discussionで挙がったTechnology候補です。候補名はここに集約し、Coreの必須構成要素へ結び付けません。各候補の能力・提供状況・性能・採用状態は今回調査しておらず、比較評価の結果もありません。

Local AIはActorの分類としても扱います。個別のLocal AIのModel・Runtime等の選定は、同じ評価過程を経る対象です。

## Version FreezeとRebuild

Version Freezeは、制作を開始できると人間が判断した範囲・版・既知の制限を固定し、Projectで使う基準を安定させる考え方です。制作中の改善は原則Next / Labへ送ります。緊急変更の条件やProjectの版移行はOpen Questionです。

Implementationの再構築も選択肢に含めます。[Future Vision](FUTURE_VISION.md)に記録した保持対象を引き継ぎ、既存のRequirementsとBenchmarksに照らして移行可能性を評価します。Rebuildの許可を設計思想だけから推定せず、個別の影響・評価・Human Approvalを扱う手順をB-10で提案します。
