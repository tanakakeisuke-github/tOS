# 次のチャットへの引き継ぎ — B-12環境確認から再開

更新：2026-09-25。調整・環境担当向けの入口。受験Workerへ配布する資料ではない。

## 対象と現在地

正本は [tanakakeisuke-github/tOS](https://github.com/tanakakeisuke-github/tOS)。正式名称はtOS。Greenfieldの媒体非依存Coreを維持する。

- Knowledge保存とB-01〜B-11は承認・main反映済み。
- B-12の契約・哲学の整合修正は [PR #28](https://github.com/tanakakeisuke-github/tOS/pull/28) でmainへ反映済み。[Issue #27](https://github.com/tanakakeisuke-github/tOS/issues/27)は完了。
- 残タスクは [Issue #25](https://github.com/tanakakeisuke-github/tOS/issues/25)：B-12 Fresh Worker受入試験。
- [PR #26](https://github.com/tanakakeisuke-github/tOS/pull/26) はOPEN/Draft。旧試験結果と追加の環境検証・本引き継ぎを保存している。B-12 Doneは未承認。
- **改訂後P/M/Uは未実施。現在は環境未成立。人間の確認だけを待つ状態ではなく、環境確認の作業が残っている。**

本チャットの最終依頼は次チャットへ向けた引き継ぎ整備。ここで新たな受験・merge・制作開始は行っていない。

## 再開する場所と読む順番

1. Issue #25とPR #26の最新状態・コメント・headを確認する。
2. **PR #26のhead branch `docs/b12-fresh-worker-acceptance` にある本書を使う。mainだけでは最新の環境証拠を取得できない。** mainのIssue Mapには古い進捗表示が残るため、実際の状態はIssue/PRと照合する。
3. [Purpose](../specifications/PURPOSE.md) → [Constitution](../CONSTITUTION.md) → [承認済みAcceptance Plan](ACCEPTANCE_PLAN.md) の開始条件・記録要件を読む。
4. [環境確認の総括](../outcomes/B12_ENVIRONMENT_CHECK.md) → [専用Readerの直近検証](../outcomes/b12-environment/app-server/README.md) を読む。必要な原記録だけ追加参照する。

承認済みKnowledge・試験契約の基準はmain commit `7ab8b092544f6f00b8ca8d791ed6473cfef6cd43`。環境証拠の直近保存commitは `51628ab36741b35a9ce871494ffcb686b997c483`。この引き継ぎの更新はその後のPR #26上にある。記録ブランチのheadと受験用Knowledge版を混同しない。

旧チャット全文を再投入しない。哲学修正の理由が必要なときだけ [整合レビュー](PHILOSOPHY_REVIEW.md) を読む。旧回答・採点・本書・採点者用計画は受験Workerへ渡さない。

## 確認済みと未確認

| 項目 | 確認結果 |
|---|---|
| 実行環境 | Codex CLI `0.155.0-alpha.9`、app-server、新規ephemeral session。ランタイム応答は `gpt-6-astra` / `medium`。 |
| 選択環境・自動読込 | `environments: []`、workspace rootsとinstructionSourcesは応答上空。 |
| 専用Reader | 固定IDからダミー本文を返す。許可IDは成功、範囲外の相対/絶対パス指定は拒否。要求・返却を調整側ログで確認済み。 |
| 残る取得経路 | Workerの報告にはSkill取得・他Agentへの委譲が残る。これらのアクセス制限・委譲先への制約継承は未確認。 |
| ログ | Reader要求と返却、実行設定応答を保存。サーバー内部の全ツール操作を網羅する監査は未成立。 |
| 本試験 | 修正版では未実施・未採点。環境の問題をKnowledge不合格と扱わない。 |

専用Readerが動くことと、全経路の隔離が成立することを区別する。ツールの不存在や全操作の遵守をWorkerの自己申告だけで認定しない。

既に試した経路：Codex custom profileはダミー禁止ファイルも読めた。OSの限定ディレクトリ制限は部分成功、全体読取制限は起動失敗。app-serverのcode-mode hostまで止めると必要Readerも動かなかった。同条件の再試行だけを繰り返さず、変える条件・得たい証拠を明確にする。

## 次の担当の小さな目的

**最初の目的は「許可資料を読め、禁止資料を全取得経路から参照できず、その証拠を保存できる試験環境を成立させること」。** 合格回答を得ることを先に目指さない。

1. 残るSkill・委譲等の取得経路を制限・監査できる実効構成を確認する。ダミー資料で許可/拒否・モデル設定・記録取得を検証する。
2. 成立した場合、Knowledge/設問版、P/M/Uごとの入力一覧・ハッシュ、モデル設定、担当・採点者、実際のReady承認をIssue #25へ固定する。条件はAcceptance Planを参照する。
3. Readyを確認後、ケースごとに独立したFresh SessionでP/M/Uを実施する。Pは理解説明、Mは不足資料への対応、Uは未承認Taskへの対応。基準・閾値・初期入力を回答後に変えない。
4. 独立Reviewerが原回答・入力・操作記録・公開基準を照合し、結果をPR #26から辿れるように保存する。人間が受入を判断する。

環境が検証不能なら、未達の条件と具体的な選択肢・影響を人間へ返す。別Runtimeや条件変更の案は既存方針と分け、採用済みと扱わない。B-12完了後もBootstrap Knowledge受入とtOS本体完成・Freezeは別判断である。

## 承認と履歴の扱い

試験用tOS資料・設問をOpenAI Codex `gpt-6-astra`へ送ることは、送信先・内容を説明後のユーザー回答「codexにしてもらうか」を受け、[Issue #25のR3再開前記録](https://github.com/tanakakeisuke-github/tOS/issues/25#issuecomment-5818091607)へ保存済み。同一範囲の送信承認を重ねて求める必要はない。ただし、改訂後の実試験条件・版を確定したReadyとは区別する。別の送信先や範囲へ一般化しない。

初回とR3は受入条件未達、R2は中断。旧結果は保存し、修正版の基準で遡及再採点しない。直近の環境追加記録は自己確認済み、独立Reviewは未実施。旧Draft PR #1は履歴上の旧案として開いたまま、閉じる判断は未決定。

## ローカル補助情報

前担当の作業cloneは `/private/tmp/tos-b07-20260925`。利用するならremote・branch・未保存変更を先に確認する。消えている場合はGitHubのPR #26から復元できる。ChatGPT同期ディレクトリの `sources/` は読取専用。

`/private/tmp/tos-b12-r4/` に準備したP/M/U入力が残っていても、Ready未確定の作業途中資料であり使用許可済みfixtureではない。承認済みテンプレートから改めて版と入力を固定する。再開に一時ディレクトリの存在を必須としない。
