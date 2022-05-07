from dados import products, people


def filtra(p):
    if p["valor"] > 50:
        return True


# filtered out the products that cost more than 50 reais
new_list = filter(filtra, products)

for expensive in new_list:
    print(expensive)

# filtering only those over 18 years old
of_age = filter(lambda i: i["idade"] >= 18, people)

print('\n')

for adults in of_age:
    print(adults)
