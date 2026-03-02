def check_budget(expenses, budget_limit):
    total_spent = sum(e.amount for e in expenses)

    remaining = budget_limit - total_spent

    if remaining < 0:
        return {
            "status": "exceeded",
            "message": f"Budget exceeded by {abs(remaining)}"
        }

    if remaining < budget_limit * 0.2:
        return {
            "status": "warning",
            "message": f"Only {remaining} left. You are close to your budget limit."
        }

    return {
        "status": "safe",
        "message": f"You have {remaining} remaining in your budget."
    }
