from manage import Manage
from datetime import date

class Sort:
    ma = Manage()
    # Sắp xếp sinh viên:
    # Chọn khóa
    def selectKeySort(self, line, val):
        if(val == 1):
            return str(line._idClass)
        if(val == 2):
            return int(line._id)
        if(val == 3):
            l = line._name.split(' ')
            for i in range(len(l)):
                return ''.join([str(l[2]), str(l[1]), str(l[0])])
        if(val == 4):
            l = line._birthday.split('-')
            return date(int(l[2]), int(l[1]), int(l[0]))
        if(val == 5):
            return float(line._score)

    def sortKey(self, key1, key2):
        return key1 < key2

    # Chọn
    def selectionSort(self, val):
        lines = self.ma.getListStudent()
        for i in range(len(lines)):
            min_idx = i
            for j in range(i+1, len(lines)):
                if self.sortKey(self.selectKeySort(lines[j], val), self.selectKeySort(lines[min_idx], val)):
                    min_idx = j
            lines[i], lines[min_idx] = lines[min_idx], lines[i]
        return lines

    # Chèn
    def insertionSort(self, val):
        lines = self.ma.getListStudent()
        for i in range(1, len(lines)):
            key = lines[i]
            j = i-1
            while j >= 0 and self.sortKey(self.selectKeySort(key, val), self.selectKeySort(lines[j], val)):
                lines[j+1] = lines[j]
                j -= 1
            lines[j+1] = key
        return lines

    # Nổi bọt
    def bubbleSort(self, val):
        lines = self.ma.getListStudent()
        n = len(lines)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.sortKey(self.selectKeySort(lines[j+1], val), self.selectKeySort(lines[j], val)):
                    lines[j], lines[j + 1] = lines[j + 1], lines[j]
        return lines

    # Quick Sort
    def quickSort(self, val):
        lines = self.ma.getListStudent()

        def partition(arr, low, high):
            i = (low-1)
            pivot = arr[high]
            for j in range(low, high):
                if self.sortKey(self.selectKeySort(arr[j], val), self.selectKeySort(pivot, val)):
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i+1)

        def quicksort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:
                pi = partition(arr, low, high)
                quicksort(arr, low, pi-1)
                quicksort(arr, pi+1, high)
        quicksort(lines, 0, len(lines)-1)
        return lines