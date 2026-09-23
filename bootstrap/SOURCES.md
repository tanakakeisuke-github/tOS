# tOS — Bootstrap Sources and Scope

状態：Draft / 出典と編集境界。Fresh Workerが元会話へアクセスすることは理解の前提にしない。

## S-01 — 今回のKnowledge Bootstrap依頼

2026-09-24の依頼を、本Bootstrapの要件と承認範囲の基準とする。正式名称、Greenfield、Knowledgeのみ、指定原則、推奨ファイル構造、HISTORYの経緯、自己レビュー、Draft PRでの停止が明示されている。必要な内容は本Repositoryに分割して収録した。

S-01で明示された履歴の流れは、AI Game Studio → 長期Chatの精度低下への懸念 → Fresh Context → Discussion / Task分離 → 部門横断Communication → GitHub Source of Truth → Local AI → Agent交換可能性 → Runtime候補 → Technology Radar → メディア非依存のtOSである。

## S-02 — 元のArchitecture Discussion

参照：[\[HQ\]\[DISC\] Studio Architecture 001](https://chatgpt.com/c/6aa96c7c-da58-83ee-be94-c118cf99c5cb)。会話へのアクセスには権限が必要な場合がある。リンクは来歴用であり必読ではない。

今回、直近から過去へ30ターンを取得して確認した。全文の通読・全添付画像の確認はしていない。主に以下の内容を経緯と設計意図の裏付けに使用した。

| 論点 | 確認した発言の識別子 | 扱い |
|---|---|---|
| 詳細KnowledgeをRepositoryへ移す依頼 | 72602ad3-efb7-4638-94a4-a5b43a3e9f05 | 現在の依頼とも一致 |
| tOSへの正式名称統一 | 7f1b764a-e2f7-4eee-b111-fece37ecb3bf | 現行名称 |
| GitHub中心の引継ぎと読む順序 | e9829e08-4e9e-4920-ac49-b60c3ef3fe05 | 設計意図 |
| Greenfieldと不要なアンカー除去 | 3f4e9c5d-b033-45aa-8f4c-45407709a14c | 現在の依頼を優先して反映 |
| 新しい作業側へのContext不安 | 9999b159-b2af-45f1-a485-15ebe4e5e40e | ユーザー報告。画像評価は未実施 |
| Freeze、作り直し、残すKnowledge | aeeeda2b-49ce-48eb-b40e-c648bacdcc41 | 設計の理由。旧scope案は継承しない |
| Context Compiler、Learning Loop、将来候補 | 7e3f67f5-ad57-4342-bb03-701f0ee8e728 | 構想。実装実績として扱わない |
| 媒体展開とRole / Knowledge分離 | c4c25f66-67cb-44f2-a777-be4023560118 | 現行原則に沿う内容だけ再構成 |
| Local AIの予定と交換性 | 8e50a1c1-f403-4606-af6a-fa595d96aebc | 将来意図。導入実績は未確認 |

## 編集上の境界

元会話には探索案、後から撤回された構造、AIによる実施報告が混在する。現在の依頼を優先し、旧Repository / Project / Issue構造や特定作品の例をBootstrapへ転載しない。会話内のAI発言をそのまま実施・承認の証明にしない。

元会話で言及されたNotionページの現在内容は取得していない。過去Repository、稼働環境、製品機能も本Bootstrapの証拠として調査していない。必要な原則と経緯はS-01 / S-02から記述した。

製品名は候補として[Radar](../research/TECHNOLOGY_RADAR.md)へ隔離し、現在の仕様・価格・性能を断定しない。手順や記録項目の補足は「提案」、効果予想は「仮説」、未決定は[Open Questions](OPEN_QUESTIONS.md)へ残す。
