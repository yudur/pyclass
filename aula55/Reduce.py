from functools import reduce
from dados import products, people, lista

accumulated_list = reduce(lambda ac, i: i + ac, lista, 0)
print(accumulated_list)


accumulated_products = reduce(lambda ac, p: p["valor"] + ac, products, 0)
print(round(accumulated_products / len(products), 2))


sum_of_ages = reduce(lambda ac, i: i["idade"] + ac, people, 0)
print(round(sum_of_ages / len(people)))
