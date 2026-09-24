# tOS — Technology Evolution, Freeze and Rebuild Policy

状態：B-10としてHuman Review承認済み（[PR #22](https://github.com/tanakakeisuke-github/tOS/pull/22)）。技術の調査、Benchmark / PoC、導入、Project移行、運用検証は本書の作成によって実施済みにならない。tOS v0.1全体の完成条件やFreezeを定める文書でもない。

本書は[Constitution](../CONSTITUTION.md)のHuman Gateの下で、[Evolution Model](../vision/EVOLUTION_MODEL.md)を判断手順へ具体化したものである。候補の記録欄は[Technology Radar](../research/TECHNOLOGY_RADAR.md)を使う。仕事の入口は[Triage](../protocols/TRIAGE.md)、成果と証拠の照合は[Review](../protocols/REVIEW.md)、判断・理由・失敗の正本は[Knowledge Architecture](KNOWLEDGE_ARCHITECTURE.md)に従う。Runtime / Orchestrator / Vendorの交換時に守る境界は[Core Architecture](CORE_ARCHITECTURE.md#実行技術との交換点)を参照し、ここで重複定義しない。

## 二つの独立した軸

**Radar状態**は「特定の候補を、特定の用途と条件でどう扱うか」を示す。**変更区分**は「変更案をどの版・場で検討するか」を示す。候補の状態、変更案の行き先、承認済み版、Projectへの適用は別々に記録する。

| Radar状態 | 判断上の意味 | 必要な記録 |
|---|---|---|
| WATCH | 用途・未知を追跡する。評価や採用を意味しない | 出所、用途仮説、未知、次の調査条件 |
| TRIAL | 範囲を限定してBenchmark / PoCを行うことを承認された状態。成功を意味しない | 対象・期間・比較基準・安全な停止条件・結果への参照 |
| ADOPT | 人間が、用途・条件・対象となる次版への採用を明示的に認めた状態 | 承認者と時点、証拠、対象版、制限、測定・撤回条件 |
| HOLD | 評価・採用・利用の判断を保留または撤回した状態 | 理由、影響範囲、再評価条件、必要ならRollback記録 |

未評価候補はWATCHで記録し、評価未実施を明記する。ADOPTでも、指定範囲外の用途や現行Projectでの利用は認められない。失敗・前提変化でHOLDへ戻せる。Radar状態の変更には根拠と人間の判断を残す。

| 変更区分 | 扱う対象 | 適用上の境界 |
|---|---|---|
| Current | 制作に使う、人間が承認した版とその固定範囲 | 既存Projectの選択版を指す。候補発見やRadar変更では書き換えない |
| Next | 次版へ向けた変更案・統合・検証 | Nextへ入っても、FreezeやProject移行まではCurrentではない |
| Lab | 隔離した限定実験 | Lab結果だけで制作環境や版を変更しない |

区分は候補そのものではなく変更案に付け、Triageの人間判断と版を記録する。例えばTRIALは通常Labで評価できるが、同じ語の組合せが自動的に決まるわけではない。NextにあるADOPT候補もCurrentやProjectへ自動適用されない。現時点のtOS Current版・Freeze日は未設定である。

## 探索から継続・撤回まで

各段階は独立した判断点である。必要な証拠が欠ければその段階で止め、[Triage](../protocols/TRIAGE.md)またはHuman Reviewへ戻す。TaskのReady / Doneの手順自体は既存の仕様・Protocolを使う。

| 段階 | 出力と証拠 | 次へ進む条件・停止点 |
|---|---|---|
| Discover | 候補の出所、用途仮説、解きたい問題、未知をRadarにWATCHとして記録 | 発見だけでは試験・採用・Current変更をしない |
| Triage | 現行制作への影響、代替案、対象区分案、Task案、依存と停止点 | [Triage](../protocols/TRIAGE.md)で人間が振分けとReadyを判断。範囲外・入力不足ならSTOP / SPLIT / PROPOSE |
| Evaluate | 現状の基準版、比較対象、期待効果、品質・費用・時間・安全性・継続性などの評価項目、受入閾値、撤回条件を事前に記録 | 比較基準や許容できない影響が未定ならPoCへ進めない。候補の主張を測定結果と混同しない |
| Benchmark / PoC | 限定環境・対象版・方法・データ・結果・失敗・再現条件・未実施検証を残し、既存実装と同じ基準で比較 | 必要な測定が未実施なら「未確認」。実験の実施は採用承認ではない |
| Human Approval | Review結果、比較、制約、移行・撤回案と未解決事項を提示 | 人間が用途・条件・次版の対象を明示的に承認した場合だけADOPTへ。否決・保留なら理由付きHOLD / WATCHへ |
| Next Version | 承認範囲を次版案に組み込み、版差分・適合確認・既知の制限・移行案を記録 | 採用判断だけでCurrentやProjectを変更しない。次版のFreezeは別の人間判断 |
| Measure | 実際に承認された範囲で導入した後、事前の基準に対する効果・副作用・失敗・運用負担を記録 | 未導入なら測定済みとしない。結果不足や許容外の影響は拡大を止める |
| Keep / Rollback | 継続または撤回の人間判断、理由、適用範囲、版、実行・確認結果、残る影響を記録 | Keepは対象範囲だけ。Rollbackは復元と再検証を確認するまで完了扱いしない |

評価値や閾値は候補・用途・Projectごとに事前に決める。全技術に共通の数値を本書では設定しない。結果は成功例だけでなく失敗と未確認事項も、出所・適用版・承認状態付きで正本へ戻す。

## Freezeと変更の境界

Freezeは「制作に使える」と人間が判断した**特定の対象**を固定する。対象はCore版、必要ならStudio Template版、Projectが選ぶ組合せ、実行技術と設定のうち再現に必要な範囲、互換条件、既知の制限を明示する。未定の項目がある場合は未知として扱い、暗黙に固定済みとしない。Freeze記録には対象版・参照先、判断者・時点、根拠となるReviewと検証、許容する変更範囲、Projectへの適用条件、解除・次版移行の条件を含める。

Freezeの承認には、指定範囲の受入条件と必要な検証が確認され、既知の制限と残リスクを人間が受け入れた記録が要る。Freeze後の改善は原則Next / Labに送り、Currentを変えない。Freeze解除または後継版への切替は、理由、影響Project、比較証拠、移行・撤回可能性をReviewし、人間が版と適用範囲を指定して承認する。後継版の存在だけでは既存ProjectのFreezeを解除しない。

制作中のCurrent例外変更は、現行版を保つことによる具体的な障害や重大な損失があり、次版まで待つ案を含む選択肢を比べる場合に限り提案する。緊急性の申告だけでは適用しない。変更前に影響するProject・Task・版、原因と証拠、最小変更範囲、代替案、必要な検証、復元手段と発動条件、承認者を記録する。人間が対象と条件を明示して承認し、変更後の確認と失敗時の戻し方を用意してから適用する。差し迫って十分な検証ができない場合は、その欠落と残リスクを示して人間の判断を待つ。例外は次版への恒久採用を意味しない。

## Projectの版移行とRollback

Projectは採用候補ではなく、明示的に選んだCore / Template / 必要な実行技術の版を使用する。移行案には現行と移行先の版、目的、Project固有の制約・制作段階・進行中Task、互換性とデータ・成果物への影響、既存版との比較、必要な検証、作業停止時間、戻す版と復元手段を含める。移行で改善する点と失う可能性がある点をHuman Reviewへ示し、人間がProject単位の範囲・時点・受入条件を承認してから実施する。次版の採用やFreezeはProject移行の承認を代替しない。

Rollbackを検討する条件は、事前に定めた測定・受入基準の未達、制作や知識の受け渡しへの重大な障害、互換性の破綻、許容できない副作用、必要な検証の失敗である。実行時は影響する作業を止め、証拠と対象版を保全し、戻す版・データ整合性・残る影響・再検証条件を確認して人間が判断する。安全上の封じ込めが先に必要な場合でも、恒久的な版変更・再開・Keep判断は人間の承認に戻す。復元が不可能または未検証なら「Rollback可能」と約束せず、代替の復旧案とリスクを提示する。失敗と判断理由は次の評価に残す。

## Implementationを再構築する場合

Rebuildは、既存Implementationを維持・部分交換する案と、作り直す案を同じ目的・Requirements・Benchmarksで比較する候補である。AIによる再構築コスト低下や無改修交換は未実証であり、再構築の優位性を前提にしない。[Future Vision](../vision/FUTURE_VISION.md#作り直せるものと引き継ぐもの)と[Purpose](PURPOSE.md#実装を越えて保持する価値)に沿い、**Principles / Requirements / Decisions / Learnings / Failures / Benchmarks / Project History**を、出所・承認状態・適用版とともに引き継ぐ。正本・優先度・競合の扱いは[Knowledge Architecture](KNOWLEDGE_ARCHITECTURE.md)に従う。

提案時に保持対象の所在と欠落を棚卸しし、[Core Architecture](CORE_ARCHITECTURE.md#実行技術との交換点)の受け渡し契約、既存ProjectとTemplateへの影響、移行・Rollback手段を照合する。限定PoCでは既存実装と同じ入力・評価条件で品質、時間、費用、失敗、運用・移行負担を測る。比較不能な項目や未測定の項目はそのまま明示する。Rebuildの開始、採用、Project移行、旧実装の撤去はそれぞれ範囲と証拠を示した人間の判断を要する。再構築後もMeasureとKeep / Rollbackを経て、学びと失敗を保持する。
