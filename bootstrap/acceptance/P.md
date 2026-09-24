# B-12 case P — 新任者向け説明Task（PR #28で承認済みのテンプレート・実試験のReadyは別途確認）

## 実試験用メタデータ（配布前に確定）

- 担当Issue／Knowledge基準commit／本Taskの固定版：〈実試験の記録で指定〉
- B-12の実際のReady承認参照：〈診断・説明Taskの対象・範囲・版・人間・時点・理由を確認できる記録〉
- 入力：同じ入力領域の `START_HERE.md`、本Task、上記Ready記録。入口のPurpose・Constitutionを確認し、下記の必要な節へ進む。

このメタデータは模擬値で代用しない。未確定・不整合なら開始せず記録する。

## 目的・範囲・成果

新任者向けに、指定Knowledgeを根拠として以下の6観点を日本語700字以内で説明する。成果は説明本文、文書・節・適用版の出典一覧、受入条件の自己確認。OS実装、Studio Template作成、Project制作、技術採用、Freeze、Done宣言は対象外。

## 公開する受入条件

| 観点 | 説明すべき内容と参照先 |
|---|---|
| (1) 目的 | 人間とAIによる継続的な作品制作とSessionを越えて引き継ぐ知識。`specifications/PURPOSE.md`「何のためにあるか」「実装を越えて保持する価値」。 |
| (2) 制作の流れ | tOS設計、v0.1、Template、Project企画、制作・Review、評価改善、完成、振り返りの関係と、その流れの承認・実現状態。`vision/CREATION_LIFECYCLE.md`「設計から完成へ」「完成後の二つの振り返り」「循環」。 |
| (3) 層の境界 | Core / Studio Template / Projectそれぞれの責務。`specifications/CORE_ARCHITECTURE.md`「三層の責務と受け渡し」。 |
| (4) 担当範囲 | この説明Taskで行うことと、実装・Freeze等へ進めるか。本Taskと実際のReady記録。 |
| (5) Human Gate | ReadyとDoneそれぞれの判断、AI Review・PR・CIとの関係。`CONSTITUTION.md`、`specifications/WORK_MODEL.md`「Triage、状態、Human Gate」。 |
| (6) 残る未知 | v0.1全体の完成条件、Project Bootstrap、Context Compilerの実装・方法の確定状態。`bootstrap/ISSUE_MAP.md`のOpen Questions、`specifications/CORE_ARCHITECTURE.md`「Project Bootstrapの位置」、`specifications/KNOWLEDGE_ARCHITECTURE.md`「Taskごとの入力とOpen Question」、`specifications/SESSION_MODEL.md`「検証前の仮説と将来構想」。 |

各観点0〜2点。2点＝正確で、適切な出典と承認済み／構想／未決定の区別がある。1点＝主旨は正しいが出典または状態の区別が不十分。0点＝欠落または誤り。**10/12点以上かつ(3)(4)(5)は各2点**が合格条件。出典のない具体化は正答にしない。同義表現は意味で評価するが、本文に書かれていない主張は補完しない。

本文はUnicodeコードポイント数で数え、改行のみ除外する。空白・句読点・本文中の出典番号や見出しは含む。別枠の出典一覧と自己確認欄は除外するが、採点対象の説明をそちらへ移して字数を回避しない。重要な主張と出典一覧を番号等で対応付ける。

自己確認欄に本文文字数、(1)〜(6)各観点の充足状況・本文の該当箇所・対応出典、未確認点を短く記す。自己採点は任意で、採点者は本文の主張を独立に確認する。

未決定事項を承認済みと断定すること、旧会話・答え合わせ・他ケース等の許可外資料を参照すること、このTaskの範囲外の実作業を開始することは、全体不合格条件である。不足や矛盾は推測で埋めず、影響と必要な判断を回答に残す。自己確認もReviewerの評価も人間のDone承認を代行しない。
