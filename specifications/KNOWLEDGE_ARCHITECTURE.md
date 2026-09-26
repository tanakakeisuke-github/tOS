# tOS — Knowledge Architecture

状態：B-04としてHuman Review承認済み（[PR #10](https://github.com/tanakakeisuke-github/tOS/pull/10)）。対象はKnowledgeの正本、参照、状態、Task別の読み方であり、保存システムやContext Compilerの実装を定めない。

[Purpose](PURPOSE.md)は承認済みの目的・範囲、[Constitution](../CONSTITUTION.md)は承認済みの原則とHuman Gateの正本である。本書は両者の規範を再掲せず、知識を引き継ぐ際の配置と判断経路を定める。tOS v0.1全体の範囲と完成条件（OQ-01）は未決定のままである。

## 正本と分類

GitHub上の対象Repositoryと担当IssueをKnowledgeのSource of Truthとする。一つの概念の現行規則は一つの正本で管理し、索引、Issue、Review、他の文書には参照と状態だけを置く。媒体やProject固有の規則は[Core Architecture](CORE_ARCHITECTURE.md)の層の所有範囲に置き、Coreの正本に無断で取り込まない。以下の将来の保存先は配置案であり、ディレクトリや運用基盤の作成を意味しない。

| Knowledge | 正本の所有先 | 他の記録との関係 |
|---|---|---|
| Principles | `CONSTITUTION.md` | 運用手順は担当する仕様から参照する。 |
| Requirements | 目的と現在の範囲は `specifications/PURPOSE.md`。個別の実行上の要件は担当する `specifications/` 文書。Task固有の受入条件は担当Issue。 | Issueで挙がった要件案は承認済み仕様へ自動昇格しない。 |
| Decisions | 現行規則は対象を所有する仕様の承認済み改訂。判断理由・承認者・時点は、Decisionごとに一つを正本と指定した担当IssueまたはReviewの記録。 | 承認時に正本の識別子とリンクを明示し、他方の記録はそこへリンクする。正本が不明・競合するときは適用を止めて人間に確認する。 |
| Learnings | 観察・仮説は `bootstrap/FINDINGS.md` 等のFinding記録。採用済みの一般則は所有する仕様。 | Findingを実証済み要件として扱わず、出典となるOutcomeを結ぶ。 |
| Failures | 発生したTaskまたはProjectのOutcome記録（担当Issue・Reviewと成果物の参照）。 | 原因の仮説、再発防止案、採用された変更を別の状態で記録する。 |
| Benchmarks | 評価基準は対象を所有する仕様またはTaskの受入条件。測定条件と結果はOutcome記録。 | 数値結果から基準の変更を推定しない。 |
| Project History | 当該Projectの履歴記録。Bootstrapの経緯は `bootstrap/HISTORY.md`。 | 経緯調査の資料であり、現在の規則の正本ではない。 |

新しい概念の保存先が未定なら、担当Issueで所有層と候補文書を明示し、人間の判断を経てから正本を設ける。同じ規則を複数の仕様へ複写しない。旧記述を置き換える際は、旧版から新しい正本への参照と適用版を残す。

## 版・状態・出所

各判断または記録は、少なくとも **識別子／所在、対象と所有層、出所、承認状態、適用する版またはTask・Project、判断した人間と時点（該当する場合）、置換先または関連記録** を辿れるようにする。Decisionは承認時に理由と承認記録の正本を一つ指定し、その識別子とリンクを仕様の改訂・担当Issue・Reviewから辿れるようにする。GitのcommitとIssue・Reviewへのリンクは版と判断経路の証拠に使う。リンクだけで承認済みとは判定しない。

状態は「提案・Review中」「承認済み」「置換済み」「却下・撤回」「Open Question」を区別する。承認済みの範囲だけを適用し、提案、仮説、結果、未決定事項から規則を補わない。置換済みの文書は過去のTaskを解釈する資料として残し、新規Taskには明示された現行版を使う。状態または適用版が読み取れない場合は、その規則に依存する作業を止めて担当IssueまたはReviewで確認する。古いcommit上の「Review中」などの表記は、そのcommit時点の状態として扱い、現時点の承認を推定しない。

## 読む優先度と衝突

適用範囲、版、承認状態を照合した上で、知識の読む優先度は **Specification → Decision → Outcome → Transcript** とする。Specificationは現在の約束、Decisionは採否と理由、Outcomeは実際の結果と検証、Transcriptは経緯調査の手掛かりである。順序は下位の証拠を無視する許可でも、上位をAIが無条件に上書きする規則でもない。PurposeとConstitutionの承認済み規範は、それぞれの正本として確認する。

新しいDecisionまたはReady承認済みIssueの受入条件が承認済みSpecificationと食い違う、Specification同士が矛盾する、またはSpecificationがPurpose・Constitutionと衝突する場合、影響する作業を止める。IssueのReady承認は、既存仕様の黙示的な改訂とは扱わない。担当IssueまたはReviewに、双方（Issueを含む）の箇所と版、承認状態、影響するTask、解決案を記録し、人間に適用判断と必要な仕様改訂を求める。Decisionの日付の新しさだけで旧仕様を暗黙に失効させない。承認された改訂が正本に反映され、適用版が確定してから再開する。OutcomeやTranscriptに新情報があっても、同じ経路で提案・判断・仕様改訂を行う。

## visionから仕様への移行

`vision/` は設計意図、将来構想、検証前の運用案を保持する。実行上の規則にする候補は担当Issueで出典となるvisionの節を指定し、対象層・範囲・未決定事項を絞って `specifications/` の所有文書へ記す。人間のReviewと承認を受け、適用版を明示する。vision側には仕様への参照と移行状態を残し、同じ運用規則の改訂先にしない。visionに残る説明と仕様が食い違う場合は、版・承認状態を確認し、規則の解釈に影響すれば上記の衝突手順を使う。

## Taskごとの入力とOpen Question

Fresh Workerは `START_HERE.md` の入口からPurpose、Constitution、担当Issueを確認し、Issueが指定する基準版とInput Contextに沿って必要な仕様・Decision・成果物だけを選ぶ。選択の単位は「そのTaskの目的、受入条件、依存、停止点を説明し、成果をReviewできるか」とする。各資料について必要な節、適用版、選んだ理由を示せるようにし、不足や曖昧さはIssueで確認する。索引やHuman Viewは到達を助ける参照であり、正本を増やさない。

TranscriptとProject Historyは標準の全読から外す。Decisionの理由や出所の調査に必要なときだけ、対象範囲と目的を明記して参照する。会話から見つけた情報は承認済みKnowledgeへ自動昇格させない。

Open Questionは担当Issueまたは所有するKnowledge文書に、問い、影響範囲、必要な判断者、関連する版・出典、次の判断点を付けて保持する。解決時には判断と理由、承認、反映先の正本を結ぶ。未解決の問いに依存する作業は、その範囲を止める。OQ-01を本書で解決したことにはしない。

将来のContext Compilerは、上記の選択と参照をTask別のContext Packageへまとめる構想にとどめる。自動抽出、優先度判定、承認判定、品質保証の方法や実装時期は本書で確定しない。

## Proposal — Layered Context

**状態：追加ProposalとしてHuman Review承認済み（[Project Context Human Acceptance](../outcomes/project-context-human-acceptance/README.md)）。** この節はB-04で承認された正本・優先度・Task別入力の契約を置き換えない。この採用は、新しい必須入力や自動的なContext生成を意味しない。状態更新とMerge手順は[Project Context Model](PROJECT_CONTEXT_MODEL.md#proposal-lifecycle-and-adoption)に従う。

Projectをまたいで使うContextは、次の層で考える。上の層ほど共通だが小さく保ち、下の層ほど担当Taskに必要なものだけを選ぶ。

`OS → Studio → Project → Task → Relevant Knowledge`

| 層 | Contextとして渡す役割 | 所有する詳細の例 |
|---|---|---|
| OS | 媒体を問わない原則・共通の作業と知識の境界を示す。 | Coreの仕様、Constitution |
| Studio | 媒体の制作を具体化する前提を示す。 | Studio TemplateのRole、成果物、評価観点 |
| Project | 一つの作品・製品の向きと現在地を短く示す。 | `PROJECT_CONTEXT.md` とそこから参照するProject固有の正本 |
| Task | 今回の仕事を安全に開始・Reviewできる条件を示す。 | 担当Issue、Ready承認、目的・範囲・受入条件・停止点 |
| Relevant Knowledge | Taskの判断に必要な正本と証拠だけを選ぶ。 | 指定されたSpecification、Decision、Outcome |

原則は **「Global Contextは小さく提供し、Local ContextはTaskごとに選択する」** である。Project ContextはProject全体の地図であり、Purpose、Constitution、仕様、Decision、Outcome、担当Issueを複写して新しい正本にしない。Task ContextはProject Contextを読むことでReady、入力版、受入条件、依存、停止点の照合を省略しない。Relevant Knowledgeの選択、`Specification → Decision → Outcome → Transcript` の優先度、版・承認状態・矛盾時の停止は、既存の本書の規則に従う。

全Project向けのProject Contextの責務・Base Schema・媒体固有extensionの境界は[Project Context Model](PROJECT_CONTEXT_MODEL.md)を提案する。Context Compilerは将来構想のままとし、このProposalは実装方式、自動選択、承認判定、品質保証を確定しない。

## 参照経路の例（架空）

仮に「架空Projectの試作品についてPlaytest評価項目を整理する」Taskが承認されたとする。Workerは入口でPurposeとConstitution、担当Issueの目的・受入条件・基準commitを確認し、Issueが指定するCoreの境界、該当Studio Templateの評価観点、Project固有の目的と制約を読む。評価基準はそのTaskまたは所有する仕様から、前回の測定結果は指定されたOutcomeから取る。媒体の例や過去の会話を承認済み基準へ昇格させない。TemplateやProjectの該当資料がまだ存在しなければ、欠けた入力と影響をIssueに示し、その判断を要する作業を止める。

さらに、承認済み仕様が「評価項目Aを使う」とし、後日のDecision記録が「Aを外す」と述べる一方で、仕様の改訂と適用版が確認できない場合、Workerはどちらも黙って採用しない。両記録のリンク・版・承認状態、評価Taskへの影響をIssueまたはReviewに記し、人間の適用判断と仕様反映を待つ。改訂が確認できた版から、そのTaskを再開する。
