import random

# a
list1: list[bool] = [random.choice([True, False]) for i in range(3)]
# b
true = all(list1)
print("all true-", all({true}))
# c
true = any(list1)
print("any true-", any({true}))
# d
false = all(list1)
print("any false-", all({false}))
# e
false = any(list1)
print("any false-", any({false}))
# f
bool1: list[int] = [random.choice([2, 1, 0, -1, -2]) for _ in range(5)]
# g
bool2 = [random.randint(-2, 2) for _ in range(5) if _ != 0]
print(f"different_0{bool2}")
# h
any_0 = any(bool2)
print("any 0-", any({any_0}))
# i
all_0 = all(bool1)
print("all 0-", all({all_0}))
# j
any_0 = any(bool1)
print("any 0-", any({any_0}))
