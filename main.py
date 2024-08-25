import math

# Функція 1
def calculate_z(alpha):
    cos_alpha = math.cos(math.radians(alpha))
    z = cos_alpha**2 + cos_alpha**4
    return z

# Функція 2
def calculate_money(styp, vytr):
    total_money_needed = 0
    for month in range(10):
        total_money_needed += vytr - styp
        vytr *= 1.05  # збільшення витрат на 5% щомісяця
    return total_money_needed

def main():
    while True:
        alpha = float(input("Введіть значення α (в градусах): "))
        z = calculate_z(alpha)
        print(f"Значення z = cos^2(α) + cos^4(α) дорівнює: {z:.4f}")

        styp = float(input("Введіть розмір щомісячної стипендії (грн): "))
        vytr = float(input("Введіть розмір щомісячних витрат на проживання (грн): "))

        # Перевірка, чи стипендія менше витрат
        if styp > vytr:
            print("Помилка: Стипендія не може бути більшою за витрати на проживання.")
        else:
            needed_money = calculate_money(styp, vytr)
            print(f"Сума грошей, яку необхідно попросити в батьків для проживання протягом року: {needed_money:.2f} грн")

        repeat = input("Бажаєте повторити? (y/n): ").strip().lower()
        if repeat != "y":
            break

if __name__ == "__main__":
    main()