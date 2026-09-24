# tOS — Operating Model

状態：依頼で指定された運用思想の保存。実行可能な詳細仕様・ProtocolはIssue Mapの後続成果物。

## 仕事と会話の寿命

**Discussion ≠ Task**。検討と実行を分け、比較的長寿命の仕事を短命なAI Sessionへ渡しても継続できるようにする設計意図です。Discussion / Task / Issueの関係、Taskの粒度と状態・承認点は[Work Model](../specifications/WORK_MODEL.md)に整理しました（B-05仕様案、Human Review待ち）。WorkerとReviewerの分離やSessionの再開方法は後続Issueで具体化します。

## TriageとHuman Gate

検討中の案を人間が判断できる仕事へ整え、着手と完了の前に人間の判断を置く設計意図です。Triage、Ready・Done前のHuman Gateと記録の扱いは[Work Model](../specifications/WORK_MODEL.md#triage状態human-gate)を参照してください。具体的な実行手順は後続のProtocolで扱います。

## STOP / SPLIT / PROPOSE

この三つを、範囲と不確実性を扱う基本の判断として残します。以下の具体的説明はProtocol化する際の提案です。

| 判断 | 説明案 |
|---|---|
| STOP | 入力不足・矛盾・承認不足などで判断できない点と再開条件を残して止まる |
| SPLIT | 目的や認知負荷が大きい場合、分割案と依存を提示して着手範囲を見直す |
| PROPOSE | 追加の改善は根拠・影響・検証案を添え、現在のTaskと別にTriageへ渡す |

## 知識を引き継ぐ

**Chat is disposable. Knowledge is permanent.**

GitHubをKnowledgeのSource of Truthとする設計意図です。Knowledgeの分類・優先度、版と承認状態、Task別の読み順、TranscriptとOpen Questionの扱いは[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md)に整理しました（B-04で承認済み）。Human ViewとAI Onboarding Knowledgeの分離は[FindingsのF-03](../bootstrap/FINDINGS.md#f-03--human-viewとai-onboarding)に記録した仮説として検証します。

## 将来のContext Compiler

TaskごとのContext Packageを生成する構想です。Taskの目的、関連仕様・Decision、必要な成果物、承認状態から読むものを絞り、再開とReviewを支えます。自動生成の方式・品質評価・実装時期は未決定で、当面のContext選定手順はB-04/B-06/B-09で設計する提案です。
