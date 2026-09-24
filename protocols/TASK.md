# Task Protocol — 選択肢を着手判断できる案へ整える

状態：B-08としてHuman Review承認済み（[PR #18](https://github.com/tanakakeisuke-github/tOS/pull/18)）。Task、Issue、状態とHuman Gateの定義は[Work Model](../specifications/WORK_MODEL.md)を参照する。

## 入力

Discussionで明示した問い・選択肢・出所、選んで検討する成果案、既承認の制約、依存、未決定事項。Discussion以外から依頼された場合も、同じ情報を問いと選択肢として整理してから扱う。

## 担当・手順

Task案を整える担当Actorが記述し、Triage担当へ渡す。Roleと担当Actorの割当は[Actor Model](../specifications/ACTOR_MODEL.md#割当と交代)に従う。Readyを判断するのは人間である。

1. **一つの小さな目的**に絞り、期待成果と対象外を明示する。目的、成果、検証、承認の境界が異なるなら依存付きの別Task案へ**SPLIT**する。
2. 各案に目的、範囲、入力の所在・版・出所・承認状態、成果、受入条件、依存、担当Role／Actor候補、停止点を記す。受入条件はReviewerが成果と照合できる形にし、未実施の検証を合格扱いしない。入力選択と正本は[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md#taskごとの入力とopen-question)に従う。
3. 欠けた条件、矛盾、承認範囲外の判断を列挙し、影響する案を**STOP**して再開条件を示す。妨げない未知は判断者と次の判断点を付けて残す。
4. 案と元の選択肢への参照を[Triage Protocol](TRIAGE.md)へ渡す。TriageがTask化を選んだ後も、担当Issueには条件と承認状態への参照を残し、**Ready待ち**で人間の着手判断を待つ。人間は対象Taskと適用版、目的・範囲・入力・受入条件・依存を確認して明示的に承認する。Issue作成、ラベル変更、AI Review、PR、CI結果はReady承認にならない。

## 出力

一つの目的ごとのTask案と依存、Triageに渡す判断事項、Ready前Human Gateに必要な条件。承認・却下の理由と記録先は[Work Model](../specifications/WORK_MODEL.md#記録と照合例)および[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md#正本と分類)に従い、担当IssueまたはReviewの一方を正本として参照する。

## 停止条件

目的・入力・受入条件を定められない案、依存の承認が不明な案、承認済み仕様と競合する案はReadyへ進めない。人間のReady承認がない間は実行しない。承認後に目的・範囲・入力・受入条件を変えるなら、影響する作業を止めてReady前Human Gateへ戻す。

## 照合例

「調査して画面を刷新する」は調査結果と制作成果、受入条件が異なる。まず「対象と評価条件を整理する」案と「承認された評価結果から画面案を作る」案に分け、後者を前者へ依存させる。各案は別にTriageし、各々のReady承認までは着手しない。
