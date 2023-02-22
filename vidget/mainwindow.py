# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(s, qapplication, *args, **kwargs):
        super().__init__()
        s._qapplication = qapplication
        s.screen_starting_geometry()

    def screen_starting_geometry(s, x_factor=0.8, y_factor=0.8, primary=True):
        for screen in s._qapplication.screens():

            x = screen.geometry().left()
            y = screen.geometry().top()
            w = screen.geometry().width()
            h = screen.geometry().height()

            bleed_x = (w - (w * x_factor)) * 0.5
            bleed_y = (h - (h * y_factor)) * 0.5

            geo = int(bleed_x) + x, int(bleed_y) + y, int(w * x_factor) or 1280, int(h * y_factor) or 768

            if primary and screen == QtGui.QGuiApplication.primaryScreen():
                s.setGeometry(*geo)
                return

            elif not primary and screen != QtGui.QGuiApplication.primaryScreen():
                s.setGeometry(*geo)
                return

        s.setGeometry(0, 0, 1280, 768)  # fallback


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(qapplication=app)
    window.show()
    sys.exit(app.exec())
