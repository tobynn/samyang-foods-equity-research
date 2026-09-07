def cagr(begin, end, years):
    if begin <= 0 or years <= 0:
        return None
    return (end / begin) ** (1 / years) - 1

def margin(profit, revenue):
    if revenue == 0:
        return None
    return profit / revenue
