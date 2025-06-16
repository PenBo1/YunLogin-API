from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget

class EnvironmentsTab(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 工具栏
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        
        # 添加环境按钮
        self.add_env_btn = QPushButton("添加环境")
        toolbar_layout.addWidget(self.add_env_btn)
        
        # 导入/导出按钮
        self.import_btn = QPushButton("导入")
        self.export_btn = QPushButton("导出")
        toolbar_layout.addWidget(self.import_btn)
        toolbar_layout.addWidget(self.export_btn)
        
        toolbar_layout.addStretch()
        layout.addWidget(toolbar)
        
        # 环境列表
        self.env_list = QListWidget()
        layout.addWidget(self.env_list)
        
    def add_environment(self, env_data):
        """添加环境到列表"""
        self.env_list.addItem(env_data["name"])
        
    def get_selected_environment(self):
        """获取选中的环境"""
        return self.env_list.currentItem()
