#main
import math
from mod import calculate_money  # Імпортуємо функцію з модуля

# Функція 1
def calculate_z(alpha):
    cos_alpha = math.cos(math.radians(alpha))
    z = cos_alpha**2 + cos_alpha**4
    return z

def main():
    while True:
        alpha = float(input("Введіть значення α (в градусах): "))
        z = calculate_z(alpha)
        print(f"Значення z = cos^2(α) + cos^4(α) дорівнює: {z:.4f}")

        styp = float(input("Введіть розмір щомісячної стипендії (грн): "))
        vytr = float(input("Введіть розмір щомісячних витрат на проживання (грн): "))

        # Перевірка, чи стипендія менша витрат
        if styp > vytr:
            print("Помилка: Стипендія не може бути більшою за витрати на проживання.")
        else:
            needed_money = calculate_money(styp, vytr)
            print(f"Сума грошей, яку необхідно попросити в батьків для проживання протягом року: {needed_money:.2f} грн")

        repeat = input("Бажаєте продовжити роботу з програмою? (y/n): ").strip().lower()
        if repeat != "y":
            break

if __name__ == "__main__":
    main()