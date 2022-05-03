shopping_cart = []

shopping_cart.append(('cama box', 218.25))
shopping_cart.append(('camiseta', 55.00))
shopping_cart.append(('pingente', 15.99))

value_of_products = [float(value_of_products[1]) for value_of_products in shopping_cart]

print(f'você deve pagar: {sum(value_of_products)}')
