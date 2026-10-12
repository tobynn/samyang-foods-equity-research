# Analysis Review — Samyang Foods

**Review date:** 2026-10-12  
**Latest actual anchor in this model:** 2026H1  
**Market price date in model:** 2026-09-18

## What was weak and what changed

| Area | Review finding | Improvement in this revision | Remaining evidence gate |
|---|---|---|---|
| Date vintage | The workbook called 2026-06-30 its valuation date while using a 2026-09-18 share price. That made the market and accounting snapshots look simultaneous. | DCF and RIM now show 2026-09-18 as the valuation / price date. The model notes separately identify 2026-06-30 as the latest actual-period end. | Refresh peer prices and estimates to the same market date before publishing a new target-price comparison. |
| RIM equity base | The input was called “beginning common equity” although its source note said consolidated equity. Consolidated equity can include non-controlling interests. | The Summary and Inputs now call it a **provisional consolidated-equity proxy** and flag parent-attributable equity / NCI reconciliation as a hard gate. No unsupported restatement was made. | Retrieve the 2026H1 DART statement of changes in equity / statement of financial position; use equity attributable to owners, then reconcile shares and treasury stock. Until then treat the RIM per-share output as provisional. |
| DCF terminal dependence | PV of terminal value is KRW 9,797.8bn of KRW 12,293.1bn equity value, or **79.7%**. A small change in WACC, terminal growth, or mature margin can dominate the result. | Keep DCF as a cross-check, not a stand-alone target. Show terminal-value share and WACC × g sensitivity with every refresh. | Add a fade bridge from 2030 EBIT margin / reinvestment to mature ROIC, and test terminal ROIC against WACC. |
| Growth narrative | A single revenue CAGR can hide whether growth comes from price, volume, geography, product mix, FX, or capacity. | The existing 2026H1 driver framework is retained as the causal bridge from export demand and capacity to forecast inputs. | Quantify region × product growth and separate shipment volume, realised price/mix, FX, and capacity constraints once disclosed. Avoid treating overseas share as margin evidence by itself. |
| PER premium | Peer-level multiple differences can double-count growth already included in EPS. The observed share-price sensitivity is not proof of a fair premium. | PER premium remains explicitly a sensitivity and is not used to override the DCF/RIM cross-checks. | Peer observations must have matching valuation date, forecast year, accounting basis, currency, and positive normalized EPS; record the source and retrieval date per peer. |

## Company-specific thesis to test

Samyang’s valuation should be driven by **repeatable overseas sell-through and contribution margin**, not export share alone. The causal chain to track is: regional distribution and brand pull → sell-through / repeat purchase → product and channel mix → realised price and gross margin → marketing and logistics burden → incremental ROIC on new capacity. Capacity additions create value only when incremental after-tax returns exceed the cost of capital after ramp-up costs and working capital.

## Model hierarchy

- **DCF:** operating-cash-flow test; currently terminal-value sensitive.
- **RIM:** balance-sheet / excess-return check; provisional until equity attribution is verified.
- **PER:** market context; no blended peer median and no automatic “brand premium.”

## Release gate

Before calling the per-share range final, reconcile (1) parent-attributable equity and non-controlling interests, (2) price date with peer-data date, (3) regional volume / price / mix evidence, and (4) mature-state ROIC and terminal value share. Primary-source starting points: [DART](https://dart.fss.or.kr/), [Samyang Foods IR financial information](https://www.samyangfoods.com/kor/ir/finance.do), [Samyang Foods IR library](https://www.samyangfoods.com/kor/ir/list.do).
