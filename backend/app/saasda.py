from collections import defaultdict

def build_report(expenses, insights, forecast):
    category_totals = defaultdict(float)

    for e in expenses:
        category_totals[e.category] += e.amount

    return {
        "total_expenses": sum(category_totals.values()),
        "category_breakdown": {
            k: round(v, 2) for k, v in category_totals.items()
        },
        "forecast_next_period": forecast,
        "key_insights": insights
    }
