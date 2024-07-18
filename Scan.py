import sys
import time
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QImage, QPainter, QColor, QPixmap
from PyQt6.QtCore import QTimer, Qt
import pyautogui

class ScreenCaptureWidget(QLabel):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setGeometry(0, 0, pyautogui.size().width, pyautogui.size().height)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_screen)
        self.timer.start(1000 // 60)  # 60 FPS
        self.show()

    def update_screen(self):
        screen_width, screen_height = pyautogui.size()
        screenshot = pyautogui.screenshot()
        image = QImage(screenshot.tobytes(), screenshot.width, screenshot.height, QImage.Format.Format_RGB32)
        
        painter = QPainter(image)
        pen = painter.pen()
        pen.setColor(QColor('red'))
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawLine(0, screen_height - 1, screen_width, screen_height - 1)
        painter.end()
        
        self.setPixmap(QPixmap.fromImage(image))

    def mousePressEvent(self, event):
        if event.y() >= self.height() - 5:
            QMessageBox.information(self, "Clicked", "Line clicked!")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Screen Capture with Line')
        self.setGeometry(100, 100, 800, 600)

        self.capture_widget = ScreenCaptureWidget()
        self.setCentralWidget(self.capture_widget)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
