from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog,QColorDialog,QApplication,QTextEdit,QFontDialog,QDialog,QWidget,QPushButton
from PyQt5.QtPrintSupport import QPageSetupDialog,QPrintDialog,QPrinter
from PyQt5.QtGui import QIcon
import sys

class Ui_test:
    def __init__(self):
        self.creat_info()
        self.printer=QPrinter()

    def creat_info(self):
        self.w=QWidget()
        self.w.setGeometry(400,400,500,500)
        self.w.setWindowTitle('模拟打印机')
        self.w.setWindowIcon(QIcon('res/nene.png'))
        self.creat_res()
        self.w.show()

    def creat_res(self):
        self.t1=QTextEdit(self.w)
        self.t1.setGeometry(15,15,300,400)
        self.B_openfile=QPushButton('打开文件',self.w)
        self.B_openfile.setGeometry(350,15,100,30)
        self.B_openmorefile=QPushButton('打开多文件',self.w)
        self.B_openmorefile.setGeometry(350,65,100,30)
        self.B_change_font=QPushButton('修改字体',self.w)
        self.B_change_font.setGeometry(350,115,100,30)
        self.B_change_color=QPushButton('修改颜色',self.w)
        self.B_change_color.setGeometry(350,165,100,30)
        self.save_file=QPushButton('保存文件',self.w)
        self.save_file.setGeometry(350,215,100,30)
        self.set_page=QPushButton('页面设置',self.w)
        self.set_page.setGeometry(350,265,100,30)
        self.print_file=QPushButton('文件打印',self.w)
        self.print_file.setGeometry(350,315,100,30)
        self.clear_file=QPushButton('清除文本',self.w)
        self.clear_file.setGeometry(350,365,100,30)
        self.config()

    def config(self):
        self.B_openfile.clicked.connect(self.open_file)
        self.B_openmorefile.clicked.connect(self.open_files)
        self.B_change_color.clicked.connect(self.change_color)
        self.B_change_font.clicked.connect(self.change_font)
        self.clear_file.clicked.connect(self.clear_all)
        self.save_file.clicked.connect(self.save_files)
        self.set_page.clicked.connect(self.page_config)
        self.print_file.clicked.connect(self.print_files)

    def clear_all(self):
        self.t1.clear()

    def open_file(self):
        files=QFileDialog.getOpenFileName(self.w,'打开本地文件')
        if files[0]:
            with open(files[0],mode='r',encoding='gb18030',errors='ignore') as f:
                self.t1.setText(f.read())

    def open_files(self):#此处获取得是多个文件，返回得是文件列表
        files=QFileDialog.getOpenFileNames(self.w,'打开本地文件')
        print(files)
        if files[0]:
            for file in files[0]:
                with open(file,mode='r',encoding='gb18030',errors='ignore') as f:
                    self.t1.append(f.read())

    def change_font(self):
        fo,b=QFontDialog.getFont()
        if b:
            self.t1.setCurrentFont(fo)

    def change_color(self):
        co=QColorDialog.getColor()
        if co.isValid():
            self.t1.setTextColor(co)

    def save_files(self):
        file=QFileDialog.getSaveFileName(self.w,'保存文件')
        if file[0]:
            with open(file[0],mode='r',encoding='gb18030',errors='ignore') as f:
                f.write(self.t1.toPlainText())

    def page_config(self):
        page_set=QPageSetupDialog(self.printer,self.w)
        page_set.exec_()

    def print_files(self):
        page_print=QPrintDialog(self.w)
        if QDialog.Accepted==page_print.exec_():
            self.t1.print(self.printer)

ap=QApplication(sys.argv)
u=Ui_test()
sys.exit(ap.exec_())
