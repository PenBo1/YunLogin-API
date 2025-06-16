import sys
import logging
from PyQt6.QtWidgets import QApplication
from ui import MainWindow

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_app_style(app):
    """设置应用程序样式"""
    app.setStyle('Fusion')
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f5f5f5;
        }
        QPushButton {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #0056b3;
        }
        QPushButton:pressed {
            background-color: #004085;
        }
        QListWidget {
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: white;
        }
        QTextEdit {
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: white;
        }
        QTabWidget::pane {
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: white;
        }
        QTabBar::tab {
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            padding: 8px 16px;
            margin-right: 2px;
        }
        QTabBar::tab:selected {
            background-color: white;
            border-bottom: 1px solid white;
        }
        QStatusBar {
            background-color: #f8f9fa;
            color: #6c757d;
        }
    """)

def main():
    app = QApplication(sys.argv)
    setup_app_style(app)
    
    window = MainWindow()
    window.show()
    
    return app.exec()

if __name__ == '__main__':
    sys.exit(main())
