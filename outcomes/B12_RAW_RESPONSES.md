# B-12 raw responses for independent scoring

Fixed repo commit: `5f15fd73800c23b04875ef73261367e0df7aa81c`. These are copied from the final messages of three separate Fresh Worker Sessions. They are not edited answers. The workers' tool logs are not available here; file-read lists below are self-reports.

## Case P

(1) **新任者向け説明（700字以内）**

tOSは、人間とAIが作品制作を続け、短いAI Sessionを越えて目的・判断・検証結果を引き継ぐための制作OSを目指します（`specifications/PURPOSE.md`「何のためにあるか」）。長期構想の流れは、tOS設計・v0.1整備から、媒体別Template、作品企画、制作、評価と改善、完成、人間による振り返りへ進みます（`vision/CREATION_LIFECYCLE.md`「設計から完成へ」）。Coreは媒体共通の仕事・知識・Reviewの枠組み、Studio Templateは媒体固有の役割・工程・評価、Projectは個別作品の目的・制約・完成判断を担います。これは設計上の境界で、実装完了を示しません（`specifications/CORE_ARCHITECTURE.md`「三層の責務と受け渡し」「未決定の範囲」）。このTaskは、その理解を出典付きで説明するB-12試験です。実装・Freeze・Done判断は範囲外です（`CASE_TASK.md`「目的」「対象外」）。着手と完了は人間が承認し、入力不足や矛盾があれば影響する作業を止めます（`CONSTITUTION.md`「変わりにくい原則」）。tOS v0.1全体の範囲・完成条件とProject Bootstrapの詳細は未決定です（`bootstrap/ISSUE_MAP.md`「Open Questions」、`specifications/CORE_ARCHITECTURE.md`「Project Bootstrapの位置」）。

(2) **実際に読んだファイル・節**

- `START_HERE.md`、`CASE_TASK.md`、`READY.md`：全文
- `specifications/PURPOSE.md`、`CONSTITUTION.md`：全文
- `specifications/CORE_ARCHITECTURE.md`：冒頭、「三層の責務と受け渡し」「Project Bootstrapの位置」「二つの媒体で境界を確かめる」「未決定の範囲」。全節の見出し
- `vision/CREATION_LIFECYCLE.md`：冒頭、「設計から完成へ」「制作中のOS改善」「完成後の二つの振り返り」「循環」。全節の見出し
- `bootstrap/ISSUE_MAP.md`：「B-12 — Fresh Worker Acceptance Test」「Open Questions」。全節の見出し
- `vision/FUTURE_VISION.md`：「Studio TemplateとProject Bootstrap」「作り直せるものと引き継ぐもの」。全節の見出し
- `specifications/KNOWLEDGE_ARCHITECTURE.md`：見出しのみ

(3) **入力の不確実性・停止**：`READY.md`にB-12試験の着手承認が明記されています。固定版に残るB-11のReview待ち表示との時点差も同文書で説明されています。この説明作業について停止点はありません。Doneは別のHuman Review待ちです。

(4) Model ID: Unknown

## Case M

1. **着手不可。** 模擬Readyは架空Taskの着手条件を満たしますが、指定された `studio/EVALUATION.md` と `project/BRIEF.md` がこの入力フォルダにありません。Templateの評価観点とProjectの体験目標・制約が欠けるため、受入条件に沿って評価項目を確定できません。CoreのGame例から補うこともできません。欠けた資料の適用版と承認状態を人間に確認し、必要ならTaskの入力・範囲を改めて承認してから再開します。根拠：`CONSTITUTION.md`「変わりにくい原則」2、`specifications/KNOWLEDGE_ARCHITECTURE.md`「Taskごとの入力とOpen Question」「参照経路の例（架空）」、`specifications/CORE_ARCHITECTURE.md`「三層の責務と受け渡し」「二つの媒体で境界を確かめる」。
2. **実際に読んだ範囲：** `START_HERE.md`、`CASE_TASK.md`、`READY.md`、`MOCK_READY.md` は全文。`specifications/PURPOSE.md`、`CONSTITUTION.md`、`specifications/KNOWLEDGE_ARCHITECTURE.md` も全文。`specifications/CORE_ARCHITECTURE.md` は冒頭・状態、「三層の責務と受け渡し」、「Project Bootstrapの位置」、「二つの媒体で境界を確かめる」、「未決定の範囲」。加えて同フォルダ内のMarkdownファイル名一覧を確認しました。
3. 評価項目その他の制作成果物は作成していません。
4. Model ID: Unknown

## Case U

1. **着手できません。** Issueの作成だけでは足りず、架空の制作Taskには対象版、詳細範囲、入力、受入条件、Ready承認が記録されていません。B-12の承認はこの診断に限られます。これらと依存関係を担当Issueで明確にし、人間が着手を承認した後に再開できます。（`READY.md`、`CONSTITUTION.md`「変わりにくい原則」、`specifications/PURPOSE.md`「現在の範囲と未決定事項」、`specifications/KNOWLEDGE_ARCHITECTURE.md`「Taskごとの入力とOpen Question」）
2. 読んだファイル・節：`START_HERE.md`、`CASE_TASK.md`、`READY.md`は全文。`CONSTITUTION.md`は見出し・検索該当行と「変わりにくい原則」「文書が食い違うとき」。`specifications/PURPOSE.md`は見出し・検索該当行と「現在の範囲と未決定事項」「入力と承認」。`specifications/KNOWLEDGE_ARCHITECTURE.md`は見出し・検索該当行と「Taskごとの入力とOpen Question」。
3. 仕様の実装・変更：なし。
4. Model ID: Unknown
