# Technology Radar — 記録構造

状態：B-10の記録様式としてHuman Review承認済み（[PR #22](https://github.com/tanakakeisuke-github/tOS/pull/22)）。この文書は候補を記録するための空の様式であり、Technology / Vendorの調査、性能評価、利用可能性確認、採用、実導入を示さない。

[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md)の判断に必要な候補・根拠・履歴を記録する。Radar状態（WATCH / TRIAL / ADOPT / HOLD）と変更区分（Current / Next / Lab）は独立している。Radarに候補が載ること、TRIALやADOPTになることだけで、承認済みCurrent版やProjectの選択版は変わらない。改善案の入口は[Triage](../protocols/TRIAGE.md)、証拠の照合は[Review](../protocols/REVIEW.md)、判断の正本・承認状態は[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md)に従う。

## 候補レコードの様式

候補ごとに一件を作り、状態が変わっても以前の判断を消さず履歴へ追記する。未調査・未評価・未決定は空白ではなくそのまま記す。候補名だけから能力や提供状況を推定しない。

| 欄 | 記入する内容 |
|---|---|
| Record ID / 更新日 / 記録者 | 一意の識別子、対象とした情報の時点、記録責任者 |
| 候補と分類 | Technology / Model / Runtime / Orchestrator / Vendor等の候補名と、何を交換・改善する仮説か。事実と仮説を分ける |
| 出所と確認状態 | 一次資料や提案への参照、確認日、未確認の主張と変動しうる条件 |
| 問題・用途・対象範囲 | 解くべき問題、想定用途、対象となるCore / Template / Project・版。対象未定なら未定と書く |
| Radar状態と判断 | WATCH / TRIAL / ADOPT / HOLD、理由、決定者・時点、承認記録への参照。未承認なら提案として記す |
| 変更案の区分 | Current / Next / Labの振分け案または人間が決めた区分とTriage参照。未振分けを許す |
| 評価計画と比較基準 | 現行実装・代替案、事前の指標と受入閾値、PoCの範囲・期間・停止条件 |
| 証拠と結果 | 実施したBenchmark / PoCの方法・条件・結果、失敗、再現性、未実施の検証。実施前なら「未評価」 |
| 影響・制約 | Coreの交換境界、知識・データ、費用・運用、セキュリティ等の影響と未知 |
| 版・移行・撤回 | 採用を認めた用途・対象次版・条件、Project移行の別承認、測定計画、Rollback条件。該当しなければ「未決定」 |
| 次の判断点 | 次に必要な調査・Task・人間の承認、担当、再評価日または再開条件 |
| 判断履歴 | 状態・区分・版の変更前後、理由、証拠、承認記録、失敗・撤回の参照を追記 |

新規候補の初期状態は、出所と用途仮説しかなければ**WATCH / 未評価 / 変更区分未振分け / 採用未承認 / Project適用なし**と明記する。TRIALには限定評価のReady承認と計画を、ADOPTにはHuman Approvalと用途・条件・対象次版を記録する。HOLDには停止理由と再評価条件を記録する。Currentの例外、Project移行、RollbackはRadar欄だけで決定せず、[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md#freezeと変更の境界)の個別判断記録へ接続する。

## 記入テンプレート

```text
Record ID: 未採番
候補・分類: 未記入
出所・確認日・未確認事項: 未記入
問題・用途仮説・対象範囲: 未記入
Radar状態: WATCH（初期案、採用未承認）
変更区分: 未振分け（Triage判断待ち）
現行比較対象・評価指標・閾値: 未決定
Benchmark / PoC: 未評価
影響・制約・未知: 未決定
対象次版・Project適用: 未決定・適用なし
測定・Rollback条件: 未決定
次の判断点・担当: 未決定
判断履歴・承認参照: なし
```

このテンプレート自体は実在候補のレコードではない。既存のDiscussionに挙がった名称も、個別の出所・用途・評価・人間の判断を確認するまでは採用済みや利用可能と記録しない。
