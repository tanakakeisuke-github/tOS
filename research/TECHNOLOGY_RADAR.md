# tOS — Technology Radar

状態：Draft。WATCH / TRIAL / ADOPT / HOLDは指定方針。候補表は議論に登場した名称の記録であり、製品評価・採用推薦ではない。

## 状態の意味

| 状態 | 意味 | 必要な判断・証拠（提案） |
|---|---|---|
| WATCH | 関連性を観察する候補 | 解決したい問題、調査する理由 |
| TRIAL | 限定した試行を承認済み | 範囲、担当、予算、評価基準、停止条件 |
| ADOPT | 特定用途・版への採用を承認済み | 試行結果、制約、Human Approval、戻し方 |
| HOLD | 導入を保留または見送り | 理由、再評価条件 |

WATCH → TRIAL → ADOPTは自動遷移ではない。HOLDやWATCHへ戻ることもある。候補の採用と既存Projectへの移行は別々に承認する。

## Bootstrapで保持する候補

以下のWATCHは「観察候補として残す」という本Draftの初期整理である。Human Review済みRadar台帳や実験承認を意味しない。正式製品の同定、公式URL、現行version、機能、価格、ライセンス、保守状態は未調査。名称だけから機能を補完しない。

| 候補名（元議論の表記） | Draft分類 | 次に確認すべきこと |
|---|---|---|
| Herdr | WATCH | 対象製品の同定、Executionとの境界、出力・移行可能性 |
| Orca | WATCH | 対象製品の同定、Workflowとの接続、Human Gateの表現 |
| Factory | WATCH | 対象製品の同定、限定Taskでの評価方法 |
| Cursor | WATCH | 利用する機能範囲、Knowledgeへの依存、証跡の保存 |
| GitHub Agents | WATCH | 対象機能の同定、権限とレビュー、Task契約への適合 |

これらをCoreへ固定しない。比較調査の実施・順位付け・導入時期は未決定。Local AIのModel / Runtime / hardware選定も別途評価する。

## 評価する軸（提案）

同じTaskと受入条件での品質、再現性、失敗時の停止、Human Gate、Fresh Context構成、権限、費用、人間の介入、出力形式、Vendor変更時の持出しと移行、運用負荷を確認する。

試行するときは公式一次情報のURL・確認日・対象versionを記録する。宣伝上の能力、試行で確認した能力、未確認事項を分ける。採用候補には比較対象と不採用理由も残す。

Current / Next / Labとの関係、Freeze、移行の考え方は[Technology Evolution](../specifications/TECHNOLOGY_EVOLUTION.md)。今回のBootstrapでは製品の現行機能調査やインストールを行っていない。
