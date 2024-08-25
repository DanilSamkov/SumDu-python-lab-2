# mod.py
def calculate_money(styp, vytr):
    total_money_needed = 0
    for month in range(10):
        total_money_needed += vytr - styp
        vytr *= 1.05  # збільшення витрат на 5% щомісяця
    return total_money_needed