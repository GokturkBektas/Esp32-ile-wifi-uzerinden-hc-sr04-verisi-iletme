import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow
import socket
import _thread

SERVER_IP = "0.0.0.0"
class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.baslat_button.clicked.connect(self.Calistir)
        self.ui.durdur_button.clicked.connect(self.close)

    def Calistir(self):
        result = self.ui.lineEdit.text()
        SERVER_PORT = int(result)
        def lissen():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((SERVER_IP, SERVER_PORT))
                s.listen()

                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        decoded_data = data.decode()
                        self.ui.textEdit.append(f"{decoded_data}")

        _thread.start_new_thread(lissen, ())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Uygulama()
    win.show()
    sys.exit(app.exec_())
