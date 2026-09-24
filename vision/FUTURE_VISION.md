# tOS — Future Vision

状態：設計思想・将来構想の保存とB-01によるPurposeへの参照整理はHuman Review承認済み。将来構想の実装・検証を承認したものではありません。

## 目指すもの

正式名称は **tOS** です。目的・対象媒体・保持する価値は[Purpose](../specifications/PURPOSE.md)へ整理しました（B-01で承認済み）。ここでは、その目的から広がる将来の構成と設計方向を保存します。以下は実装済み機能や確定したv0.1の必須範囲を意味しません。

## 協働と交換可能性

Human / Cloud AI / Local AIの協働と、役割を特定の実行技術へ固定せずに割り当てられる設計を目指します。Role / Actor / Agent / Modelの関係と承認責任は[Actor Model](../specifications/ACTOR_MODEL.md)で扱います（B-07で承認済み）。

Runtime / Orchestrator / Vendorも交換可能な選択肢として扱います。新しい技術を導入する際、責務と接続条件を保ちながら該当部分を交換でき、OS全体の再設計を必須にしない方向です。具体的なAPIや実行環境は未決定です。

## Studio TemplateとProject Bootstrap

共通のtOSから複数のStudio Templateを用意し、各Templateから複数のProjectを立ち上げる将来像です。媒体ごとの専門Role、成果物、品質確認はStudio Templateで具体化し、各Projectで作品の目的と制約を定めます。

**Project Bootstrap構想**：適用するtOSの版、Studio Template、Project固有の目的・制約をもとに、制作開始に必要な知識と仕事の入口を用意する。入力項目、生成物、手動と自動の分担、承認手順はOpen Questionです。今回のBootstrap Knowledge保存は、この機能の実装とは段階が異なります。

## 作り直せるものと引き継ぐもの

AIにより再構築コストが下がるという見通しのもと、Implementationは作り直せるものとして考えます。コスト低下の程度や、再構築の優位性は実際の測定が必要です。

保持する知識と後続設計事項は[Purposeの「実装を越えて保持する価値」](../specifications/PURPOSE.md#実装を越えて保持する価値)を参照します。

## 次の具体化

Purposeは[B-01の仕様](../specifications/PURPOSE.md)、Core境界は[Core Architecture](../specifications/CORE_ARCHITECTURE.md)、Actorの関係は[Actor Model](../specifications/ACTOR_MODEL.md)で扱っています。交換・再構築の評価はB-10の提案です。依存順と未決定事項は[Issue Map](../bootstrap/ISSUE_MAP.md)に集約しています。
