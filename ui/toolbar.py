from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QSpinBox, QMessageBox
from PyQt6.QtGui import QIcon

class ToolbarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        
    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        
        # 端口设置
        port_label = QLabel("端口:")
        self.port_input = QSpinBox()
        self.port_input.setRange(1, 65535)
        self.port_input.setValue(50213)  # 默认端口
        layout.addWidget(port_label)
        layout.addWidget(self.port_input)
          # 添加设置按钮
        self.settings_btn = QPushButton("设置")
        self.settings_btn.setIcon(QIcon.fromTheme("configure"))
        layout.addWidget(self.settings_btn)
        
        # 添加启动/停止按钮
        self.start_stop_btn = QPushButton("启动服务")
        layout.addWidget(self.start_stop_btn)
        
        layout.addStretch()
        
        # 连接信号槽
        self.start_stop_btn.clicked.connect(self.on_start_stop_clicked)
        self.settings_btn.clicked.connect(self.on_settings_clicked)
        self.port_input.valueChanged.connect(self.on_port_changed)
        
    def get_port(self):
        return self.port_input.value()
        
    def toggle_service_button(self):
        """切换服务按钮状态"""
        if self.start_stop_btn.text() == "启动服务":
            self.start_stop_btn.setText("停止服务")
            return True
        else:
            self.start_stop_btn.setText("启动服务")
            return False
        
    def on_start_stop_clicked(self):
        """处理启动/停止按钮点击"""
        if self.start_stop_btn.text() == "启动服务":
            self.start_stop_btn.setText("停止服务")
        else:
            self.start_stop_btn.setText("启动服务")
            
    def on_settings_clicked(self):
        """处理设置按钮点击"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("设置功能正在开发中...")
        msg.setWindowTitle("设置")
        msg.exec()
        
    def on_port_changed(self, value):
        """处理端口值改变"""
        print(f"端口已更改为: {value}")  # 可以替换为实际的处理逻辑
