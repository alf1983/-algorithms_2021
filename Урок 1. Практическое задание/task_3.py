"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
companies_storage = [
    {
        "name": "Apple",
        "profit": 10087898769
    },
    {
        "name": "Apple1",
        "profit": 22128789
    },
    {
        "name": "Apple2",
        "profit": 134348789
    },
    {
        "name": "Apple3",
        "profit": 152368789
    },
    {
        "name": "Apple4",
        "profit": 107698789
    },
    {
        "name": "Apple5",
        "profit": 145823789
    },
    {
        "name": "Apple6",
        "profit": 165128789
    },
    {
        "name": "Apple7",
        "profit": 1342348789
    },
    {
        "name": "Apple9",
        "profit": 10567789
    },
    {
        "name": "Microsoft",
        "profit": 1342348789
    },
]  # O(1)


def three_best_companies1(companies):
    max_profit_companies = []  # O(1)
    while len(max_profit_companies) < 3:  # O(1) т.к цикл до 3 (константа)
        max_profit_company = companies[0]  # O(1)
        for company in companies:  # O(N)
            if company["profit"] > max_profit_company["profit"]:  # O(1)
                max_profit_company = company  # O(1)
        max_profit_companies.append(max_profit_company)  # O(1)
        companies.remove(max_profit_company)  # O(N)
    return max_profit_companies  # O(1)


def three_best_companies2(companies):
    profits = []  # O(1)
    max_profit_companies = []  # O(1)
    for company in companies:  # O(N)
        profits.append(company["profit"])  # O(1)
    profits_sorted = sorted(profits, reverse=True)  # O(N log N)
    start = 0  # O(1)
    for index in range(3):  # O(1)
        max_profit_companies.append(companies[profits.index(profits_sorted[index], start)])  # O(N)
        start = profits.index(profits_sorted[index], start) + 1  # O(1)
    return max_profit_companies  # O(1)


print(three_best_companies2(companies_storage))
print(three_best_companies1(companies_storage))
"""
Сложность функции three_best_companies1 O(N)
Сложность three_best_companies2 - O(N log N)
Первое решение лучше так как в нотации О-большое линейная а во втором решении линейно-лагарифмическая что "хуже"
"""
