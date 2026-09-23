# tOS — Knowledge Architecture

状態：Draft。優先順位・永続化・Context Compilerは指定された思想と構想。記録項目と競合処理の具体化は提案。

## 正本と知識の優先順位

GitHubを正本の中心とし、適用OS / Project Versionと承認状態を確認したうえで、**Specification → Decision → Outcome → Transcript**の順に読む。

| 種類 | 答える問い | 扱い |
|---|---|---|
| Specification | 現在何が求められ、どの制約を守るか | 適用版の規範 |
| Decision | なぜその選択になったか、代替案と影響は何か | 承認と変更理由の記録 |
| Outcome | 実際に何を行い、何が検証できたか | 成果と証跡、限界 |
| Transcript | どのような会話・探索を経たか | 必要時の一次経緯。未採用案も含む |

Constitutionはこれら全体の上位制約である。優先順位は矛盾を隠すための規則ではない。新しいDecisionと古いSpecificationが矛盾する場合、版・承認・置換関係を確認し、該当作業をSTOPして整合を求める。会話の新しさだけで規範を更新しない。

## 永続化するもの

Principles / Requirements / Specifications / Decisions / Learnings / Failures / Benchmarks / Project Historyを、実装を再構築するときにも残す。採用しなかった選択肢は理由が再検討に役立つ範囲で保存し、現行仕様と区別する。

文書の分類は知識の内容・対象・ライフサイクルを基準とする。組織や担当者は属性として記録し、組織変更で知識の意味や参照先が失われないようにする。具体的なID・metadata schemaは未決定。

## 記録に含めたい情報（提案）

- 状態、対象、適用版、作成・更新の根拠。
- 何を要求・決定・観察したかと、理由・制約・代替案。
- 関連Task、Specification、Decision、Artifactの参照。
- 承認者・承認対象の版・証跡、置換関係。
- 検証済み範囲、未実施の検証、不確実性。

過去の記録を黙って書き換える代わりに、訂正と置換を追えるようにする。[Decisions](../decisions/README.md)と[Outcomes](../outcomes/README.md)は将来の保存方法を説明する。

## Context Compiler構想

目的は、Taskに必要な正本からFresh Worker用Context Packageを組み立てること。全文圧縮だけでは、未採用案や欠落した承認を見分けられない。選択理由と参照元の版を追えることを重視する。

入力候補はTaskの目的・範囲・受入条件・承認証跡、Constitution、採用OS Version、関連Specification / Decision、必要なArtifact / code、既知の制約と未決定事項。出力候補は読む順序を持つ参照一覧、必要な抜粋、停止条件、不足一覧である。

手動でTaskにRequired Contextを指定することが最初の運用候補となる。自動生成、検索、要約、容量制御、実装技術、権限管理は未決定。Compilerの存在や性能はまだ検証していない。

提案する失敗時の動作：参照切れ、版の不一致、承認不足、矛盾、必要情報が容量に収まらない場合は不足を明示し、黙って省略・補完しない。生成したPackageは派生物であり、元の正本を置き換えない。

## Transcriptと来歴

Transcriptを保存してもFresh Workerへ無条件に再投入しない。必要な論点の調査で範囲を限定し、抽出した内容を規範・提案・観察に分類する。保存場所・保持期間・アクセス制御は未決定。

Provenanceは将来候補として、成果物から担当Actor、Agent / Modelの版、入力資料、Task、Decision、レビューへ遡れる形を検討する。公開Repositoryへ持ち込む情報の範囲は個別に確認し、元会話へのリンクを知識理解の必須条件にしない。
