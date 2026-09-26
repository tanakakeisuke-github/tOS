# Project Context — Fresh Worker Acceptance Plan

状態：Proposalに対する新規の受入計画。B-12の契約・結果・Acceptance evidenceを変更または上書きしない。実施には、この計画とは別のTask、固定版、Ready承認、独立したFresh WorkerとReviewerを必要とする。

## Objective

元の会話を知らないFresh Workerが、GitHub上の`PROJECT_CONTEXT.md`と`START_HERE.md`を入口に、参照先を使って次を説明できるか確認する。

1. tOSとは何か。
2. なぜ存在するか。
3. 現在どこまで進んでいるか。
4. 次に何が未設計または未決定か。
5. Taskを開始する前に何を確認するか。

これはProject Contextの説明・到達性を確認する試験であり、tOS全体の完成、v0.1 Freeze、実制作TaskのReady、B-12の再採点を意味しない。

## Fixed Inputs and Method

- 人間がReady承認したcommitを固定し、`PROJECT_CONTEXT.md`と`START_HERE.md`を初期入口として渡す。
- WorkerにはGitHub上の固定commitと、二つの入口から参照される資料だけを使わせる。旧Chat、採点者専用資料、未公開のローカル文書は入力にしない。
- Workerは上の五問への回答と、実際に読んだGitHub資料・commitを提出する。
- 独立したReviewerが、固定入力、回答、閲覧記録、正本への参照、状態表現の正確さを照合する。必要なら人間が最終的に受入可否を判断する。

## Acceptance Criteria

回答は少なくとも次を満たす。

- tOSの目的をPurposeへ結び、将来像と実装済み状態を区別する。
- B-01〜B-12が受入承認済みであり、B-12 R5がDone承認済みであることを示す。同時に、これがtOS全体の完成・v0.1 Freeze・実制作TaskのReadyではないと区別する。
- OQ-01、OQ-07、OQ-08、または固定版でそれらを置き換えた未決定事項の正本を示す。
- Open Questionsだけでなく、Studio Template Model、Organization / Cross-role Collaboration、Production Planning、Project Bootstrap等が未設計のArchitecture領域であり、採用済みSpecificationやReady Taskではないと説明する。
- Task前に、担当Issue、Ready承認、基準版、指定Input Context、目的、範囲、受入条件、依存、停止点を確認すると説明する。
- 入力不足・矛盾・承認範囲外の判断では停止して人間に確認することを示す。
- Project ContextをPurpose、Constitution、仕様、Decision、Outcome、担当Issueの代替や新たな正本として扱わない。

## Evidence to Record

実施時は、固定commit、Ready承認、Workerへの初期指示、許可された閲覧範囲、実際の閲覧ログ、原回答、Workerの自己確認、Reviewerの採点と引用根拠、未実施・汚染・限界、人間の受入判断を新しいOutcomeとして保存する。B-12の保存済み原回答・Review・Acceptance evidenceは変更しない。

## Current Execution Status

候補commit `3367aaab1ac9c81dd74d2b419c786cd4897fbd53` に対して、元会話を渡さない独立Fresh WorkerがGitHub上のbranchをcloneして実行した。回答・閲覧資料・自己レビューの結果は[実行記録](../outcomes/project-context-fresh-worker/README.md)に保存する。

この初回実行では期待した理解が得られたが、Project Contextの有効性を証明したものではない。Workerの閲覧制限は実行指示とWorkerの報告に基づくため、Toolの完全な隔離ログや人間の最終受入は含まれない。Revision後の質問4を含む内容整合確認は別記録へ保存する。Proposalの正式受入が必要な場合は、人間がこの限界を確認し、必要なら固定版・隔離・独立Reviewerを含む専用Taskで再実施する。
