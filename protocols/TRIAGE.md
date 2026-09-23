# tOS — Triage Protocol

状態：Draft。Triage controls work creationは指定原則。担当・保存先・具体的な運用は未決定。

## 役割

Triageは発見を、実行する仕事へ変える前の判断点である。AIは提案できるが、作業の新設、優先順位、範囲、担当、Ready化を自己決定しない。今回はTriage用のIssue、Project、Automationを作成しない。

## 提案に含める情報（案）

観察と出典、問題、現在のTaskとの関係、期待する改善、影響範囲、緊急度と根拠、既存候補との重複、必要な検証、費用・権限の見込みを簡潔に示す。数字が不明なら不明と記載する。

承認された永続化先がまだない場合は、現在の成果報告・引継ぎの「Triage候補」に記録して人間へ渡す。AIが保存先を理由に新しいIssueを作る必要はない。

## 判断（提案）

既存作業への統合候補、別Task候補、調査が先、保留、却下、重複として整理する。採用する場合も、目的・受入条件・Required Context・権限を整え、Ready前のHuman Approvalを得る。

Triageの受付と、実行承認は別。AIが評価を補助する方式は検討できるが、Human Gateを消さない。承認担当や委任範囲は[Open Questions](../bootstrap/OPEN_QUESTIONS.md)で決める。

急を要する依存問題は、現在のTaskを[STOP](TASK.md)し、影響と必要な判断を提示する。緊急性だけで新規作業やOS Version変更を実行しない。
