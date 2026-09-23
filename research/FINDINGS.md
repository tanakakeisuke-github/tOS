# tOS — Findings

状態：Draft。元議論での報告と、そこからの設計仮説を区別する。定量評価・比較実験は未実施。

## F-01 — 長期ChatのContext混在への懸念

**Observation**：AI Game Studioを検討する中で、長期ChatによるAI精度低下や前提混在への懸念が設計課題となった。これは[依頼で明示された経緯](../bootstrap/SOURCES.md)であり、原因や低下量を測定した結果ではない。

**Finding候補**：仕事の継続性を一つの会話に依存させると、必要な現行知識と古い探索案を分離しにくい。

**Hypothesis**：Fresh Contextと明示的なKnowledge優先順位により、誤った前提の混入を減らせる。

**Validate案**：同じ限定課題で、目的の理解、仕様参照、未決定の識別、範囲外実行の有無を比較する。情報欠落と人間の準備負担も評価する。結果はまだない。

## F-02 — 新しいWorkerへの引継ぎ不安

**Observation**：元議論でユーザーは、新しい作業側が議論の詳細を理解しているか不安を表明した。その後Greenfieldでの再記述、GitHubへのKnowledge移行を求めた。参照した会話には画像に対する発言も含まれるが、本Bootstrapでは画像自体を評価していない。

**Finding候補**：文書を渡すだけでは理解を確認できない。引継ぎの入口、読む順序、判断根拠、理解の出力を含む受入が必要。

**Hypothesis**：Taskごとに選択されたGitHub KnowledgeとFresh Workerの説明テストを組み合わせると、誤解を発見しやすくなる。

**Validate案**：[Acceptance](../bootstrap/ACCEPTANCE.md)で、Repositoryのみからの理解を確認する。GitHubへ移すだけで精度が上がるとは断定しない。媒体による差と、情報構造による差を分けて評価する。

## F-03 — 不要な具体例が判断を引く懸念

**Observation**：元議論でユーザーは、特定対象への言及が否定形でも後続の判断を引くという経験上の懸念を述べ、Bootstrapから除くよう求めた。

**Finding候補**：現在の目的に不要な固有の具体例は、禁止例として繰り返すより、必要な抽象概念だけ残した方がContext境界を保ちやすい。

**Hypothesis**：媒体共通の目的とレイヤーを正方向で記述すれば、過去構造の再現を減らせる。

**Validate案**：Fresh Workerの説明に未指定の作品・組織・Issue構造が混ざらないかを確認する。今回は自己レビューのみで、独立した理解テストは未実施。

## Learning Loopへ戻す

これらの仮説は、OS Improvement Proposal → Prototype → Validate → Next Versionの候補になる。原則として採用されたFresh Contextと、その効果が実証されたかは別の問いである。新しい検証を行う場合はTriageとHuman Approvalを経る。
