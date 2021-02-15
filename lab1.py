import random
import tkinter
import time
import threading

l = 10
n = 100

WIDTH = 800
HEIGHT = 150

def partition(arr, low, high): 
    i = (low-1)
    pivot = arr[high]
  
    for j in range(low, high): 
  
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
 
  
def quickSort(arr, low, high):

    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        pi = partition(arr, low, high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

def draw_list(l, c: tkinter.Canvas):
    w = c.winfo_width() / len(l) * 750
    min_ = l.index(min(l))
    max_ = l.index(max(l))
    for i in range(len(l)):
        c.create_rectangle(i * w, HEIGHT, (i + 1) * w, HEIGHT - l[i], fill='yellow')
    
    c.create_rectangle(min_ * w, HEIGHT, (min_ + 1) * w, HEIGHT - l[min_], fill='blue')
    c.create_rectangle(max_ * w, HEIGHT, (max_ + 1) * w, HEIGHT -l[max_], fill='red')


def B_arr(l: list):
    array = l.copy()
    res = list()
    while len(array) > 0:
        res.append(max(array))
        array.remove(max(array))
        res.append(min(array))
        array.remove(min(array))
    return res

def C_arr(l: list):
    temp = B_arr(l)
    temp.reverse()
    res = B_arr(l)
    res += temp
    return res

def A_arr1(l: list):
    array = l.copy()
    res = list()
    while len(array) > 0:
        res.append(max(array))
        array.remove(max(array))
        res.insert(0, max(array))
        array.remove(max(array))
    return res

def A_arr2(l: list):
    array = l.copy()
    res = list()
    while len(array) > 0:
        res.append(min(array))
        array.remove(min(array))
        res.insert(0, min(array))
        array.remove(min(array))
    return res


class App:
    def __init__(self, l):
        self.window = tkinter.Tk()
        self.list = l
        self.init_canvas()
        self.sort_canvas()
        self.A()
        self.B()
        self.C()

    def start(self):
        self.window.mainloop()

    def init_canvas(self):
        text = tkinter.Label(self.window, text="Init array")
        text.pack()
        self.canvas_ = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvas_.grid_location(400, 0) 
        self.canvas_.pack()
        draw_list(self.list, self.canvas_)

        self.window.update()

    def sort_canvas(self):
        text = tkinter.Label(self.window, text="Sorted array")
        text.pack()
        self.canvas_sort = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvas_sort.pack()
        s = self.list.copy()
        quickSort(s, 0, n - 1 - l)
        draw_list(s, self.canvas_sort)

        self.window.update()


    def A(self):
        text = tkinter.Label(self.window, text="A) 1")
        text.pack()
        self.canvasA1 = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)
        s = A_arr1(self.list)
        self.canvasA1.pack()
        draw_list(s, self.canvasA1)

        text = tkinter.Label(self.window, text="A) 2")
        text.pack()
        self.canvasA2 = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)
        s = A_arr2(self.list)
        self.canvasA2.pack()
        draw_list(s, self.canvasA2)

    def B(self):
        text = tkinter.Label(self.window, text="B)")
        text.pack()
        self.canvasB = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvasB.pack()
        arr = B_arr(self.list)
        draw_list(arr, self.canvasB)
     
    def C(self):
        text = tkinter.Label(self.window, text="C)")
        text.pack()
        self.canvasC = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvasC.pack()
        arr = C_arr(self.list)
        draw_list(arr, self.canvasC)

if __name__ == "__main__":
    array = list(map(lambda x: random.randint(l, n), range(l, n)))

    app = App(array)

    app.start()