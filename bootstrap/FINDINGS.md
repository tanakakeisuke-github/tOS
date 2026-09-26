# tOS — Bootstrap Findings

状態：Finding / Hypothesis。確定仕様や有効性を立証した実験結果とは区別して保存。

出典は[README](../README.md#出典と確認範囲)を参照。以下の検証方法は今回の提案で、未実施です。観察された不安と、実際のContext欠落量・原因を分けて扱います。

## F-01 — 長大ChatとContext品質

- **Finding（懸念）**：長大ChatでContext品質が低下するのではないかという懸念が設計の出発点になった。
- **Hypothesis**：Taskごとに必要な知識を選びFresh Sessionへ渡すことで、理解の混線や脱落を減らせる。
- **未確認**：会話長との因果、Model間の差、改善量。
- **検証案**：同じTaskと採点基準で、継続Chatと限定Contextの理解・成果・修正回数を比較する。

## F-02 — Project / Work間の引き継ぎ

- **Finding（経験）**：引き継ぎ時に、詳細Contextが十分伝わっているかという不安が実際に表明された。
- **Hypothesis**：期待する理解と必要な出典を明示し、受け手の説明を照合すれば、欠落を見つけやすくなる。
- **未確認**：具体的に失われた情報の網羅的な一覧と、欠落の発生経路。
- **検証案**：Fresh Workerに目的・範囲・停止条件・未決定事項を説明してもらい、期待回答と出典を人間が確認する。

## F-03 — Human ViewとAI Onboarding

- **Finding（経験・懸念）**：人間向けの説明を渡すだけで、AIの仕事に必要な詳細を引き継げるか不安が生じた。
- **Hypothesis**：Human View（Notion等）とAI Onboarding Knowledgeを分離し、後者でTaskごとの参照を明示した方がよい。
- **未確認**：表示媒体自体の優劣、分離による改善量、二重管理を避ける具体方式。
- **検証案**：同じ内容から作った表示とTask別の参照案で、必要情報への到達・矛盾検出を比較する。GitHubを正本にする方針と、この仮説の有効性は分けて評価する。

## F-04 — 否定形によるアンカー

- **Finding（懸念）**：不要な概念を「〜ではない」と強く書くことで、逆にAIの注意をその概念へ向ける可能性がある。
- **Hypothesis**：不要な概念はContextから外し、必要な目的・境界を直接書くと理解しやすい。
- **未確認**：表現差による影響と、明示が必要な制約との使い分け。
- **検証案**：同じ要求の二つの表現で範囲逸脱を比較する。承認条件や重要な禁止事項は意味を保つ。

## F-05 — Small IssueとFresh Worker

- **Finding（懸念）**：巨大Taskで複数の設計を連続して行うと、誤解の位置や成果の妥当性を確かめにくい。
- **Hypothesis**：Small Issue + Fresh Workerなら、目的・成果物・受入条件を対応づけ、検証しやすい。
- **未確認**：最適な粒度、引き継ぎ負荷、品質改善量、独立Reviewを含めた総コスト。
- **検証案**：Bootstrapの各Issueで読み込み量、説明の正確さ、Review指摘、修正・引き継ぎ負荷を記録する。認知負荷が大きい場合は分割案を見直す。

## F-06 — Project全体の向きとTask局所入力

- **Finding（懸念）**：Task Contextだけでも局所作業を始められる一方、Project全体の意味・背景・現在地・次の論点を短時間で復元できない可能性が、Project Context導入の検討時に実際に懸念された。
- **Hypothesis**：小さなcanonical Project ContextをGlobal Orientationとして置き、Taskごとに選んだLocal Contextを組み合わせれば、長大な継続ChatとProjectを知らない完全Freshな開始の間を埋められる可能性がある。
- **未確認**：理解時間・正確さ・誤解や重複の増減、適切な最小量、媒体やProject規模による差、維持コスト。
- **検証案**：固定したProject Contextと`START_HERE.md`だけを入口にFresh WorkerがProjectの目的・現在地・未決定事項・Task開始前の確認事項を説明できるかを確認し、指定Input Contextだけの場合と比較する。結果・入力版・閲覧範囲・採点根拠は別のOutcomeに残す。

## F-07 — 実際のFresh ChatにおけるGlobal OrientationとContext選択

- **Finding（単一試行の観察）**：main反映後の`PROJECT_CONTEXT.md`と`START_HERE.md`を入口に、過去のtOS Discussionを渡さない新しいChatが、tOSのPurpose、B-01〜B-12の現在地、B-12とtOS全体完成・v0.1 Freezeの区別、未設計Architecture領域、Task開始前のHuman Gateを説明した。一方で、主要なOpen Questionsに加えてOQ-11も取得した。[Real Fresh Chat Context Test Outcome](../outcomes/project-context-real-chat-test/README.md)を出典とする。
- **Hypothesis**：小さなGlobal OrientationとTask別に選ぶLocal Contextの組合せは、Project全体の理解に必要な情報へ到達させつつ、Repository全体の無条件な全読を避けられる可能性がある。正しい情報を取得できることと、その時点のContextとして必要十分であることは別に評価する必要がある。
- **未確認**：再現性、Model差、入力量と理解品質の関係、最小かつ十分なKnowledge selection、OQ-11のような周辺情報が理解・誤解・効率へ与える影響、比較対象との差、長期の維持コスト。
- **検証案**：固定版・同一質問・明示的な採点基準・複数の独立Fresh Workerを用い、Project Contextのみ、Project Context + `START_HERE.md`、Task別Input Contextなどの条件を比較する。各条件で参照されたファイル、得られた理解、不要または欠落した情報、停止判断をOutcomeとして保存し、仕様変更は別TaskのHuman Reviewで判断する。

## 後続での扱い

検証方法を選ぶ段階で、評価基準・入力版・観察者・実施条件を明示する提案です。B-12の受入テストは引き継ぎの可否を確認するもので、上記すべての仮説の因果を証明するものではありません。結果はOutcomeとして記録し、採用する変更だけをHuman Review後に仕様へ反映します。
