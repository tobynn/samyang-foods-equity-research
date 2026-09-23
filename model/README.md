# Valuation models

## 현재 포함 파일

- `PER_template.xlsx`: 기존 PER 템플릿
- `DCF_model.xlsx`: 2026E–2030E FCFF, terminal value, 순현금, 민감도 계산
- `RIM_model.xlsx`: 2026H1 확정 자기자본, 잔여이익, terminal value, 장부가치 브리지 계산
- `valuation_assumptions.csv`: DCF·RIM·PER 공통 가정표
- `valuation_results.csv`: `src/valuation.py`가 생성하는 결과표

Excel 모델과 Python 계산은 같은 입력값을 사용한다. 기준 결과는 DCF 1,631,897원, PER 1,366,590원, RIM 837,658원이다.

## 입력 원칙

- 단위를 명시한다.
- 공시값, 전망값, 임시값을 구분한다.
- Base/Bull/Bear를 같은 정의로 비교한다.
- Excel과 Python의 가정을 `valuation_assumptions.csv`에 맞춘다.
- 외부 링크와 과거 표본기업 값을 제거한 뒤 공개한다.
