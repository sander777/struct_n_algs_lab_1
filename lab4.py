import random

class Set:
    def __init__(self, *arr):
        self.set = []
        for i in arr:
            is_in = False
            for j in self.set:
                if i == j:
                    is_in = True
            if not is_in:
                self.set.append(i)

    def add(self, *el):
        for i in el:
            is_in = False
            for j in self.set:
                if i == j:
                    is_in = True
            if not is_in:
                self.set.append(i)

    def __add__(self, o):
        res = Set(*self.set)
        res.add(*o.set)
        return res

    def __sub__(self, o):
        res = Set(*self.set)
        for i in o.set:
            try:
                res.set.remove(i)
            except ValueError:
                continue
        return res

    def __and__(self, o):
        return (self - (self - o))

    def sim_sub(self, o):
        return (self - o) + (o - self)

    def print(self):
        for i in self.set:
            print(f"{i} ", end='')
        print()
    
    def __str__(self):
        res = ""
        for i in self.set:
            res += f"{i} "
        return res

arr1, arr2 = [], []

for i in range(random.randint(5, 10)):
    arr1.append(random.randint(0, 20))

for i in range(random.randint(5, 10)):
    arr2.append(random.randint(0, 20))

s1, s2 = Set(*arr1), Set(*arr2)

print("Set 1 (A): ", end='')
s1.print()
print("Set 2 (B): ", end='')
s2.print()

print(f"A U B = {s1 + s2}")
print(f"A \ B = {s1 - s2}")
print(f"B \ A = {s2 - s1}")
print(f"A ∩ B = {s1 & s2}")
print(f"A △ B = {s1.sim_sub(s2)}")
