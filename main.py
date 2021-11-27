from manage import Manage
from sort import Sort
from search import Search
from statistic import Statistic
from menu import mainMenu, sortMenu1, keyMenu, searchMenu1, statisticMenu


ma = Manage()
so = Sort()
se = Search()
stat = Statistic()
while (1==1):
    mainMenu()
    
    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("Thêm mới hồ sơ: ")
        ma.importStudent()
        print("Thêm mới thành công: ")

    elif (key == 2):
        if (ma.quantityStudent() > 0):
            ma.showStudent(ma.getListStudent())
        else:
            print("Danh sách sinh viên trống!")

    elif (key == 3):
        sortMenu1()
        keySub1 = int(input("Nhập tùy chọn: "))
        if(keySub1 == 1):
            keyMenu()
            keySub2 = int(input("Nhập tùy chọn: "))
            ma.showStudent(so.selectionSort(keySub2))
        elif(keySub1 == 2):
            keyMenu()
            keySub2 = int(input("Nhập tùy chọn: "))
            ma.showStudent(so.insertionSort(keySub2))
        elif(keySub1 == 3):
            keyMenu()
            keySub2 = int(input("Nhập tùy chọn: "))
            ma.showStudent(so.bubbleSort(keySub2))
        elif(keySub1 == 4):
            keyMenu()
            keySub2 = int(input("Nhập tùy chọn: "))
            ma.showStudent(so.quickSort(keySub2))
            
    elif (key == 4):
        searchMenu1()
        keySub1 = int(input("Nhập tùy chọn: "))
        if(keySub1 == 1):
            keyMenu()
            keySub2 = int(input("Nhập tùy chọn: "))
            if(keySub2 == 2):
                keySearch = int(input("Nhập: "))
                ma.showStudent(se.linearSearch(keySub2, keySearch))
            else:
                keySearch = str(input("Nhập: "))
                ma.showStudent(se.linearSearch(keySub2, keySearch))
        if(keySub1 == 2):
            sortMenu1()
            keySub1 = int(input("Nhập tùy chọn: "))
            if(keySub1 == 1):
                keyMenu()
                keySub2 = int(input("Nhập tùy chọn: "))
                keySearch = str(input("Nhập: "))
                ma.showStudent(se.binarySearch(so.selectionSort(keySub2), keySearch))
            elif(keySub1 == 2):
                keyMenu()
                keySub2 = int(input("Nhập tùy chọn: "))
                keySearch = str(input("Nhập: "))
                ma.showStudent(se.binarySearch(so.insertionSort(keySub2), keySearch))
            elif(keySub1 == 3):
                keyMenu()
                keySub2 = int(input("Nhập tùy chọn: "))
                keySearch = str(input("Nhập: "))
                ma.showStudent(se.binarySearch(so.bubbleSort(keySub2), keySearch))
            elif(keySub1 == 4):
                keyMenu()
                keySub2 = int(input("Nhập tùy chọn: "))
                keySearch = str(input("Nhập: "))
                ma.showStudent(se.binarySearch(so.quickSort(keySub2), keySearch))
            
    elif (key == 5):
        statisticMenu()
        keyStat = int(input("Nhập tùy chọn: "))
        if(keyStat == 1):
            stat.showQuantity(stat.quantity())

    elif (key == 6):
        print("Ban da chon thoat chuong trinh!")
        break

    else:
        print("nKhong co chuc nang nay!")
        print("nHay chon chuc nang trong hop menu.")