# tOS — Future Vision

状態：依頼で指定された設計思想・将来構想の保存。記述はHuman Review待ち。

## 目指すもの

tOSは、人間・Cloud AI・Local AIが協働し、Game / Film / Music / Publishing / App等へ展開できるAI-native制作OSを目指します。長期に残る知識と、短命なAI Sessionを結び、制作を継続できる基盤にします。

制作の媒体や作品が変わっても、目的、意思決定、仕事の受け渡し、検証結果を復元できることが重要です。正式名称は **tOS** です。

## 協働と交換可能性

Human / Cloud AI / Local AIをActorとして扱います。Role / Actor / Agent / Modelを分離し、役割を特定の実行技術へ固定せずに割り当てられる設計を目指します。

以下は用語を読むための説明案です。厳密な関係・権限はIssue MapのB-07で定義します。

| 概念 | 説明案 |
|---|---|
| Role | 制作上の責任・期待される仕事 |
| Actor | 仕事を担う主体。Human / Cloud AI / Local AI |
| Agent | AIによる仕事の実行を構成する単位 |
| Model | Agentが利用する推論等の能力を提供するモデル |

Runtime / Orchestrator / Vendorも交換可能な選択肢として扱います。新しい技術を導入する際、責務と接続条件を保ちながら該当部分を交換でき、OS全体の再設計を必須にしない方向です。具体的なAPIや実行環境は未決定です。

## Studio TemplateとProject Bootstrap

共通のtOSから複数のStudio Templateを用意し、各Templateから複数のProjectを立ち上げる将来像です。媒体ごとの専門Role、成果物、品質確認はStudio Templateで具体化し、各Projectで作品の目的と制約を定めます。

**Project Bootstrap構想**：適用するtOSの版、Studio Template、Project固有の目的・制約をもとに、制作開始に必要な知識と仕事の入口を用意する。入力項目、生成物、手動と自動の分担、承認手順はOpen Questionです。今回のBootstrap Knowledge保存は、この機能の実装とは段階が異なります。

## 作り直せるものと引き継ぐもの

AIにより再構築コストが下がるという見通しのもと、Implementationは作り直せるものとして考えます。コスト低下の程度や、再構築の優位性は実際の測定が必要です。

Principles / Requirements / Decisions / Learnings / Failures / Benchmarks / Project Historyは、実装を交換するときも残します。何を守り、何を試し、なぜ採用・撤回したかが、次の実装の判断材料になります。保持形式・版管理・移行時の同等性確認は後続Issueで設計します。

## 次の具体化

PurposeとCore境界はB-01/B-03、Actorの関係はB-07、交換・再構築の評価はB-10で扱う提案です。依存順と未決定事項は[Issue Map](../bootstrap/ISSUE_MAP.md)に集約しています。
