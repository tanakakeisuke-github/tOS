# Review Protocol — 成果を照合しHuman Done判断へ渡す

状態：B-09としてHuman Review承認済み（[PR #20](https://github.com/tanakakeisuke-github/tOS/pull/20)）。本手順は[Constitution](../CONSTITUTION.md)のDone前Human Gateにつなぐ。Reviewerの分離は[Session Model](../specifications/SESSION_MODEL.md#sessionと担当の原則)、ActorとHumanの責任は[Actor Model](../specifications/ACTOR_MODEL.md)を参照する。

## 入力

Ready承認済みの担当Issue、適用版・指定入力・受入条件・停止点、Draft PRまたは提出成果、[Handoff](HANDOFF.md)の成果版・確認結果・未実施の検証・残課題。

## 担当・手順

作成Workerと分離したReviewerが、可能な限り新しいSessionで確認する。ReviewerはWorkerの説明だけでなく指定入力と成果を照合する。完了判断は人間が行う。

1. Review対象の成果版、Taskの範囲とReady承認、指定入力の適用版を確認する。Review中に成果または入力が変われば、影響する確認を新しい版でやり直す。
2. 受入条件ごとに成果と証拠を独立に照合し、合致・不一致・未確認を区別する。実施した検証の条件と結果を確認し、必要な検証が未実施なら合格としない。問題、残課題、Unknown、承認範囲外の変更を明示する。
3. Review結果を根拠と対象版付きで記録する。差戻しなら修正箇所、必要な検証、担当、再提出条件を示す。Workerは引き継ぎを更新して再作業し、Reviewerは変更範囲と影響する受入条件を再確認する。目的・範囲・入力・受入条件が変わるならReady前Human Gateへ戻す。
4. 別ReviewerやFresh Sessionを用意できない例外は、理由、対象範囲、引き継いだ入力と承認、独立性への影響、判断した人間と時点を担当IssueまたはReviewに残す。例外の可否・追加確認は人間が判断し、例外記録だけで必要な検証やDone承認を置き換えない。
5. Review結果、未実施の検証、例外、残課題を人間に渡す。人間が成果・Review・必要な検証・未解決事項を確認し、明示的にDoneを承認した記録がある場合に限りTaskを完了扱いする。AI Review、CI、PRマージ、IssueクローズからDoneを推定しない。

## 出力

受入条件ごとのReview結果と証拠、差戻し・再提出条件、例外の判断、Human Reviewへ渡す未解決事項。Done承認または差戻しの理由と記録先は[Knowledge Architecture](../specifications/KNOWLEDGE_ARCHITECTURE.md#正本と分類)に従う。

## 停止条件

受入条件や対象版が不明、証拠が足りない、必要な検証が未実施、独立性の例外が未判断なら、合格やDoneへ進めない。差戻し後は再提出と必要な再Reviewまで止める。人間の明示的なDone承認がなければ、Reviewが合格でも完了扱いしない。

## 照合例（架空）

- **合格へ進む例**：Ready承認された評価項目一覧の版AをWorkerが提出し、受入条件ごとの確認と必要な検証の結果を渡す。別SessionのReviewerが指定入力と版Aを照合して合致を記録する。人間が成果、Review、検証、残課題を確認して明示的にDone承認した後に完了とする。
- **検証未実施の例**：同じ一覧の提出時に必要な測定確認が未実施と記録されている。Reviewerはその受入条件を未確認として差戻し、実施結果または受入条件変更の人間判断を求める。確認を終えて再Reviewを受けるまでDoneへ進めない。
