# Valuation models

## 현재 포함 파일

- `PER_template.xlsx`: 기존 PER 템플릿
- `valuation_assumptions.csv`: DCF·RIM·PER 공통 가정표
- `valuation_results.csv`: `src/valuation.py`가 생성하는 결과표

이전 문서에 적혀 있던 `RIM_template.xlsx`, `DCF_template.xlsx`는 현재 GitHub 저장소에 존재하지 않는다. 두 파일을 추가하기 전까지 Python 계산을 재현 가능한 기준본으로 사용한다.

## 입력 원칙

- 단위를 명시한다.
- 공시값, 전망값, 임시값을 구분한다.
- Base/Bull/Bear를 같은 정의로 비교한다.
- Excel과 Python의 가정을 `valuation_assumptions.csv`에 맞춘다.
- 외부 링크와 과거 표본기업 값을 제거한 뒤 공개한다.
