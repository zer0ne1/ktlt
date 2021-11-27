from rich.console import Console
from rich.table import Table

from student import Student

class Manage:
    listS = []
    
    def quantityStudent(self):
        with open('data.txt', 'r', encoding="utf-8") as rf:
            lines = rf.readlines()
            return lines.__len__()

    def importStudent(self):
        # Khởi tạo một sinh viên mới
        idClass = input("Nhập mã lớp: ")
        id = input("Nhập mã sinh viên: ")
        name = input("Nhập họ tên sinh viên: ")
        birthday = input("Nhập ngày sinh: ")
        score = input("Nhập điểm trung bình: ")
        st = Student(idClass, id, name, birthday, score)
        self.listS.append(st)
        
        with open('data.txt', 'a', encoding="utf-8") as f:
            f.write("{}, {}, {}, {}, {}\n".format(st._idClass,st._id, st._name, st._birthday, st._score))

    # Hàm hiển thị danh sách sinh viên ra màn hình console dưới dạng bảng

    def showStudent(self, lines):
        console = Console()
        table = Table(title="Danh sách sinh viên")
        table.add_column("Mã lớp")
        table.add_column("Mã sinh viên")
        table.add_column("Họ và tên")
        table.add_column("Ngày sinh")
        table.add_column("Điểm trung bình tích lũy")
        if (len(lines) > 0):
            for line in lines:
                table.add_row(line._idClass, line._id, line._name, line._birthday, line._score)
            console.print(table)
        else:
            print("Not found!")

    # Hàm trả về danh sách sinh viên trong file
    def getListStudent(self):
        lst = []
        with open('data.txt', 'r', encoding="utf-8") as rf:
            lines = rf.readlines()
            for line in lines:
                l = line.split(', ')
                st = Student(l[0], l[1], l[2], l[3], l[4])
                lst.append(st)
        return lst
                

