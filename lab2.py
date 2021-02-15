from lab1 import quickSort
import random

RED = '\033[1;31m'
BLUE = '\033[1;34m'
NC = '\033[0;37m'
print(NC)


class Matrix:
    def __init__(self, m, n):
        self.mx = []
        self.m = m
        self.n = n
        self.arr = []
        for _ in range(m):
            self.mx.append([0] * n)

    def random(self):
        self.arr = []
        for i in range(self.m):
            for j in range(self.n):
                val = random.randint(0, 100)
                self.mx[i][j] = val
                self.arr.append(val)
        quickSort(self.arr, 0, len(self.arr) - 1)

    def min(self):
        res = self.mx[0][0]
        for i in range(self.m):
            for j in range(self.n):
                if self.mx[i][j] < res:
                    res = self.mx[i][j]
        return res

    def max(self):
        res = self.mx[0][0]
        for i in range(self.m):
            for j in range(self.n):
                if self.mx[i][j] > res:
                    res = self.mx[i][j]
        return res

    def print(self):
        min_ = self.min()
        max_ = self.max()
        for i in range(self.m):
            for j in range(self.n):
                print("------", end='')
            print()
            print('|', end='')
            for j in range(self.n):
                color = RED if self.mx[i][j] == min_ else BLUE if self.mx[i][j] == max_ else NC
                print("{}{:4}{} |".format(
                    color, str(self.mx[i][j]), NC), end='')
            print()
        for j in range(self.n):
            print("------", end='')
        print()

    def A(self):
        res = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                res.mx[i][j] = self.arr[i * self.n + j]

        res.print()

    def B(self):
        res = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                res.mx[j][i] = self.arr[i * self.m + j]

        res.print()

    def C(self):
        res = Matrix(self.m, self.n)
        arr = mx.arr.copy()
        i = 0
        s = 1
        x = 0
        y = 0
        while len(arr) != 0:
            for _ in range(self.n - i):
                res.mx[y][x] = arr.pop(0)
                x += s
            x -= s
            i += 1
            y += s
            for _ in range(self.m - i):
                res.mx[y][x] = arr.pop(0)
                y += s
            y -= s
            s *= -1
            x += s
        res.print()

    def D(self):
        res = Matrix(self.m, self.n)
        arr = mx.arr.copy()
        arr.reverse()
        i = 0
        s = 1
        x = 0
        y = 0
        while len(arr) != 0:
            for _ in range(self.n - i):
                res.mx[y][x] = arr.pop(0)
                x += s
            x -= s
            i += 1
            y += s
            for _ in range(self.m - i):
                res.mx[y][x] = arr.pop(0)
                y += s
            y -= s
            s *= -1
            x += s
        res.print()

    def E(self):
        res = Matrix(self.m, self.n)
        arr = self.arr.copy()
        s = 1
        x, y = 0, 0
        while len(arr) != 0:
            for _ in range(res.n):
                res.mx[y][x] = arr.pop(0)
                x += s
            x -= s
            s *= -1
            y += 1
        res.print()


mx = Matrix(10, 10)
mx.random()
mx.A()
mx.B()
mx.C()
mx.D()
mx.E()
