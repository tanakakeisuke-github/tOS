# B-12 R4 — 実試験条件・Ready判断用

**状態：入力と条件の提案を固定。Human Ready待ち。P/M/Uは未実施・未採点。** ユーザーのB-12再開依頼により環境確認・準備を行ったが、以下の具体的条件への実Readyは推定しない。

## 人間に求める判断

下記の入力・範囲・実行設定・環境証拠と限界により、P/M/Uの説明・診断試験を開始してよいか。了承後、承認者・実際の発言・時点・対象Task・範囲・適用版・理由・manifest hashをIssue #25とREADY記録へ保存し、その記録を各ケースに配布する。PR #28への承認や旧試験のReadyを今回へ流用しない。

## 固定した条件

| 項目 | 条件 |
|---|---|
| 対象 | https://github.com/tanakakeisuke-github/tOS/issues/25、改訂後系列R4 |
| Knowledge/設問/計画の基準 | `7ab8b092544f6f00b8ca8d791ed6473cfef6cd43`、PR #28で承認・main反映済み |
| Actor / Agent | 互いの回答・旧会話を引き継がないCloud AI / Codex、新規ephemeral Sessionをケースごとに作る |
| Model / 設定 | `gpt-6-astra` / `medium`、代替禁止。Runtime応答を照合する |
| Runtime | Codex CLI `0.155.0-alpha.9` app-server。environmentなし、Agent委譲無効、標準SkillをSKILL.md単位で無効化 |
| 初期入力 | 各ケースのSTART_HERE.md、CASE_TASK.md、実際のREADY.mdの3文書 |
| 追加資料 | 以下manifestの文書だけ。固定ID Readerで必要な資料を取得する |
| 保存 | 初期入力、要求設定/実行応答、文書hash、追加取得とTool操作、原回答・自己確認を系列ごとに保存 |
| 採点者 | 受験Session・作成担当から分離したFresh Reviewer。原回答・入力・操作記録と公開基準を照合。独立ReviewをHuman Doneの代用にしない |
| 停止 | 未承認、設定差異、入力/版不整合、未知の取得経路、自動案内の再注入、汚染、実施不能は停止・記録。結果はDraft PR #26でHuman受入待ち |

受験者には本README、Acceptance Plan、旧結果、環境報告、Reviewer用情報、他ケースを配布しない。manifestを読むのは調整側のみ。受験者が指定したパスをファイルとして開くことはなく、manifestとhashを検証済みの文字列だけを返す。

## ケースと入力hash

| ケース | 内容・合格条件 | Knowledge文書 + CASE_TASK | manifest.json SHA-256 |
|---|---|---|---|
| P | 700字以内の説明、6観点で10/12以上、(3)(4)(5)各2点。本文・出典・自己確認 | 9 + 1 | `7728a7b81c8d9a035d8fb3fb615eaf56e4472245df09b7351bd6ad4e29b92619` |
| M | 架空Taskの着手可否診断。公開5項目すべてと範囲遵守 | 6 + 1 | `4bef1998a2ae5db9c58fb8129a84b20617257cfb6331053e66243c9b10a57995` |
| U | 架空Taskの着手可否診断。公開5項目すべてと範囲遵守 | 6 + 1 | `3e6fa9314bdb2000f03c075eafce505eb7858eb55abbb136fd1d7b33351aaf7e` |

入力一覧は [P](P/manifest.json)・[M](M/manifest.json)・[U](U/manifest.json)。各Knowledge本文は基準commitとバイト一致。CASE_TASKは承認済みテンプレートから題名・メタデータだけを具体化し、基準を変更していない。READY.mdはこの一覧に加わる実承認記録であり、今は存在しない。そのhashと全文は実行時のlaunch.jsonとinitial.txtへ保存する。

固定Knowledgeには承認前の状態ラベルが残るが、試験途中に書換えない。READY記録に、B-11の依存解消、PR #28の承認済み状態、基準commit、今回の説明・診断だけへの着手承認を明記して整合させる。

## 環境の根拠・限界

[追加検証と独立Review](../b12-environment/explicit-controls/README.md)を参照。ファイル指定でSkill案内が消え、明示的委譲無効化、Readerの許可/拒否、Skillの一覧空・既知識別子拒否、JS直接取得経路の未提供、raw call/output保存を確認した。本試験と共通runnerでもダミーmanifestの本文一致と禁止要求拒否を確認した。

これは通常Runtimeの設定強制を信頼する範囲の実測であり、Runtime内部の完全隔離や全内部動作の独立監査の証明ではない。外側のTool非公開はnested ALL_TOOLSだけで認定していない。各ケースの記録を再確認し、不明なアクセスを合格扱いしない。

`runner.py` は実Readyがなくても実行できるように迂回しない。Ready guardは記録形式/hashの確認であり、人間の承認の真偽や意味を自動認定する機能ではない。担当者が実際のユーザー承認と照合する。

## この試験後

全ケースと独立Reviewを揃えて、人間へ結果・限界・未解決事項を提示する。人間の受入前にB-12 DoneやPR mergeを行わない。受入後も、実コンテンツ制作とフィードバックによるtOSのリデザインは別の作業として続く。このB-12だけでtOS全体の完成を宣言しない。
