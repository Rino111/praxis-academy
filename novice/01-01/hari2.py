
fruits = ["duren", "salak", "mangga", "kelapa"]

# print (fruits.index("kelapa"))
print (fruits[2])
print(f"Semua buah: ada {len(fruits)} buah")
for b in fruits:
    print (b)
fruits.insert(2, "jeruk")
print(fruits)
del fruits[3]
print (fruits)
print (fruits[1:5])
f = fruits.pop(1)
print(f)
print (fruits.count("duren"))
print (fruits.index("kelapa"))




