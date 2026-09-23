# tOS — Design History

状態：Draft / 経緯の要約。**Fresh Workerの必読ではない。** 現行の規範はConstitutionと適用Specificationを参照する。

この文書は[現在の依頼と元議論](SOURCES.md)に基づき、「なぜこの設計になったか」を再構成する。厳密な日時順の全発言録や、過去の実装状態を証明する監査記録ではない。

## 1. AI Game Studioから始まった問い

最初の関心は、AIと人間でゲーム制作を進める環境だった。個別の制作手段だけでなく、長期間の協働、役割間の受け渡し、人間の判断、知識の蓄積が課題となった。この出発点から、媒体が変わっても共通する問題を切り出す方向へ発展した。

## 2. 長期Chatの精度低下への懸念 → Fresh Context

会話が長くなるにつれ、古い前提、採用していない案、複数の目的が混ざることへの懸念があった。一つのChatを永続的な担当者や記憶として使うより、必要な知識を外部へ残してFresh Workerへ渡す方針につながった。

ここでの設計上の回答が「Chat is disposable. Knowledge is permanent.」と「Fresh Context by default.」である。懸念への回答であり、定量的な改善効果が確認されたという意味ではない。

## 3. Discussion / Task分離 → 部門横断Communication

探索しながら成果を作り続けると、目的と完了条件が変わりやすい。考えるDiscussionと、一つのsmall objectiveを実行するTaskを分け、作業を発見したときはTriageへ戻す設計になった。

さらにRoleや部門をまたぐ協働では、一つのChatにある暗黙の前提が相手に伝わるとは限らない。目的、受入条件、Artifact、Decisionを共有する必要があり、組織構造から独立したKnowledgeという考え方が強くなった。

## 4. GitHub Source of Truth → Local AI

複数の担当が同じ仕様、仕事、判断理由、結果を参照できる中心としてGitHubを位置づけた。ChatGPTはDiscussion / Planning / Directionを担い、正本とProject MemoryはGitHubへ残す。

Local AIも使う構想が加わると、知識を一つの会話サービス内に閉じ込める問題が明確になった。Cloud AI / Local AI / Humanが同じ仕事契約と知識を扱えるようにする意図につながった。Local AIを導入済みという意味ではない。

## 5. Agent交換可能性 → Runtime / Orchestrator候補

担当Roleを特定AgentやModelと一体化すると、技術が変わるたびに組織や知識を作り直すことになる。Role / Actor / Agent / Modelを分離し、Organizationを変更可能にする方針が生まれた。

Herdr / Orca等の候補が議論に登場したことで、実行を支える製品と上位の原則を分ける必要性が強まった。候補名と導入時期をCoreの前提へ昇格させず、交換可能な下位レイヤーとして扱う。

## 6. Technology Radar → FreezeとLearning Loop

AI技術を追い続けることと、制作を安定して進めることを両立させるため、WATCH / TRIAL / ADOPT / HOLD、Current / Next / Labを分ける構想となった。

Projectで採用したOS Versionを原則Freezeし、新しい発見は改善提案と検証を経て次版へ反映する。「Discover continuously, adopt deliberately.」がこの境界を表す。実装は作り直せても、原則、要求、仕様、判断、学び、失敗、評価、Project Historyは残す。

## 7. メディア非依存のtOSへ

複数作品と複数メディアへ展開する意図から、共通基盤、Studio Template、Creative Project、Executionを分ける設計へ進んだ。Game / Film / Music / Publishing / Appに共通する仕事と知識の仕組みをtOSとして扱う。

現在の正式名称は**tOS**。Greenfieldとして目的・原則から再評価し、過去の物理構造を継承しない。初版の実装scope、最初のTemplate、製品選定は再検討対象である。

## 8. Bootstrap自身の引継ぎ課題

元議論では、新しい作業側が設計の詳細を理解しているかという不安が表明された。人間向けのまとめを用意するだけでなく、AIが何をどの順で読むか、何を未決定と扱うか、理解をどう確認するかが必要になった。

そこで今回、GitHubに分割したKnowledgeを構築し、短いSTART_HEREを入口とする方針になった。まずDraft PRでHuman Reviewを受ける。その後のFresh Worker理解テストは[検証案](ACCEPTANCE.md)として残し、今回の自己レビューと混同しない。

過去の会話中の実施報告や提案は、そのまま現在の稼働状態・承認・仕様には採用していない。現在の原則は明示された依頼から、未決定事項は[Open Questions](OPEN_QUESTIONS.md)から確認する。
