text_tuple = (1, 2, 3, 4, 5)
text_tuple = list(text_tuple)
text_tuple[-1] = 654321
text_tuple = tuple(text_tuple)

print(text_tuple)
