name_and_city: str = "Adva Hamershtein, beer sheva"
print(name_and_city.strip())
# a
print(len(name_and_city))
# b
print(name_and_city.upper())
# c
print(name_and_city.lower())
# d
print('startswith("Adva") ?', name_and_city.startswith(""))
# e
print('endswith("Hamershtein") ?', name_and_city.endswith(""))
# f
print(name_and_city.split())
# g
print(name_and_city.replace(" ", "*"))
print(name_and_city.split("*"))
# h
print(name_and_city.center(50, '='))
# i
print("  [4:]", name_and_city[4:])
# j
print("  [:5]", name_and_city[:5])
# k
print("  [::2]", name_and_city[::2])
# l
print('title: ', name_and_city.title())
