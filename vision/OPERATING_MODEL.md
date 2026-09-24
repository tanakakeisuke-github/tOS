# tOS — Operating Model

状態：依頼で指定された運用思想の保存。実行可能な詳細仕様・ProtocolはIssue Mapの後続成果物。

## 仕事と会話の寿命

**Discussion ≠ Task**。Discussionは問いや選択肢を検討する場、Taskは実行する小さな目的です。Discussion / Taskは比較的長寿命で、AI Sessionは短命です。Sessionが終わっても判断・成果・残課題から仕事を再開できるようにします。

**1 Task = 1 small objective**。分割の基準は、Fresh AIが一度のSessionで理解→作成→自己確認できる認知負荷です。ファイル数や時間だけで機械的に区切る考え方ではありません。

**1 Issue = 原則1 Fresh Worker**。WorkerとReviewerは可能な限りFreshかつ分離し、Reviewerが成果物・受入条件・根拠を独立に確認します。継続Sessionや兼任が必要な例外と、その記録方法は後続設計で明示します。

## TriageとHuman Gate

Discussionから出た案・課題をTriageし、Taskにするか、追加検討するか、次版の評価へ送るか整理します。

- **Ready前Human Gate**：目的、範囲、入力、受入条件、依存を人間が確認し、着手を承認する。
- **Done前Human Gate**：成果、Review、必要な検証、未解決事項を人間が確認し、完了を承認する。

AIの自己確認はこれらのGateを置き換えません。Gateの記録形式、担当者、PRのmergeとの関係は未決定です。

## STOP / SPLIT / PROPOSE

この三つを、範囲と不確実性を扱う基本の判断として残します。以下の具体的説明はProtocol化する際の提案です。

| 判断 | 説明案 |
|---|---|
| STOP | 入力不足・矛盾・承認不足などで判断できない点と再開条件を残して止まる |
| SPLIT | 目的や認知負荷が大きい場合、分割案と依存を提示して着手範囲を見直す |
| PROPOSE | 追加の改善は根拠・影響・検証案を添え、現在のTaskと別にTriageへ渡す |

## 知識を引き継ぐ

**Chat is disposable. Knowledge is permanent.**

Knowledgeの優先度は **Specification → Decision → Outcome → Transcript**。承認状態と適用版を確認して使うための順序です。上位文書と新しいDecisionが食い違う場合の調停方法は、B-04の設計対象です。

Transcriptは経緯調査の資料として保存できますが、Fresh Workerに必要な入力はTaskに関係するKnowledgeから選びます。会話全文を無条件に再投入せず、未決定事項はOpen Questionのまま引き継ぎます。

GitHubをKnowledgeのSource of Truthとする方針です。Human ViewとAI Onboarding Knowledgeの分離は[FindingsのF-03](../bootstrap/FINDINGS.md#f-03--human-viewとai-onboarding)に記録した仮説として検証します。

## 将来のContext Compiler

TaskごとのContext Packageを生成する構想です。Taskの目的、関連仕様・Decision、必要な成果物、承認状態から読むものを絞り、再開とReviewを支えます。自動生成の方式・品質評価・実装時期は未決定で、当面のContext選定手順はB-04/B-06/B-09で設計する提案です。
