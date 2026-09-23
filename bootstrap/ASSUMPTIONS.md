# tOS — Assumptions

状態：Draft。仮定は確定事項として扱わず、依存する判断の前に確認する。

## 現時点で明示された前提

- 正式名称はtOS。Greenfieldで設計し、旧構造を自動継承しない。
- 今回はKnowledge Bootstrapだけを作成し、Draft PRでHuman Reviewを待つ。
- 指定された原則と構想を保持する。実装範囲・運用開始・製品採用は別の判断である。
- GitHubを将来のSource of Truth / Project Memory / Work Managementの中心とする。

これらは依頼で明示された条件であり、下記の仮説とは区別する。

## 検証すべき仮定・仮説

| ID | 仮定・仮説 | 外れた場合の影響 | 確認方法案 |
|---|---|---|---|
| A-01 | 選択したKnowledgeだけでFresh WorkerがTaskを理解できる | 欠落による誤解、再説明 | Repositoryのみからの理解テスト |
| A-02 | 小さなTaskとHuman Gateの負担が運用可能な範囲に収まる | 承認待ち、過度な細分化 | 人間の時間と修正回数を測る |
| A-03 | 媒体共通のCoreと媒体固有Templateを分離できる | Coreが肥大化、Templateで表現不足 | 複数媒体の限定ケースで検証 |
| A-04 | 異なるActorが同じTask契約を利用できる | Adapterごとの仕様分岐 | 同じ課題で能力・証跡・権限を比較 |
| A-05 | Version Freezeと次版改善の分離が制作を安定させる | 版の分岐管理や移行の負担 | Project運用と移行の記録 |
| A-06 | GitHub中心の記録が素材の所在・来歴も管理できる | 外部Artifactとの参照切れ | 所在・版・検証可能性を確認 |

## 文書化上の選択

主文は日本語、共有語彙は英語表記を併記する。読み順と優先順位を明示し、手順・field例は提案と表示する。これは表現上の選択であり、将来のschemaやUIを固定しない。

OS Version、承認責任者、最初のProject、対象製品の実体、数値benchmark、保存方式は仮定で補わず[未決定](OPEN_QUESTIONS.md)として扱う。現時点の文書に架空の実施結果や採用記録を追加しない。
