# B-12 Retry R2 — 中断記録

状態：**未完了・合否未判定**。前回の不合格を置き換えない。

ユーザーの「リトライしてみましよう」を受け、[実施前記録](https://github.com/tanakakeisuke-github/tOS/issues/25#issuecomment-5818046953)を残した。Knowledge版 `5f15fd73800c23b04875ef73261367e0df7aa81c`、20文書、CASE_TASK、採点基準を維持し、Ready参照へ今回の再試行承認を追記した。Knowledge改訂後の正式受入試験ではなく、同じ版での再試行を準備した。

## 実行方法と事前確認

保存済みCodex設定の `gpt-6-astra` / `medium` を明示指定するCodex CLI 0.155.0-alpha.9を使用し、ケースごとに新しいSessionを起動する方法を用意した。JSONLで操作記録を取得し、入力ファイルのSHA-256と起動引数をローカルに保存した。公式の[非対話実行](https://learn.chatgpt.com/docs/non-interactive-mode)と[権限設定](https://learn.chatgpt.com/docs/config-file/config-reference)を参照した。

隔離の事前確認では、許可外のダミーファイルも読めた。明示的な読取禁止を追加した後、Agentは読取を拒否したが、直接のsandbox確認では読めたため、技術的強制は実証できていない。設定の存在を隔離の成功として扱わない。

## 中断と実際の状態

P/M/Uの起動を要求した際、Pは自動承認審査により拒否された。理由は、非公開Repository資料を選択した外部モデルサービスへ送ることについて、送信資料と送信先を明示したユーザー承認が必要というものだった。

同時に起動したM/Uはすでに資料の読取を開始していた。拒否確認後、両プロセスを終了シグナルで停止し、終了コード `-15` を確認した。停止前に一部の資料はモデルへ渡っており、送信前に全件止められたとは扱わない。

| ケース | 確認した状態 |
|---|---|
| P | 起動拒否。受験回答なし。 |
| M | 入口・Task・Ready・模擬Ready・Purpose・Constitution・Core Architecture等の閲覧操作を記録。停止済み。最終回答なし。 |
| U | 入口・Task・Ready・Purpose・Constitutionの閲覧操作を記録。停止済み。最終回答なし。 |

三ケースとも完了イベントはなく、採点・独立採点Reviewは未実施。R2の得点も合格も推定しない。ローカル記録は `/private/tmp/tos-b12-retry/logs/` にあり、一時領域なので永続保存の保証はない。本書に中断の事実と判断を残す。

## 再開条件

入力パッケージ内のtOS文書と設問をOpenAIのCodexモデル `gpt-6-astra` へ送信することについて、ユーザーの明示承認を得る。再開時は中断Sessionを使わず、新規Sessionで実施する。読取隔離の未解決は別途解消・確認が必要であり、回答の成功だけで正式受入合格にはしない。Issue #25とPR #26は開いたまま、B-12 Doneは未承認。
