# tOS — Technology Evolution

状態：Draft。Radar、Current / Next / Lab、Version / Freeze、Learning Loopは指定された思想。移行手順は提案。

## Discover continuously, adopt deliberately

新技術の発見と、制作環境への採用は別の活動として管理する。最新であることを完成条件にしない。必要な品質・費用・安定性・交換性を、対象と条件を固定して評価する。

| 区分 | 意味 | 更新の境界 |
|---|---|---|
| Current | 承認された現在のbaseline | 採用Projectの安定性を優先 |
| Next | 次版に向けた変更候補 | 評価・レビュー中。使用許可ではない |
| Lab | 限定した実験 | 実験範囲だけの承認。成果を直接Currentへ入れない |

現段階では運用中のCurrent Versionは未設定。このBootstrap DraftをCurrentやリリースv0.1と呼ばない。Next / Labも概念上の区分であり、環境やブランチは未作成である。

WATCH / TRIAL / ADOPT / HOLDは個々の技術候補の判断状態であり、Current / Next / LabはOS改善と利用の区分である。TRIALは承認された限定実験、ADOPTは対象用途・版に対する承認を表す。ADOPTでも既存ProjectのFreezeを自動解除しない。詳細は[Radar](../research/TECHNOLOGY_RADAR.md)。

## Version / Freeze / Migration

Projectで採用したOS Versionは原則Freezeする。参照を「常に最新」にせず、後から判断条件を再現できる識別子に固定する。Versionの付番・release手段・互換性の定義は未決定。

移行する場合の提案手順：変更理由、影響Project、互換性、検証結果、費用、戻し方を提示し、人間が対象と時期を承認する。その後、新版への移行と確認を記録する。重大な問題があっても、緊急性だけでAIがFreezeを解除しない。影響する作業を止め、例外判断を求める。

## Rebuildable systems

Implementation、Runtime連携、UI、Automation、Agent設定は将来作り直せる。一方、Principles / Requirements / Specifications / Decisions / Learnings / Failures / Benchmarks / Project Historyを残し、新しい実装を評価する基準にする。

再構築可能性は「無断で既存資産を削除してよい」という意味ではない。変更前後の振る舞い、必要な移行、復元可能性、残すKnowledgeをレビュー対象にする。

## Studio Learning Loop

**Observation → Finding → Hypothesis → OS Improvement Proposal → Prototype → Validate → Next Version**。

1. Observation：制作中の出来事と条件を記録する。
2. Finding：証拠が支持する範囲で問題やパターンを言語化する。
3. Hypothesis：変更すると何が改善するか、反証条件を示す。
4. OS Improvement Proposal：作品固有か共通課題かを見極め、Triageへ送る。
5. Prototype：承認された小さな実験を行う。
6. Validate：同じ条件で評価し、失敗や費用も記録する。
7. Next Version：採否をHuman Reviewし、版として反映する。

Projectの振り返りとOSの振り返りを区別する。失敗した仮説もKnowledgeとして残し、自動的に次版へ採用しない。

Benchmark / Failure Library / Cost Ledger / Provenance / Project Bootstrapは将来候補。[Open Questions](../bootstrap/OPEN_QUESTIONS.md)に目的と決定前の条件を残す。これらの構築は今回の範囲に含めない。
