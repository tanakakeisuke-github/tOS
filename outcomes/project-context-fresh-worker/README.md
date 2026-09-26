# Project Context — Fresh Worker Test Outcome

状態：実施済み / この結果自体はHuman Acceptanceではない。B-12の契約・結果・Acceptance evidenceを変更または上書きしない。

## Purpose

元の会話を知らないFresh Workerが、`PROJECT_CONTEXT.md`と`START_HERE.md`を入口にGitHub上の資料だけから、tOSの目的・現在地・未決定事項・Task開始前の確認事項を説明できるかを確認する。

## Fixed Conditions

| 項目 | 実施内容 |
|---|---|
| 対象commit | `3367aaab1ac9c81dd74d2b419c786cd4897fbd53` (`docs/project-context-model`) |
| Worker | 元会話を渡さない独立Fresh Worker / 別Session |
| 初期入口 | `PROJECT_CONTEXT.md`、`START_HERE.md` |
| 参照範囲 | GitHubからcloneした対象branch。実行指示で既存ローカルcheckoutや会話の参照を禁止 |
| 成果 | 五問への回答と、読んだRepository内ファイルの一覧 |

このcommitはProposal branch上の候補であり、main反映やProposalのHuman Acceptanceを意味しない。

## Raw Worker Response

### 1. tOSとは何か

人間とAIが作品制作をSessionをまたいで継続するための、AI-nativeな制作OSの構想・知識基盤である。目的、判断理由、作業の受け渡し、検証結果をGitHub上で残し、次の制作や制作環境の改善へつなげる。

### 2. なぜ存在するか

長い会話や単発のAI Sessionだけに判断・経緯を残すと、次の担当者が目的や根拠を復元できないためである。媒体や実行技術が変わっても、知識・承認・作業境界を引き継げることを目指す。

### 3. 現在どこまで進んでいるか

Bootstrap KnowledgeのB-01〜B-12は人間に受入承認されている。B-12はR5でP/M/Uの全ケースが合格し、人間がDone、PR #26のマージ、Issue #25のクローズを承認済みである。ただし、これはFresh Workerが知識だけで説明・停止判断をできるかのBootstrap受入であり、tOS全体の完成、v0.1 Freeze、実制作TaskのReadyを意味しない。

### 4. 次に未設計・未決定なこと

OQ-01（tOS v0.1の実際の範囲と完成条件）、OQ-07（Project Bootstrapの入力・生成物・承認・自動化範囲）、OQ-08（Context CompilerとHuman Viewの実装時期・評価方法）が未決定である。Project Context ModelもHuman Review待ちの提案段階であり、媒体別Studio Templateや具体的なRuntime・保存形式・Automationの選定／実証は確定していない。

### 5. Task開始前に何を確認するか

担当Issue、対象Taskへの人間のReady承認記録、基準commit、指定Input Contextを確認する。そのうえで、目的・範囲・受入条件・依存関係・停止点、各入力の出所・適用版・承認状態を照合する。不足・矛盾・未承認の判断があれば影響範囲を止め、人間の判断を待つ。Issue、PR、Readyラベルの存在だけでは着手しない。

## Files Reported as Read

- `PROJECT_CONTEXT.md`
- `START_HERE.md`
- `CONSTITUTION.md`
- `specifications/PURPOSE.md`
- `specifications/CORE_ARCHITECTURE.md`
- `specifications/KNOWLEDGE_ARCHITECTURE.md`
- `specifications/WORK_MODEL.md`
- `specifications/PROJECT_CONTEXT_MODEL.md`
- `protocols/FRESH_CONTEXT.md`
- `bootstrap/ISSUE_MAP.md`
- `outcomes/BOOTSTRAP_ACCEPTANCE.md`
- `outcomes/b12-r5/README.md`
- `outcomes/b12-r5/HUMAN_ACCEPTANCE.md`

## Review Against the Plan

| Criterion | Result | Evidence |
|---|---|---|
| tOSの目的と将来像・実装状態を区別する | Pass | 回答1・2でPurposeとKnowledge継続を説明し、回答3でBootstrap受入をtOS全体完成と区別した。 |
| B-12完了を正しく説明する | Pass | 回答3でR5、Done、PR #26、Issue #25を示した。 |
| 未決定事項の正本へ到達する | Pass | 回答4でOQ-01、OQ-07、OQ-08を示した。 |
| Task前の確認・停止条件を説明する | Pass | 回答5でReady、版、Input Context、受入条件、矛盾時の停止を示した。 |
| Project Contextを正本やTask条件の代替にしない | Pass | 回答5で担当Issue・Ready・指定Input Contextの照合を示した。 |

## Limitations and Next Decision

Workerは実行指示に従いGitHub cloneだけを使ったと報告したが、完全なTool隔離ログは取得していない。このため、本記録はProject Contextの入口としての説明到達性を確認するOutcomeであり、隔離保証を含む厳格な受入試験やHuman Acceptanceではない。Human Reviewでは、この限界を受け入れるか、固定版・隔離・独立Reviewerを備えた再試験を求めるかを判断する。
