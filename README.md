# Samyang Foods Equity Research & Valuation

**Company:** Samyang Foods Co., Ltd. (KRX: 003230)  
**Project type:** Finance × Data Analytics portfolio project  
**Status:** Starter repository

## Project objective

Build a reproducible equity-research workflow that connects:

1. public financial data,
2. Python-based cleaning and analysis,
3. business-driver forecasting,
4. PER / RIM / DCF valuation,
5. a final equity-research report,
6. and later an LLM/RAG research assistant using the same public filings.

### Core research question

> Can Samyang Foods sustain its earnings growth, and what valuation is justified by a driver-based forecast rather than a simple historical-average extrapolation?

This is a hypothesis to test, not a predetermined conclusion.

---

## Repository structure

```text
samyang-foods-equity-research/
├── README.md
├── START_HERE_KR.md
├── PROJECT_PLAN.md
├── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   │   └── financials_annual.csv
│   └── source_registry.csv
├── documents/
│   ├── annual_reports/
│   ├── quarterly_reports/
│   └── ir_presentations/
├── notebooks/
│   ├── 01_financial_trend_analysis.ipynb
│   ├── 02_revenue_driver_framework.ipynb
│   └── 03_forecast_valuation_bridge.ipynb
├── src/
│   └── metrics.py
├── model/
│   ├── PER_template.xlsx
│   ├── RIM_template.xlsx
│   └── DCF_template.xlsx
├── figures/
├── report/
└── llm_extension/
```

---

## Current baseline data

The starter dataset contains 2021-2025 consolidated headline financials from Samyang Foods' official IR financial-information page.

| Year | Revenue (KRW mn) | Operating Profit (KRW mn) | Net Income (KRW mn) |
|---:|---:|---:|---:|
| 2021 | 642,030 | 65,363 | 56,658 |
| 2022 | 909,037 | 90,376 | 80,271 |
| 2023 | 1,192,915 | 147,514 | 126,591 |
| 2024 | 1,728,015 | 344,569 | 271,256 |
| 2025 | 2,351,785 | 524,188 | 388,674 |

**Primary source:** https://www.samyangfoods.com/kor/ir/finance.do

Before valuation, detailed figures should be reconciled to the annual/quarterly filings in DART.

---

## Analysis roadmap

### Phase 1 — Historical financial analysis
- Revenue growth
- Operating margin
- Net margin
- CAGR
- profitability trend
- cash-flow and balance-sheet items to be added from DART

### Phase 2 — Business-driver analysis
Instead of forecasting revenue with only historical growth rates, define operational drivers.

Candidate drivers to test:
- domestic vs. overseas sales
- major regional growth
- product / brand mix
- production capacity and utilization
- ASP / pricing
- FX exposure
- raw-material / logistics cost
- CAPEX and new capacity

### Phase 3 — Forecast
Create Base / Bull / Bear cases for:
- revenue
- EBIT margin
- tax rate
- D&A
- working capital
- CAPEX
- FCFF
- EPS / book value

### Phase 4 — Valuation
Use the existing templates in `/model` as a starting point:
- PER
- RIM
- DCF

The final project should explain **why each assumption is used**. Do not simply apply historical averages.

### Phase 5 — Research report
Target output:
- 10-15 page equity-research PDF
- investment thesis
- industry/company analysis
- earnings forecast
- valuation
- risks
- sensitivity / scenario analysis

### Phase 6 — LLM extension
Reuse Samyang Foods filings and IR documents to build a citation-based RAG research assistant.

See `/llm_extension/README.md`.

---

## Getting started

```bash
pip install -r requirements.txt
jupyter notebook
```

Run notebooks in order:

1. `01_financial_trend_analysis.ipynb`
2. `02_revenue_driver_framework.ipynb`
3. `03_forecast_valuation_bridge.ipynb`

---

## Data-source policy

Prefer primary sources:
1. Samyang Foods IR
2. DART
3. KRX KIND
4. Bank of Korea / KOSIS / customs data where needed

Every model input should eventually have a traceable source.

---

## Disclaimer

This repository is an educational portfolio project and is not investment advice.
