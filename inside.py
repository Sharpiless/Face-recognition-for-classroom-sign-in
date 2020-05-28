
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Camera.in_main_gui import MainUi

sys.path.append('./')

class MonitorWindows(MainUi):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":

    try:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        App = QApplication(sys.argv)
        monitor_box = MonitorWindows()
        monitor_box.show()
        sys.exit(App.exec_())
    except Exception as e:
        print(e)
    
    input('输入任意键退出')