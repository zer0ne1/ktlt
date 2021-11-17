from QuanLySinhVien import QuanLySinhVien

# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
qlsv = QuanLySinhVien()
while (1==1):
    print("THỰC TẬP KỸ THUẬT LẬP TRÌNH")
    print("*************************MENU**************************")
    print("**  1. Thêm mới hồ sơ                                **")
    print("**  2. In danh sách                                  **")
    print("**  3. Sắp xếp                                       **")
    print("**  4. Tìm kiếm                                      **")
    print("**  5. Thống kê                                      **")
    print("**  6. Thoát                                         **")
    print("*******************************************************")
    
    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("Thêm mới hồ sơ: ")
        qlsv.nhapSinhVien()
        print("Thêm mới thành công: ")

    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống!")

    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("n3. Xoa sinh vien.")
            print("nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("nSinh vien co id = ", ID, " da bi xoa.")
            else:
                print("nSinh vien co id = ", ID ," khong ton tai.")
        else:
            print("nSanh sach sinh vien trong!")

    elif (key == 4):
        print("Thống kê:")
        if (qlsv.soLuongSinhVien() > 0):
            print("n4. Tim kiem sinh vien theo ten.")
            print("nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("nSanh sach sinh vien trong!")

    elif (key == 5):
        qlsv.xepLoaiHocLuc()
        # if (qlsv.soLuongSinhVien() > 0):
        #     print("n5. Sap xep sinh vien theo diem trung binh (GPA).")
        #     qlsv.sortByDiemTB()
        #     qlsv.showSinhVien(qlsv.getListSinhVien())
        # else:
        #     print("nSanh sach sinh vien trong!")

    elif (key == 6):
        print("nBan da chon thoat chuong trinh!")
        break

    else:
        print("nKhong co chuc nang nay!")
        print("nHay chon chuc nang trong hop menu.")