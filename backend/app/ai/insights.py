from collections import defaultdict

def generate_insights(expenses):
    if not expenses:
        return ["No expense data available yet."]

    category_totals = defaultdict(float)

    for e in expenses:
        category_totals[e.category] += e.amount

    insights = []
    for category, total in category_totals.items():
        insights.append(
            f"You spent {round(total, 2)} in {category}."
        )

    top_category = max(category_totals, key=category_totals.get)
    insights.append(
        f"Your highest spending category is {top_category}."
    )

    return insights
