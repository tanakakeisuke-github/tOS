# tOS — Purpose

状態：B-01の仕様案。着手承認済み、成果物はHuman Review待ち。保存済みKnowledgeの承認は、仮説の実証や本仕様案の承認を意味しません。

## 何のためにあるか

tOSは、人間とAIが協働し、作品の制作を継続するためのAI-native制作OSを目指します。短命なAI Sessionを越えて目的、意思決定、仕事の受け渡し、検証結果を復元できるよう、長期に残す知識と個々の制作作業を結びます。

作品を完成させた経験を次の制作へ引き継ぎ、制作環境そのものも改善できることが狙いです。人間・Cloud AI・Local AIの協働や実行技術の交換可能性は、そのための将来の設計方向です。現在の実装済み機能を表すものではありません。

## 対象媒体と将来への広がり

Game / Film / Music / Publishing / App等への展開を想定します。これらすべてへの対応を、現在の作業やtOS v0.1の必須要件にはしません。

共通のtOSから媒体に応じたStudio Templateを用意し、Projectごとに作品の目的と制約を具体化する将来像です。専門Role、成果物、制作段階、品質評価は媒体に応じて具体化します。TemplateやProject Bootstrapの実装、媒体共通のCore境界は本仕様の決定範囲外です。

## 実装を越えて保持する価値

Implementationを交換・再構築する場合も、以下の知識を判断材料として引き継ぐ方針です。

| 保持する知識 | 次の制作・実装へ渡す意味 |
|---|---|
| Principles / Requirements | 何を守り、何を満たす必要があるか |
| Decisions | 何を、なぜ採用・撤回したか |
| Learnings / Failures | 何を試し、何を学び、何がうまくいかなかったか |
| Benchmarks | 評価・比較の基準と結果 |
| Project History | 作品と制作上の判断がどのように変わってきたか |

AIによる再構築コスト低下は見通しであり、実測済みの効果ではありません。保持形式、版管理、移行時の同等性確認は後続設計に残します。作品固有の学びと制作システムの学びを分け、観察と仮説を混同せず、他のProjectへの適用を検討します。

## 現在の範囲と未決定事項

- **保存済みの土台**：KnowledgeとBootstrap Knowledge v0.1 Issue MapのHuman Reviewは承認済みです。これは設計意図と分解案の保存に対する承認です。
- **現在のB-01**：PurposeとFresh Workerの入口を作り、READMEの案内を整理します。本成果物のDone承認は未実施です。
- **BootstrapとtOS v0.1全体**：Bootstrap Knowledgeの受入と、tOS v0.1全体の完成・Version Freezeは別の判断です。v0.1全体の範囲・完成条件は未確定（OQ-01）です。この文書で確定させません。
- **今回の範囲外**：B-02以降の仕様化、OS本体の実装、Automation、GitHub Project設定、Studio Templateや作品の制作を開始する承認は含みません。

全体の長期的な流れは[Creation Lifecycle](../vision/CREATION_LIFECYCLE.md)、将来の構成は[Future Vision](../vision/FUTURE_VISION.md)、作業候補と未決定事項は[Issue Map](../bootstrap/ISSUE_MAP.md)にあります。これらの存在を、全読や後続作業の開始条件とはしません。

## 入力と承認

本案は[B-01 / Issue #3](https://github.com/tanakakeisuke-github/tOS/issues/3)と、そこで指定された基準commit `99c869f974b23ccf56197402a74f0063a9c7a5a4` のREADME、Future Vision、Creation Lifecycleだけから再構成しました。旧会話・旧PRの全文・Historyは入力に含めていません。

人間がPurposeの再構成と入口の分かりやすさを確認し、Doneを判断します。それまではDraft PRで停止します。新しい担当者の読み始めと停止条件は[START_HERE](../START_HERE.md)を参照してください。
