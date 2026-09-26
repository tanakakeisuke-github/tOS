# Project Context — Real Fresh Chat Context Test Outcome

状態：Human Approval済み / Accepted for Merge（[Human Acceptance](HUMAN_ACCEPTANCE.md)）。この記録は、mainへ反映済みのProject Context / Layered Contextを入口に、過去のtOS Discussionを渡さない新しいChatで得られた単一試行の結果である。Project Context / Layered Contextの有効性を証明するものではない。B-01〜B-12、PR #32、既存Outcome、および既存Acceptance evidenceを変更・再採点・上書きしない。

## Purpose

`PROJECT_CONTEXT.md`と`START_HERE.md`を入口にした実際の新しいChatが、GitHub上のKnowledgeだけを根拠として、tOSのProject全体を期待した範囲で説明できたかを、後から条件・回答・限界とともに確認できるOutcomeとして保存する。

このOutcomeは新しい機能、仕様、TaskのReady、Context Compilerの実装を提案または確定しない。

## Relationship to Existing Outcomes

既存の[Fresh Worker Test](../project-context-fresh-worker/README.md)および[Revision Fresh Worker Consistency Outcome](../project-context-fresh-worker-revision/README.md)は、PR #32のProposal / Revision段階で行われた別の確認である。本記録は、PR #32のmain反映後に実際の新Chatで行った単一試行を別の条件・結果として保存する。

Project Context / Layered Context自体の承認範囲は、[Project Context Human Acceptance](../project-context-human-acceptance/README.md)を正本とする。

## Recorded Conditions

| 項目 | 実施内容 |
|---|---|
| 対象版 | main、`a7c8f16e96045f03dbf35adb0dd622b8964c6d1e`（`docs: propose layered project context model (#32)`） |
| Worker | 過去のtOS Discussionを渡さない新しいChat |
| 初期入口 | Repositoryとmainを指定し、`PROJECT_CONTEXT.md`、`START_HERE.md`を最初に確認するよう依頼 |
| 根拠の制約 | GitHubに記載された情報だけを根拠とし、過去の会話・記憶を前提にしないよう依頼 |
| 求めた説明 | tOSとは何か、存在理由、現在地、未設計Architecture領域、Open Questions、次の判断、Task開始前の確認事項 |
| 記録方法 | このOutcomeはFresh Chatから報告された回答本文を保存する。逐語のToolログ、完全なTool isolationの証拠、独立採点の記録は取得していない。 |

## Recorded Fresh Chat Response

以下はFresh Chatから得られた回答である。意味を変更せず、項目構造だけをOutcome内の記録として保持する。

> tOSは、人間とAIがSessionをまたいで制作を継続するための、AI-nativeな制作OSを目指すKnowledge中心のRepositoryです。目的・意思決定・作業の受け渡し・検証結果をGitHub上に残し、制作経験を次の制作と制作環境の改善へつなげることを狙っています。
>
> 現在地：
>
> - Bootstrap KnowledgeのB-01〜B-12は人間の受入承認済みです。
> - B-12はR5のP/M/U全ケース合格後、Done承認済みです。
> - ただし、これはBootstrap Knowledgeの受入完了であり、tOS全体の完成、v0.1 Freeze、次の実制作TaskがReadyであることを意味しません。
> - 現在、Project-wide Milestoneは未承認です。
>
> 今後設計が必要な主なArchitecture領域：
>
> - Studio Template Model
> - Organization / Cross-role Collaboration
> - Production Planning
> - Project Bootstrap
> - Creative Project / Production
>
> 現在の主要なOpen Questions：
>
> - OQ-01：tOS v0.1の実際の範囲と完成条件
> - OQ-07：Project Bootstrapの入力・生成物・承認・自動化の範囲
> - OQ-08：Context CompilerとHuman Viewの実装時期・評価方法
> - OQ-11：旧Draft PR #1を閉じるかどうか
>
> 次に判断すべきこと：
>
> 次の全体テーマや優先順位は未決定です。人間が個別の小さなTaskを選び、目的・範囲・入力・受入条件・依存・停止点を具体化して、Ready承認する必要があります。OQ-01を必ず次に決めるという順序までは、文書上で確定していません。
>
> 新しいTaskの開始前に確認すること：
>
> - 担当Issue
> - Ready承認記録
> - 基準版と指定Input Contextの出所・適用版・承認状態
> - 目的、範囲、受入条件、依存、停止点
>
> これらが不足・矛盾・未承認の場合は、推測で補わず、作業を開始しません。Issue作成、ラベル変更、PRの作成・マージ、CI成功、AIの自己確認はReady承認の代替ではありません。
>
> 情報が不足していること：
>
> - tOS v0.1の具体的な範囲・完成条件・Freeze条件
> - 次に選ぶTask、その優先順位、Ready承認
> - Studio Template、Cross-role Collaboration、Production Planning、Project Bootstrapの具体設計
> - Context Compiler / Human Viewの実装・評価方針

## Files Reported as Read

- `PROJECT_CONTEXT.md`
- `START_HERE.md`
- `specifications/PURPOSE.md`
- `CONSTITUTION.md`
- `bootstrap/ISSUE_MAP.md`
- `specifications/WORK_MODEL.md`
- `protocols/FRESH_CONTEXT.md`

## Positive Observations

- 過去の長大なtOS Discussionを渡さなくても、GitHubからtOSのPurposeを説明できた。
- B-01〜B-12という現在地を説明できた。
- B-12完了とtOS全体完成を混同しなかった。
- B-12完了とv0.1 Freezeを混同しなかった。
- 未設計Architecture領域を認識できた。
- 次Taskが自動的にReadyではないことを認識できた。
- Human GateとReady条件を維持できた。
- 情報不足を推測で補完しなかった。
- Repository全体を無条件に全読せず、入口から必要なKnowledgeを辿った。

## Interesting Observation — Context Selection

Fresh Chatは主要Open QuestionsであるOQ-01、OQ-07、OQ-08に加えて、`bootstrap/ISSUE_MAP.md`に残るOQ-11（旧Draft PR #1を閉じるか）も取得した。

この取得自体は誤りではない。しかし、正しい情報であることと、今回のProject理解のContextとして必要であることは同じではない可能性がある。この観察は、将来のContext CompilerまたはContext selectionを検討する際のFinding候補であり、OQ-11の扱い、Contextの選択規則、またはSpecificationをこのOutcomeだけで変更するものではない。

## Interpretation and Boundaries

この単一試行で確認できたのは、過去Conversationを渡していない実際の新Chatが、`PROJECT_CONTEXT.md`と`START_HERE.md`を入口にしたとき、期待していたProject理解を説明できたという初期の実運用結果である。

この結果を「Project Context / Layered Contextの有効性が証明された」とは扱わない。Project ContextはGlobal Orientationであり、Purpose、Constitution、Specification、Decision、Outcome、担当Issue、TaskのReady条件を置き換えない。[Project Context Model](../../specifications/PROJECT_CONTEXT_MODEL.md)および[Knowledge Architecture](../../specifications/KNOWLEDGE_ARCHITECTURE.md)の既存の境界を変更しない。

## Limitations and Unresolved Questions

- 単一試行であり、再現性、理解品質のばらつき、比較対象との差は未検証である。
- Model差、実行環境、Context量、質問表現、Repository更新による影響は評価していない。
- 逐語のToolログ、完全なTool isolation、独立Reviewerによる採点は取得していない。
- 長期運用時の維持コスト、最適なKnowledge selection、Context最小量、誤解や不要情報の混入を測定していない。
- OQ-11の取得が有益・不要・有害のいずれか、またその選択を誰がどの基準で行うかは未決定である。

次に何を設計・実装・評価するかは、このOutcomeから自動的には決まらない。後続のTaskを始める場合は、担当Issueで目的・範囲・入力・受入条件・依存・停止点を定め、個別のReady承認を得る。
