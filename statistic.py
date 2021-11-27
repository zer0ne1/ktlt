from rich.console import Console
from rich.table import Table
from manage import Manage
from search import Search

class Statistic:
    ma = Manage()
    se = Search()
    # Thống kê:
    # Báo cáo số lượng sinh viên theo lớp
    def quantity(self):
        lines = self.ma.getListStudent()
        Dict = dict()
        for line in lines:
            if line._idClass in Dict:
                Dict[line._idClass] +=1
            else:
                Dict[line._idClass] = 1
        return Dict

    def showQuantity(self, Dict):
        console = Console()
        table = Table(title="Số lượng sinh viên theo lớp")
        table.add_column("Mã lớp")
        table.add_column("Số lượng sinh viên")
        for d in Dict:
            table.add_row(str(d), str(Dict.get(d)))
        console.print(table)

    # Tỷ lệ phân loại kết quả học tập theo lớp
    def showClassify(self):
        Dict = dict()
        console = Console()
        table = Table(title="Số lượng sinh viên theo lớp")
        table.add_column("Mã lớp")
        table.add_column("Tỷ lệ sinh viên xuất sắc")
        table.add_column("Tỷ lệ sinh viên giỏi")
        table.add_column("Tỷ lệ sinh viên khá")
        table.add_column("Tỷ lệ sinh viên trung bình")
        table.add_column("Tỷ lệ sinh viên yếu")
        table.add_column("Tổng số sinh viên")
        
    def excellent(self):
        print