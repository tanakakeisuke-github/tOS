# tOS — Start Here

tOSは、人間・Cloud AI・Local AIが、複数メディアの制作を長期的に協働するための、知識・仕事・承認・学習の共通基盤です。

**現在地：Knowledge Bootstrap / Draft / Human Review待ち。稼働するOS・採用済みOS Version・実装承認はまだありません。**

## 読み順

1. この文書 → [CONSTITUTION](CONSTITUTION.md)。
2. assigned Task / Issueで、目的・範囲・受入条件・Human Approvalを確認。
3. そのTaskが参照するSpecifications / Decisionsだけを読む。
4. 関連するartifacts / codeを、指定された版で読む。
5. 理解・根拠・未決定事項・停止条件を短く説明して、承認範囲内だけ作業する。

**全ファイルを読む必要はありません。** 今回はTask / Issueを作成していません。割当がなければ目的理解までで止まり、作業を自作しないでください。理解のみが依頼された場合は[Purpose](specifications/PURPOSE.md)と[Core Architecture](specifications/CORE_ARCHITECTURE.md)へ進みます。

## 判断の境界

- Greenfieldです。旧Repository / Project / Issue構造を推測・再現・継承せず、目的と原則から再評価します。
- 未決定事項は未決定のまま扱い、承認なしに実装しません。詳細手順の提案も実装許可ではありません。
- GitHub上の承認済みKnowledgeが正本となる方針です。このDraftはまだ承認済みbaselineではありません。
- Knowledgeの読み取り優先順位は **Specification → Decision → Outcome → Transcript**。適用版と承認状態を先に確認し、矛盾は[STOP](protocols/TASK.md)へ。
- 範囲外の発見は[Triage](protocols/TRIAGE.md)へ提案します。Ready前・Done前はHuman Approvalが必要です。
- [HISTORY](bootstrap/HISTORY.md)とTranscriptは必要な調査時だけ参照します。Fresh Workerへの一括投入は行いません。

必要な参照が欠ける場合は推測で埋めず、[未決定事項](bootstrap/OPEN_QUESTIONS.md)を確認して不足を報告してください。文書の状態と構成は[README](README.md)にあります。
