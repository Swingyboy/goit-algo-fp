from typing import Dict, List, Union


def greedy_algorithm(food_items: Dict[str, Dict[str, int]], budget: int) -> Dict[str, Union[int, List[str]]]:
    sorted_items = sorted(food_items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return {"calories": total_calories, "selected items": selected_items, "total cost": total_cost}


def dynamic_programming(food_items: Dict[str, Dict[str, int]], budget: int) -> Dict[str, Union[int, List[str]]]:
    n = len(food_items)
    items = list(food_items.items())

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(1, budget + 1):
            cost = items[i - 1][1]['cost']
            calories = items[i - 1][1]['calories']
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(items[i - 1][0])
            b -= items[i - 1][1]['cost']

    return {"calories": dp[n][budget], "selected items": selected_items, "total cost": budget - b}


if __name__ == "__main__":
    food_items = {}
    while True:
        item = input("Enter item: ")
        if not item:
            break
        cost = int(input("Enter cost: "))
        calories = int(input("Enter calories: "))
        food_items[item] = {"cost": cost, "calories": calories}
    if not food_items:
        food_items = {
            "apple": {"cost": 2, "calories": 10},
            "banana": {"cost": 3, "calories": 20},
            "orange": {"cost": 4, "calories": 30},
            "pear": {"cost": 5, "calories": 40},
            "grape": {"cost": 6, "calories": 50},
        }
    print("Food items:")
    for item, info in food_items.items():
        print(f"{item}: {info}")
    budget = int(input("Enter budget: "))

    for algorithm in [greedy_algorithm, dynamic_programming]:
        print(f"\n{algorithm.__name__}:")
        res = algorithm(food_items, budget)
        print(f"Calories: {res['calories']}")
        print(f"Selected items: {res['selected items']}")
        print(f"Total cost: {res['total cost']}")
