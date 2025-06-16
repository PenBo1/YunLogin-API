from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget,
                           QSystemTrayIcon, QMenu, QMessageBox, QApplication)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction
import os
from .toolbar import ToolbarWidget
from .environments_tab import EnvironmentsTab
from .log_tab import LogTab
from .about_tab import AboutTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("云指纹浏览器 RPA")
        self.setMinimumSize(900, 600)
        
        # 设置应用图标
        icon_path = os.path.join(os.path.dirname(__file__), "icons", "logo.png")
        self.app_icon = QIcon(icon_path)
        self.setWindowIcon(self.app_icon)
        
        # 创建系统托盘
        self.setup_system_tray()
        
        # 创建主窗口部件和布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        
        # 添加工具栏
        self.toolbar = ToolbarWidget()
        main_layout.addWidget(self.toolbar)
        
        # 创建选项卡组件
        tab_widget = QTabWidget()
        
        # 添加环境列表页
        self.environments_tab = EnvironmentsTab()
        tab_widget.addTab(self.environments_tab, "环境列表")
        
        # 添加日志页
        self.log_tab = LogTab()
        tab_widget.addTab(self.log_tab, "日志")
        
        # 添加关于页
        self.about_tab = AboutTab()
        tab_widget.addTab(self.about_tab, "关于")
        
        main_layout.addWidget(tab_widget)
        
        # 状态栏
        self.statusBar().showMessage('就绪')
        
    def setup_system_tray(self):
        """设置系统托盘"""
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.app_icon)
        
        # 创建托盘菜单
        tray_menu = QMenu()
        
        # 添加菜单项
        show_action = QAction("显示主窗口", self)
        show_action.triggered.connect(self.show)
        
        hide_action = QAction("最小化到托盘", self)
        hide_action.triggered.connect(self.hide)
        
        quit_action = QAction("退出", self)
        quit_action.triggered.connect(self.close_application)
        
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addSeparator()
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        # 连接托盘图标的双击事件
        self.tray_icon.activated.connect(self.tray_icon_activated)
        
    def closeEvent(self, event):
        """重写关闭事件"""
        if self.tray_icon.isVisible():
            QMessageBox.information(
                self, "提示",
                "程序将继续在系统托盘运行，右键点击托盘图标可以退出程序。"
            )
            self.hide()
            event.ignore()
            
    def tray_icon_activated(self, reason):
        """处理托盘图标的激活事件"""
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()
                
    def close_application(self):
        """完全退出应用程序"""
        self.tray_icon.hide()
        QApplication.quit()
