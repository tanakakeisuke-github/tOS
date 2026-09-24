# tOS — Bootstrap History

状態：依頼で提示された発展経緯の保存。現在の規則はvision文書、今後の作業案はIssue Mapを参照。

この文書は「なぜこの設計になったか」を調べるための履歴です。Fresh Workerの必読Contextにはせず、Taskが理由の調査を必要とするときに読む資料とします。以下は概念上の発展順で、各段階の正確な日時や因果を実験で立証した記録ではありません。

| 段階 | 関心・懸念 | 次の設計につながった考え |
|---|---|---|
| 1. AI Game Studio構想 | 人間とAIの専門的な協働で制作を進めたい | 制作の役割と仕事の受け渡しを考える |
| 2. 長期Chatへの懸念 | 会話が長くなるとAIのContext品質が落ちるのではないか | 継続性を会話の長さに依存させない |
| 3. Fresh Context | 新しいAIにも必要な理解を渡したい | 目的に必要なKnowledgeを選んで渡す |
| 4. Discussion / Task分離 | 検討と実行が混ざると範囲が曖昧になる | 長寿命の検討・仕事と短命なSessionを分ける |
| 5. 部門横断Communication | 複数の専門Roleの判断をつなぐ必要がある | 個々のChatを越えて決定と成果を参照できるようにする |
| 6. Chat管理問題 | Chatの増加と引き継ぎで必要な知識を追いにくい | 持続する知識の置き場所を整える |
| 7. GitHub Source of Truth | Project / Workへの引き継ぎで詳細が伝わるか不安が生じた | 版管理できるKnowledgeとTaskに必要な参照をGitHubに残す |
| 8. Local AI | Cloud AIに加え、別の実行主体も協働に含めたい | Human / Cloud AI / Local AIをActorとして捉える |
| 9. Agent / Model交換可能性 | 技術が変わっても役割とKnowledgeを維持したい | Role / Actor / Agent / Model、実行技術の関係を分離する |
| 10. Technology候補の検討 | Herdr / Orca等、新しい仕組みをどう取り込むか | 個別技術の評価とCoreの設計を切り分ける |
| 11. Technology Radar | 制作と継続的な技術探索を両立したい | Current / Next / Labと段階的な評価・採用を考える |
| 12. 媒体に共通するtOS | ゲームで考えた制作基盤を他の媒体にも展開したい | 共通OS、Studio Template、Projectの分離へ発展する |

正式名称はtOSへ統一しました。今回の保存はGreenfieldで行い、以前のRepositoryやProjectの構造を引き継ぐ前提は置いていません。

## 今回の作業範囲へ至った理由

引き継ぎKnowledge一式を一度に作る案から、まず設計思想を保存し、Bootstrap KnowledgeをSmall Issueへ分けてレビューする方式へ移りました。Fresh Workerが一つの目的を理解し、作成し、確認できる範囲を見定めるためです。

Repositoryの確認時点では、mainは空の初期コミットのみで、以前の広いKnowledge案がDraft PR #1に残っていました。今回の案はmainを起点とする別のDraftとして保存します。既存PRの仕様を今回の承認済み入力としては扱わず、どちらを採用するかは人間のReviewで判断します。

懸念・経験・仮説の区別は[Findings](FINDINGS.md)、原文の参照先と確認範囲は[README](../README.md#出典と確認範囲)に記録しています。
