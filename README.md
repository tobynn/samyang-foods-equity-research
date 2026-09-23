# 삼양식품 기업분석 · 가치평가

> 해외 매출, 생산능력, 수익성의 변화를 2026E–2030E 실적과 DCF·RIM·PER 가치평가로 연결한 기업분석 포트폴리오

[![Company](https://img.shields.io/badge/Company-Samyang%20Foods-E60012)](https://www.samyangfoods.com/)
![Ticker](https://img.shields.io/badge/KRX-003230-1f6feb)
![Status](https://img.shields.io/badge/Status-Complete%20v1.0-2ea44f)
![Data](https://img.shields.io/badge/Data-2026H1-2ea44f)

## 한눈에 보기

삼양식품의 최근 성장은 해외 매출 확대와 생산능력 증설에서 나왔다. 이 저장소는 2021–2025년 실적과 2026년 상반기 자료를 바탕으로 매출·이익·FCFF를 전망하고, 서로 다른 관점의 세 평가법을 비교한다.

| 항목 | 핵심 내용 |
|---|---:|
| 2025 매출 / 영업이익률 | 2.352조원 / 22.3% |
| 2026H1 매출 / 영업이익률 | 1.485조원 / 23.8% |
| 2026H1 해외 매출 비중 | 82.9% |
| Base 2026E 매출 / EPS | 3.10조원 / 76,132원 |
| Base 2030E 매출 / FCFF | 5.27조원 / 8,279억원 |
| DCF 기준값 | 1,631,897원/주 |
| PER 기준값 | 1,366,590원/주 |
| RIM 기준값 | 837,658원/주 |

> 위 값은 2026년 상반기까지의 공개자료와 독립 가정을 사용한 포트폴리오 계산 결과다. 목표주가나 투자 권유가 아니다. RIM 시작 자기자본은 2026H1 공시 기준 1.5483조원으로 확정했다.

### 완성본 바로 보기

- [최종 PDF 보고서](report/Samyang_Foods_Equity_Research_2026H1.pdf)
- [DCF Excel 모델](model/DCF_model.xlsx)
- [RIM Excel 모델](model/RIM_model.xlsx)
- [가치평가 상세 설명](report/VALUATION.md)

## 투자 판단의 핵심

1. **해외 매출이 성장의 중심이다.** 2026H1 해외 매출은 1.231조원으로 전체 매출의 82.9%다.
2. **증설 시점이 전망을 바꾼다.** 밀양 2공장의 2026년 가동률 상승과 2027년 예정된 중국 자싱 공장이 매출 증가의 주요 전제다.
3. **마진은 23%대에서 안정되는 것으로 잡았다.** Base 영업이익률은 2026E 23.5%, 2028E 24.0%, 2030E 23.5%다.
4. **평가법별 결과 차이가 크다.** DCF는 163만원, 비교기업 PER은 137만원, RIM은 84만원이다. 성장의 현금흐름 반영 시점과 장기 ROE 가정 차이가 평가 편차를 만든다.

## Base 전망

| 구분 | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---:|---:|---:|---:|---:|
| 매출(십억원) | 3,100 | 3,720 | 4,315 | 4,833 | 5,268 |
| 매출 성장률 | 31.8% | 20.0% | 16.0% | 12.0% | 9.0% |
| 영업이익률 | 23.5% | 23.8% | 24.0% | 23.8% | 23.5% |
| 순이익(십억원) | 573.5 | 699.4 | 819.9 | 903.8 | 969.3 |
| FCFF(십억원) | 294.6 | 516.3 | 659.1 | 756.1 | 827.9 |

상세 가정과 계산식은 [`report/VALUATION.md`](report/VALUATION.md), 입력값과 출력값은 [`model/valuation_assumptions.csv`](model/valuation_assumptions.csv)와 [`model/valuation_results.csv`](model/valuation_results.csv)에서 확인할 수 있다.

## 평가 결과

| 평가법 | 기준 가정 | 주당가치 | 해석 |
|---|---|---:|---|
| DCF | WACC 8.5%, 영구성장률 2.5% | 1,631,897원 | Base FCFF와 2026H1 순현금 사용 |
| PER | 2027E EPS 92,839원, 14.72배 | 1,366,590원 | 비교기업 중앙값 9.815배에 50% 프리미엄 |
| RIM | 자기자본비용 9.0%, 장기 ROE 14.0% | 837,658원 | 2026H1 자기자본 1.5483조원 사용 |

DCF 민감도에서 주당가치는 132만~216만원 범위다(WACC 7.5~9.5%, 영구성장률 2.0~3.0%). 숫자 하나보다 가정 변화에 따른 범위를 먼저 본다.

## 저장소 구성

```text
.
├── data/
│   ├── raw/                    # 원문 자료 위치 안내
│   ├── processed/              # 재무·사업지표·전망 CSV
│   └── source_registry.csv     # 출처 목록
├── documents/                  # 사업·반기·IR 자료 위치 안내
├── notebooks/
│   ├── 01_financial_trend_analysis.ipynb
│   ├── 02_revenue_driver_framework.ipynb
│   ├── 03_forecast_valuation_bridge.ipynb
│   └── 04_per_relative_valuation.ipynb
├── research/
│   ├── 2026H1_DRIVER_NOTES.md
│   ├── FORECAST_ASSUMPTIONS_2026_2030.md
│   └── PER_PREMIUM_FRAMEWORK.md
├── model/
│   ├── DCF_model.xlsx
│   ├── RIM_model.xlsx
│   ├── PER_template.xlsx
│   ├── valuation_assumptions.csv
│   └── valuation_results.csv
├── report/
│   ├── Samyang_Foods_Equity_Research_2026H1.pdf
│   └── VALUATION.md
├── src/
│   ├── generate_portfolio_artifacts.py
│   ├── metrics.py
│   └── valuation.py
├── figures/                    # 보고서에 사용한 재무·전망·가치평가 차트
└── assets/fonts/               # PDF 재현용 오픈 라이선스 한글 폰트
```

DCF·RIM Excel은 입력, 예측, 가치평가, 민감도 또는 브리지 시트로 구성했다. 외부 링크와 과거 표본기업 값은 제거했고, Python 기준본과 동일한 가정을 사용한다.

## 재현 방법

```bash
pip install -r requirements.txt
python src/valuation.py
python src/generate_portfolio_artifacts.py
```

첫 번째 스크립트는 전망 CSV와 가정표를 읽어 가치평가 결과를 다시 만든다. 두 번째 스크립트는 DCF·RIM Excel, 차트 3종, 12쪽 PDF 보고서를 재생성한다. Notebook은 01 → 02 → 03 → 04 순서로 실행한다.

## 다음 업데이트 시점

- PER 비교기업 컨센서스 출처와 기준일 정기 갱신
- 2026년 연간 실적 발표 후 전망 갱신
- 중국 자싱 공장 가동 일정과 밀양 2공장 가동률 점검
- 환율·원재료비 변화에 따른 영업이익률 가정 재검토

## 주요 출처

- [삼양식품 IR 재무정보](https://www.samyangfoods.com/kor/ir/finance.do)
- [삼양식품 IR 자료실](https://www.samyangfoods.com/kor/ir/list.do)
- [DART 2026년 반기보고서](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003053)
- [KRX KIND](https://kind.krx.co.kr/)

## 면책

교육·취업 포트폴리오 목적으로 작성했다. 모든 전망과 가치평가는 작성자의 가정이며 투자 조언이 아니다.

## PER 비교기업 분석

- [PER 프리미엄 산정 근거](research/PER_PREMIUM_FRAMEWORK.md)
- [비교기업 데이터](data/processed/peer_valuation_2026_2027.csv)
- `notebooks/04_per_relative_valuation.ipynb`에서 프리미엄과 적정가치 민감도를 재현할 수 있다.
