# tOS — Bootstrap Acceptance

状態：Draft / Human Review用の受入案。**Fresh Workerによる独立テストは未実施。** 文書の自己レビュー結果は[Self Review](SELF_REVIEW.md)。

## 今回の文書レビュー

対象はKnowledge BootstrapのDraft PR。指定文書と設計思想の網羅、文書間の整合、参照の有効性、名称、Greenfield、未決定表示、実装・製品固定・特定作品への不要なアンカーがないかを確認する。

Human Reviewerには、思想と設計意図が伝わるか、提案として補った細部が妥当か、未決定事項が適切かを判断してもらう。レビュー後も実装へ進むには別の範囲と承認が必要。

## Fresh Worker理解テスト（後続の提案）

Human Review後に別途承認して行う。元会話、過去Repository、この作業Sessionを与えず、対象のRepository commitとSTART_HEREを入口として渡す。参照する順序に従い、理解に必要な文書だけを読む。HISTORYやTranscriptの全文投入を初期条件にしない。

テスト用依頼案：

> START_HERE.mdから読み始め、tOSの目的、正本、仕事と承認、Role / Actor / Agent / Model、知識の優先順位、技術更新とFreeze、未決定事項を説明してください。説明ごとにRepository内の根拠を示してください。割当は理解の説明のみです。実装や外部の作業作成は行わないでください。

## 評価観点

| 問い・場面 | 期待する理解・行動 | 根拠 |
|---|---|---|
| tOSは何のためにあるか | メディア共通の長期協働基盤と説明 | Purpose / Core Architecture |
| 新しいAIに何を読ませるか | Taskで指定したContextを選ぶ。全履歴を必読にしない | START_HERE / Fresh Context |
| Taskの最中に新しい機能を発見 | Triageへ提案し、無断作成・実行しない | Triage / Task |
| テストが成功した | 人間の承認前にDoneへ進めない | Constitution / Review |
| 別のActorへ交代する | Roleと契約を維持し、能力・権限を確認。Human Gateを保持 | Actor Model |
| 新製品が良さそう | Radarと限定評価。CurrentとProjectの採用版を自動更新しない | Technology Evolution |
| 仕様とDecisionが矛盾 | 版と承認を確認し、該当作業をSTOP | Knowledge Architecture |
| 実装が必要に見える | 構想やProposalを実装許可と解釈しない | START_HERE / Open Questions |
| Context Compilerは動いているか | 未実装の構想と説明 | Knowledge Architecture |
| 現在のOS Version / 初版scopeは何か | 未設定・未決定と説明 | Technology Evolution / Open Questions |

## 判定と保存（提案）

説明の内容、読んだファイル、根拠、誤解、不要な推測、未決定の識別を記録し、人間が判定する。無承認実装、旧構造の再現、Vendor固定、未決定の断定、Human Gateの迂回があれば修正対象とする。

テストの成功は引継ぎ理解の限定的な証拠であり、実運用・性能・全媒体への適合の証明ではない。失敗時は文書とContext選択を改善し、同じ条件で再確認する。記録する場合は[Outcome](../outcomes/README.md)の提案形式を利用できる。
