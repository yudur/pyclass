"""
Tuplas em python
"""
text_tuple1 = (1, 2, '<3', 'Yudi', 'Yudi Duarte')
text_tuple2 = 1, 2, 3, 4, 5

print(text_tuple1[4], text_tuple1[2])
print(text_tuple2)


for x in text_tuple1:
    print(x)


print(text_tuple1[0:3])


text_tuple3 = text_tuple1 + text_tuple2
print(text_tuple3)


l1, l2, l3, *_ = text_tuple3
print(l3)
