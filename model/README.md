# Valuation models

## 현재 포함 파일

- `PER_template.xlsx`: 기존 PER 템플릿
- `DCF_model.xlsx`: 2026E–2030E FCFF, terminal value, 순현금, 민감도 계산
- `RIM_model.xlsx`: 2026H1 연결 equity proxy, 2026H2 잔여이익, terminal value, 장부가치 브리지 계산
- `valuation_assumptions.csv`: DCF·RIM·PER 공통 가정표
- `valuation_results.csv`: `src/valuation.py`가 생성하는 결과표

Excel 모델과 Python 계산은 같은 입력값을 사용한다. 기준 결과는 DCF 1,631,897원, PER 1,366,590원, RIM 811,036원이다.

## 입력 원칙

- 단위를 명시한다.
- 공시값, 전망값, 임시값을 구분한다.
- Base/Bull/Bear를 같은 정의로 비교한다.
- Excel과 Python의 가정을 `valuation_assumptions.csv`에 맞춘다.
- 외부 링크와 과거 표본기업 값을 제거한 뒤 공개한다.


## 해석 기준 보완

PER 모델의 primary panel은 농심·오리온이지만 관찰 프리미엄 +50%는 공정가치로 검증된 계수가 아니라 기존 snapshot 기반 sensitivity다. 기준일은 DCF/RIM의 평가일/주가일은 2026-09-18, 실제기간 말은 2026-06-30이다. 갱신·해석 때 [`peer scorecard`](../research/PEER_SELECTION_SCORECARD.md), [`premium framework`](../research/PER_PREMIUM_FRAMEWORK.md), [`vintage policy`](../research/VALUATION_VINTAGE_POLICY.md)를 먼저 확인한다.


The DCF and RIM `Inputs` tabs now carry an in-model vintage/evidence control block: the 2026-09-18 valuation/price date and 2026-06-30 latest actual-period end, the +50% PER sensitivity caveat, equity attribution checks and forecast refresh labels. The 2026H2 residual-income stub now deducts reported 2026H1 net income from FY2026E and applies half-year equity charge and discount timing. Parent equity / NCI attribution remains provisional.
