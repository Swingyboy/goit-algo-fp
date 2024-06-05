import random
import collections
import matplotlib.pyplot as plt
from tabulate import tabulate
from typing import Dict

THEORETICAL_PROBABILITIES = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36
}


def simulate_dice_rolls(num_rolls: int) -> Dict[int, int]:
    sums_count = collections.defaultdict(int)
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1

    return sums_count


def calculate_probabilities(sums_count: Dict[int, int], num_rolls: int) -> Dict[int, float]:
    probabilities = {}
    for dice_sum, count in sums_count.items():
        probabilities[dice_sum] = count / num_rolls
    return probabilities


if __name__ == "__main__":
    num_rolls = 1000000
    sums_count = simulate_dice_rolls(num_rolls)
    SIMULATED_PROBABILITIES = calculate_probabilities(sums_count, num_rolls)

    theoretical_probabilities_percentage = {k: v * 100 for k, v in THEORETICAL_PROBABILITIES.items()}
    simulated_probabilities_percentage = {k: v * 100 for k, v in SIMULATED_PROBABILITIES.items()}

    table_data = []

    for sum_value in range(2, 13):
        table_data.append([
            sum_value,
            f"{simulated_probabilities_percentage[sum_value]:.2f}",
            f"{theoretical_probabilities_percentage[sum_value]:.2f}"
        ])

    print(tabulate(table_data, headers=["Sum", "Simulated Probabilities (%)", "Theoretical Probabilities (%)"],
                   tablefmt="pretty"))

    sums = list(range(2, 13))
    simulated_probs = [simulated_probabilities_percentage[sum_value] for sum_value in sums]
    theoretical_probs = [theoretical_probabilities_percentage[sum_value] for sum_value in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, simulated_probs, width=0.4, label='Simulated Probabilities (%)', align='center')
    plt.bar([x + 0.4 for x in sums], theoretical_probs, width=0.4, label='Theoretical Probabilities (%)', align='center')
    plt.xlabel('Sum')
    plt.ylabel('Probabilities (%)')
    plt.title('Sum Probabilities of Dice Rolls')
    plt.xticks(sums, [str(sum_value) for sum_value in sums])
    plt.legend()
    plt.grid(True)
    plt.show()
