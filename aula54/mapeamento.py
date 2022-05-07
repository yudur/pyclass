from dados import products, people


def increase_price(p):
    p["valor"] = round(p["valor"] * 1.5, 2)
    return p


new_products = map(increase_price, products)
new_names = map(lambda pes: [pes["nome"], pes["idade"]], people)

for new_prices in new_products:
    print(new_prices)

print()

for new_names, age in new_names:
    print(f'nome: {new_names} \n\tidade: {age}')
    print()

