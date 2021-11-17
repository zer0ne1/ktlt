import math
from rich import console
from rich.console import Console
from rich.table import Table
from SinhVien import SinhVien


class QuanLySinhVien:
    listSinhVien = []

    # Hàm tạo ID tăng dần cho nhân viên

    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        # Khởi tạo một sinh viên mới
        idClass = input("Nhập mã lớp: ")
        id = input("Nhập mã sinh viên: ")
        name = input("Nhập họ tên sinh viên: ")
        birthday = input("Nhập ngày sinh: ")
        score = input("Nhập điểm trung bình: ")
        
        sv = SinhVien(idClass, id, name, birthday, score)
        self.listSinhVien.append(sv)

    # def updateSinhVien(self, ID):
    #     # Tìm kiếm sinh viên trong danh sách listSinhVien
    #     sv:SinhVien = self.findByID(ID)
    #     # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
    #     if (sv != None):
    #         # nhập thông tin sinh viên
    #         name = input("Nhap ten sinh vien: ")
    #         sex = input("Nhap gioi tinh sinh vien: ")
    #         age = int(input("Nhap tuoi sinh vien: "))
    #         diemToan = float(input("Nhap diem toan: "))
    #         diemLy = float(input("Nhap diem Ly: "))
    #         diemHoa = float(input("Nhap diem Hoa: "))
    #         # cập nhật thông tin sinh viên
    #         sv._name = name
    #         sv._sex = sex
    #         sv._age = age
    #         sv._diemToan = diemToan
    #         sv._diemLy = diemLy
    #         sv._diemHoa = diemHoa
    #         self.tinhDTB(sv)
    #         self.xepLoaiHocLuc(sv)
    #     else:
    #         print("Sinh vien co ID = {} khong ton tai.".format(ID))

    # Hàm sắp xếp danh sach sinh vien theo ID tăng dần
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    #Hàm sắp xếp danh sach sinh vien theo tên tăng dần
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    # Hàm sắp xếp danh sach sinh vien theo điểm TB tăng dần
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    # Hàm tìm kiếm sinh viên theo ID
    # Trả về một sinh viên
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult

    # Hàm tìm kiếm sinh viên theo tên
    # Trả về một danh sách sinh viên
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    # Hàm xóa sinh viên theo ID
    def deleteById(self, ID):
        isDeleted = False
        # tìm kiếm sinh viên theo ID
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    # Hàm tính điểm TB cho sinh viên
    def tinhDTB(self, sv:SinhVien):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
        # làm tròn điểm trung binh với 2 chữ số thập phân
        sv._diemTB = math.ceil(diemTB * 100) / 100

    #Hàm xếp loại học lực cho nhân viên
    def xepLoaiHocLuc(self, sv:SinhVien):
        for i in range(len(sv._score)):
            if (sv._score >= 8):
                print("Số sinh viên loại giỏi là: " + len(sv._score>=8)) 
            elif (sv._score >= 6.5):
                print("Số sinh viên loại khá là: " + len(sv._score>=6.5))
            elif (sv._score >= 5):
                print("Số sinh viên loại trung bình là: " + len(sv._score>=5))
            else:
                print("Số sinh viên loại yếu là: " + len(sv._score))

    # Hàm hiển thị danh sách sinh viên ra màn hình console
    def showSinhVien(self, listSV):
        console = Console()
        table = Table(title = "Danh sách sinh viên")
        table.add_column("Mã lớp")
        table.add_column("Mã sinh viên")
        table.add_column("Họ và tên")
        table.add_column("Ngày sinh")
        table.add_column("Điểm trung bình tích lũy")
        if (listSV.__len__() > 0):
            for sv in listSV:
                table.add_row(sv._idClass, sv._id, sv._name, sv._birthday, sv._score)
                console.print(table)

    # Hàm trả về danh sách sinh viên hiện tại
    def getListSinhVien(self):
        return self.listSinhVien