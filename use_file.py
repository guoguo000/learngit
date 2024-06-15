# encoding: utf-8
# @File  : use_file.py
# @Author: guoliyan
# @Desc : 
# @Date  :  2024/06/15


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == 'main':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
