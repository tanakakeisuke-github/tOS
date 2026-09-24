# 次のSessionへの引き継ぎ — B-12契約修正

状態：修正提案のHuman Review待ち。これは担当者向けの索引であり、受験者へ渡す入力ではない。

## 目的と現在地

目的は、tOSの原則とB-12の仕事・試験の渡し方を整合させること。[Issue #27](https://github.com/tanakakeisuke-github/tOS/issues/27)が修正範囲・判断の正本。[Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)は受入試験、[PR #26](https://github.com/tanakakeisuke-github/tOS/pull/26)は過去の試行結果である。承認・merge状態は再開時にGitHubで確認する。

## 最初に読むもの

1. Issue #27の最新状態、対応PRの対象commitとHuman Review記録。
2. [Purpose](../specifications/PURPOSE.md)「何のためにあるか」、[Constitution](../CONSTITUTION.md)「変わりにくい原則」。
3. [今回の整合レビュー](PHILOSOPHY_REVIEW.md)、[次版Acceptance Plan](ACCEPTANCE_PLAN.md)。担当範囲に必要なケース本文だけを参照する。

旧チャット全文、History、過去の原回答・操作ログは標準入力に含めない。理由調査が必要な担当だけが、上記Issue/PRから対象箇所を追加で読む。新しい受験Workerは、この引き継ぎや整合レビュー、採点者向け計画、過去の回答を受け取らず、承認されたケース専用入力から始める。

## 残っている仕事と再開条件

- **改訂のHuman Review・採用・main反映**：本書の存在を承認に読み替えない。
- **試験環境の成立確認**：別の小Taskとして環境・モデル設定・記録・読取制約を確認する。未検証の隔離を達成済みと扱わない。
- **次系列の試験**：承認済み改訂版のcommit、完成したケース入力、モデル設定、判断者、Ready記録を担当Issueで固定してから、新規Sessionで実施する。今回の修正指示を次試験のReadyへ流用しない。

前の会話を読まないと上記の範囲・状態・再開条件を説明できない場合は、足りない引き継ぎ情報をIssueへ記録して補完する。新しいTaskを開始したことや、この引き継ぎの作成をDoneの根拠にしない。
