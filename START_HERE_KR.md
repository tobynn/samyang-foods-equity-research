# 시작하기 — 삼양식품 Equity Research

이 저장소는 2026H1 actuals와 2026E–2030E forecast를 DCF·RIM·PER에 연결한 포트폴리오다. 기존 평가 결과를 새로 검증된 데이터처럼 보지 않도록 vintage와 시나리오 가정을 분리한다.

## 권장 읽기 순서

1. [`README.md`](README.md) — 요약, 결과, 저장소 지도
2. [`research/COMPANY_SPECIFIC_FRAMEWORK.md`](research/COMPANY_SPECIFIC_FRAMEWORK.md) — 해외 수요·공장 증설·마진·현금 전환 논리
3. [`research/PEER_SELECTION_SCORECARD.md`](research/PEER_SELECTION_SCORECARD.md) — 농심·오리온 정량 앵커와 후보/보조 peer의 역할
4. [`research/VALUATION_VINTAGE_POLICY.md`](research/VALUATION_VINTAGE_POLICY.md) — actual, estimates, market date 동기화 규칙
5. [`report/VALUATION.md`](report/VALUATION.md) — DCF·PER·RIM 계산과 결과 차이
6. [`report/METHODOLOGY_APPENDIX.md`](report/METHODOLOGY_APPENDIX.md) — 보고서용 방법론 종합 부록
7. `model/DCF_model.xlsx`, `model/RIM_model.xlsx` — 감사 가능한 현금흐름/초과이익 빌드

## 해석할 때 주의

- DCF/RIM의 기초는 2026H1 공시 실적이다. 모델 탭의 2026-06-30 date와 PER 자료의 2026-09-18 peer snapshot은 완전히 같은 vintage가 아니므로 한 날짜의 fair value로 혼합하지 않는다.
- 14.72x PER Base는 관찰된 시장 프리미엄 +50%를 다시 쓴 sensitivity다. 적정배수로 검증된 값이 아니다.
- DCF·PER·RIM은 평균하지 않는다. 각 방법이 성장 현금흐름, 시장 상대가격, 장기 ROE를 각각 보여준다.
- 새 actuals를 추가할 때 원본 공시 출처, 연결/별도, 누적/분기, 실제/잠정 구분을 함께 기록한다.

## 갱신 순서

DART·공식 IR 자료 확인 → actuals/source registry 입력 → 지역/공장/원가/운전자본 가정 업데이트 → `src/valuation.py` 실행 → Excel/PDF 재생성 스크립트 점검 → 가치 변화를 actuals/forecast/multiple·discount-rate 요인으로 나눠 기록한다.
