# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = abs(float(input('input number: ')));
sum = 0;
if number < 1:
    while number%10 != 0:
        number = round(number * 10, 10);
while int(number)/10 != 0:
    sum = round(sum + (number%10));
    number = int(number/10)
print(sum)


