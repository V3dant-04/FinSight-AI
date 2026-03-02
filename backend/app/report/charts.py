from collections import defaultdict
from datetime import datetime

def category_chart_data(expenses):
    data = defaultdict(float)
    for e in expenses:
        data[e.category] += e.amount
    return [{"category": k, "amount": round(v, 2)} for k, v in data.items()]

def time_series_data(expenses):
    timeline = defaultdict(float)
    for e in expenses:
        day = e.date.strftime("%Y-%m-%d")
        timeline[day] += e.amount

    return [
        {"date": k, "amount": round(v, 2)}
        for k, v in sorted(timeline.items())
    ]
