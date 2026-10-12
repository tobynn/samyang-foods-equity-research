from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
FORECAST = ROOT / "data" / "processed" / "forecast_scenarios_2026_2030.csv"
ASSUMPTIONS = ROOT / "model" / "valuation_assumptions.csv"
OUTPUT = ROOT / "model" / "valuation_results.csv"


def assumption_table() -> dict[tuple[str, str], float | str]:
    table = pd.read_csv(ASSUMPTIONS)
    return {(row.method, row.item): row.value for row in table.itertuples()}


def dcf_value(fcff: list[float], wacc: float, growth: float, net_cash: float) -> float:
    pv_stage1 = sum(value / (1 + wacc) ** (year + 0.5) for year, value in enumerate(fcff))
    terminal_value = fcff[-1] * (1 + growth) / (wacc - growth)
    return pv_stage1 + terminal_value / (1 + wacc) ** (len(fcff) - 0.5) + net_cash


def rim_value(
    net_income: list[float],
    beginning_equity: float,
    cost_of_equity: float,
    payout_ratio: float,
    terminal_roe: float,
    terminal_growth: float,
    h1_actual_net_income: float,
) -> tuple[float, list[dict[str, float | int | str]]]:
    equity = beginning_equity
    pv_residual_income = 0.0
    rows = []
    for i, (year, full_year_income) in enumerate(zip(range(2026, 2031), net_income)):
        period = "2026H2" if i == 0 else str(year)
        income = full_year_income - h1_actual_net_income if i == 0 else full_year_income
        period_fraction = 0.5 if i == 0 else 1.0
        discount_time = 0.5 if i == 0 else year - 2026 + 0.5
        equity_charge = cost_of_equity * equity * period_fraction
        residual_income = income - equity_charge
        pv_residual = residual_income / (1 + cost_of_equity) ** discount_time
        dividend = income * payout_ratio
        ending_equity = equity + income - dividend
        rows.append({
            "year": year, "period": period, "beginning_equity": equity,
            "net_income": income, "dividend": dividend,
            "ending_equity": ending_equity, "equity_charge": equity_charge,
            "residual_income": residual_income, "discount_time": discount_time,
            "pv_residual_income": pv_residual,
        })
        pv_residual_income += pv_residual
        equity = ending_equity
    terminal_ri = (terminal_roe - cost_of_equity) * equity * (1 + terminal_growth)
    terminal_value = terminal_ri / (cost_of_equity - terminal_growth)
    pv_residual_income += terminal_value / (1 + cost_of_equity) ** 4.5
    return beginning_equity + pv_residual_income, rows


def main() -> None:
    values = assumption_table()
    forecast = pd.read_csv(FORECAST)
    base = forecast.loc[forecast["scenario"] == "Base"].sort_values("year")

    shares = float(values[("Common", "shares_outstanding")])
    net_cash = float(values[("Common", "net_cash")])
    dcf_equity = dcf_value(
        base["fcff_krw_bn"].tolist(),
        float(values[("DCF", "wacc")]),
        float(values[("DCF", "terminal_growth")]),
        net_cash,
    )

    per_eps = float(values[("PER", "forward_eps")])
    per_price = per_eps * float(values[("PER", "target_multiple")])
    per_equity = per_price * shares / 1_000

    rim_equity, _ = rim_value(
        base["net_income_krw_bn"].tolist(),
        float(values[("RIM", "beginning_common_equity")]),
        float(values[("RIM", "cost_of_equity")]),
        float(values[("RIM", "payout_ratio")]),
        float(values[("RIM", "terminal_roe")]),
        float(values[("RIM", "terminal_growth")]),
        float(values[("RIM", "2026H1_actual_net_income")]),
    )

    results = pd.DataFrame(
        [
            ["DCF", "Base", dcf_equity, dcf_equity * 1_000 / shares, "filed-anchor"],
            ["PER", "Base", per_equity, per_price, "market-cross-check"],
            ["RIM", "Base", rim_equity, rim_equity * 1_000 / shares, "provisional-equity-anchor"],
        ],
        columns=["method", "case", "equity_value_krw_bn", "value_per_share_krw", "status"],
    )
    results["equity_value_krw_bn"] = results["equity_value_krw_bn"].round(1)
    results["value_per_share_krw"] = results["value_per_share_krw"].round().astype(int)
    results.to_csv(OUTPUT, index=False)
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
