"""Блок ввода"""
while True:

    try:
        Number = int(input("Введите число (натуральное число)): "))
        CountSystem = int(input("Введите основание СС (натуральное число, 2 или 8)): "))
        if CountSystem != 2 and CountSystem != 8:
            print("По ТЗ программа может переводить только в двочную или восьмеричную систему, повторите ввод")
            continue
        break
    except ValueError:
        print("Ошибка, некорректный ввод, введите значения снова")

"""Блок вычисления"""
NewNumber = ""
while Number>0:
    NewNumber = str(Number % CountSystem)+NewNumber
    Number //= CountSystem
print(f"В заданной СС({CountSystem}) число будет выглядеть так: ", NewNumber)
