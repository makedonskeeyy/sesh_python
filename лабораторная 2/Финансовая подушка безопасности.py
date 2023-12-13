money_capital = 20000  # Подушка безопасности/капитал в наличии
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты начиная с первого месяца
increase = 0.05  # Ежемесячный рост цен

i = 0 # i - количество месяцев без долгов
while True:
    money_capital = money_capital + salary - spend # Остаток капитала
    if money_capital < 0:
        break
    else: money_capital >= 0
    i = i + 1  # + 1 месяц
    spend = spend + (spend * increase) #Увеличение трат
print("Количество месяцев, которое можно протянуть без долгов:", i)
