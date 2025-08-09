def even_generator(limit):
    for n in range(2,limit+1,2):
        yield n

for n in even_generator(10):
    print(n)

g1 = even_generator(10)
g2 = even_generator(20)
print(next(g1))
print(next(g2))

print(g1.gi_code is g2.gi_code)
