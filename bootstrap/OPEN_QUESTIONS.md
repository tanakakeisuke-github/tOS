# tOS — Open Questions

状態：Draft / 未決定事項の台帳。以下はTaskや実装の発注ではない。採用・順序・担当はHuman ReviewとTriageで決める。

## 次の設計で判断が必要な事項

| ID | 未決定事項 | 決めるために必要なもの | 未決定の間の扱い |
|---|---|---|---|
| Q-01 | tOS初版のscope / Definition of Done | Purposeに対する最小baselineと検証計画 | 本BootstrapをOS完成と呼ばない |
| Q-02 | Human Approvalの責任者・委任・証跡形式 | Ready / Done / Version変更の判断範囲 | AIが代理承認しない |
| Q-03 | Triageの担当・場所・運用頻度 | 新規発見の受付と判断方法 | 報告内の候補として渡す |
| Q-04 | Task / Discussion / Issue / Projectsの具体的構造 | small objectiveを維持する運用設計 | 旧構造を再現せず、設定を作らない |
| Q-05 | OS Versionの付番・release・互換性 | Freeze対象と移行条件 | Current Version未設定 |
| Q-06 | Knowledge metadata / ID / 置換・承認方式 | 参照と版を追える最小形式 | 文書の状態表示と相対参照を利用 |
| Q-07 | Context Compilerの手動運用・自動化scope | 欠落・矛盾・容量超過の検証 | 未実装の構想として保持 |
| Q-08 | 最初のStudio Templateと検証Project | 媒体を選ぶ理由、Coreとの境界 | 特定制作を既定にしない |
| Q-09 | Actor / Agent / Modelの選定・routing | 能力・費用・権限・評価証拠 | 指定製品や担当を推測しない |
| Q-10 | Runtime / Orchestrator / Local環境 | 限定試行、交換性、運用負荷 | Radarの観察候補に留める |
| Q-11 | Artifact / Transcriptの保存とアクセス | 版・所在・保持・権限・公開範囲 | 全文や大容量実体を自動転載しない |
| Q-12 | 独立ReviewerとFresh Worker受入方法 | 分離するContext、評価基準、Human判定 | 自己レビューと受入を区別 |
| Q-13 | Human Viewと同期方式 | GitHub正本との関係、更新責任 | 外部表示を正本化しない |
| Q-14 | Session Registryの必要最小scope | 継続・検索に必要な項目 | Registryを実装しない |

## 将来機能候補

| 候補 | 解決したい問い | 採用前に検討すること |
|---|---|---|
| Benchmark | 変更は本当に品質・速度を改善したか | 固定課題、評価者、再現条件、比較指標 |
| Failure Library | 同じ失敗をどう避けるか | 原因と症状の区別、条件、反証、再発防止の検証 |
| Cost Ledger | 人間時間・Cloud費用・Local計算・再試行に何を使ったか | 単位、対象範囲、欠測、集計と意思決定 |
| Provenance | 成果から入力・担当・Model・Decisionへ遡れるか | 最小metadata、版、保存とアクセス |
| Project Bootstrap | 新しい制作を繰り返し開始できるか | Template選択、Version固定、生成範囲、承認 |
| Capability Registry / Task Router | どのActorが適任か | 能力証拠、権限、選定基準、fallback |

これらを初版へ含めるかも未決定。候補が一覧にあることを、採用DecisionやReady済みTaskと解釈しない。

## 解決時の記録

決定した問いはID、選択、理由、検証、Human Approval、適用版、更新したSpecificationを結び付ける。未解決項目は未解決のまま残す。決定方式は[Decisions](../decisions/README.md)の提案を参照する。
