salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты начиная с первого месяца
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Начальный капитал

for _ in range(months):  # 10
    money_capital = money_capital + salary - spend
    spend = spend + (spend * increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", abs (round(money_capital,2)))

