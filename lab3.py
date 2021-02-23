import random, lab1


RED = '\033[1;31m'
BLUE = '\033[1;34m'
NC = '\033[0;37m'
print(NC)

n, a, b = 5, 0, 100

N = n**3

cube = []
m, M = b, a
for _ in range(N):
    r = random.randint(a, b)
    cube.append(r)
    if r > M:
        M = r
    if r < m:
        m = r

def print_cube():
    for i in range(n):
        for j in range(n):
            for _ in range(n):
                print("------", end='')
            print()
            print('|', end='')
            for k in range(n):
                e = cube[i * n**2 + (n - j - 1) * n + k]
                color = RED if e == m else BLUE if e == M else NC 
                print("{}{:5}{}|".format(color, e, NC), end='')
            print()
        for _ in range(n):
                print("------", end='')
        print('\n')

print_cube()
lab1.quickSort(cube, 0, N-1)
print_cube()