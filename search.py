from manage import Manage


class Search:
    ma = Manage()
    # Tìm kiếm sinh viên:
    # Chọn khóa
    def selectKeySearch(self, line, val):
        if(val == 1):
            return str(line._idClass)
        if(val == 2):
            return int(line._id)
        if(val == 3):
            return str(line._name)
        if(val == 4):
            return str(line._birthday)
        if(val == 5):
            return str(line._score)

    # Tìm kiếm tuần tự:
    def linearSearch(self, val, key):
        lst = []
        lines = self.ma.getListStudent()
        for line in lines:
            if type(key) == int:
                if key == self.selectKeySearch(line, val):
                    lst.append(line)
            else:
                if key in self.selectKeySearch(line, val):
                    lst.append(line)
        return lst

    # Nhị phân:
    def binarySearch(self, lines, key):
        lst = self.list.remove()
        def binarysearch(arr, low, high, x):
            if high >= low:
                mid = (high + low) // 2
                if x.title() in arr[mid].title():
                    lst.append(arr[mid])
                    arr.pop(mid)
                    return binarysearch(arr, low, high-1, x)
                elif arr[mid].title() > x.title():
                    return binarysearch(arr, low, mid - 1, x)
                else:
                    return binarysearch(arr, mid + 1, high, x)
            else:
                return -1

        binarysearch(lines, 0, len(lines)-1, key)
        return lst