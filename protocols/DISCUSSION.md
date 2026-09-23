# tOS — Discussion Protocol

状態：Draft。Discussion / Task分離は原則。以下は運用提案。

## 目的と入力

一つの論点について、要求、制約、選択肢、トレードオフ、判断材料を整理する。入力は人間の問いと関連Knowledge。ChatGPTはDiscussion / Planning / Directionの場所として扱う。

## 手順

1. 問いと今回決めたい範囲を示す。既知・仮定・未決定を分ける。
2. 関連Specification / Decisionを適用版で読む。追加調査の必要性を説明する。
3. 選択肢と採用・不採用理由を比較する。AIの推薦を人間の決定と混同しない。
4. 合意候補、未決定事項、根拠、影響を整理する。
5. Knowledge化する内容をレビューへ、実行が必要な候補をTriageへ渡す。

## 出力と停止

出力は論点の要約、選択肢、Decision案、Open Questions、必要ならTask候補。承認されるまでProposalとして扱う。会話での合意を正本へ移す際は、何を誰が承認したかを追える形にする。

実行の目的と受入条件が明確になった時点で、別の[Task](TASK.md)へ切り出す。Discussionを続けながら無制限に実装範囲を広げない。関連しない新論点は分離候補として記録する。

Session終了時は未決定も含めて[Handoff](HANDOFF.md)に整理する。全文Transcriptを次のWorkerの必須Contextにしない。
