from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import os
from .version import VERSION, COPYRIGHT

class AboutTab(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 创建滚动区域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        
        # 创建内容容器
        content = QWidget()
        content_layout = QVBoxLayout(content)
        
        # 顶部布局(logo和标题)
        top_layout = QHBoxLayout()
        
        # Logo
        logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(__file__), "icons", "logo.png")
        logo_pixmap = QPixmap(logo_path).scaled(128, 128, Qt.AspectRatioMode.KeepAspectRatio, 
                                              Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        top_layout.addWidget(logo_label)
        
        # 标题和版本信息
        title_layout = QVBoxLayout()
        title = QLabel("""
        <h1 style='margin-bottom: 5px;'>云指纹浏览器 RPA</h1>
        <p style='margin: 0; color: #666;'>版本: {}</p>
        <p style='color: #666;'>专业的浏览器指纹管理与自动化工具</p>
        """.format(VERSION))
        title_layout.addWidget(title)
        top_layout.addLayout(title_layout)
        top_layout.addStretch()
        
        content_layout.addLayout(top_layout)
        content_layout.addWidget(self.create_separator())
        
        # 详细介绍
        about_label = QLabel("""
        <h2>🚀 产品特点</h2>
        <ul>
            <li><b>🔒 专业的指纹管理</b> - 支持详细的浏览器指纹配置，包括系统信息、
            语言、时区、字体等多维度参数设置</li>
            <li><b>🤖 强大的自动化能力</b> - 集成 Selenium 和 Puppeteer，支持多种自动化
            场景</li>
            <li><b>📊 高效的批量处理</b> - 支持环境的批量导入导出，提高工作效率</li>
            <li><b>📝 完整的日志记录</b> - 详细记录所有操作和运行状态，方便追溯和调试</li>
            <li><b>🎨 人性化的界面设计</b> - 支持主题切换，窗口置顶等功能</li>
        </ul>

        <h2>💡 使用教程</h2>
        <ol>
            <li>在工具栏设置云指纹浏览器服务端口</li>
            <li>点击"启动服务"连接到浏览器服务</li>
            <li>在环境列表页面管理您的浏览器环境</li>
            <li>使用内置的自动化工具执行任务</li>
        </ol>

        <h2>🔧 技术支持</h2>
        <p>如果您在使用过程中遇到问题，可以通过以下方式获取帮助：</p>
        <ul>
            <li>📖 查看<a href='https://docs.example.com/guide'>在线文档</a></li>
            <li>💬 加入用户交流群获取帮助</li>
            <li>📧 发送邮件至技术支持</li>
        </ul>
        """)
        about_label.setOpenExternalLinks(True)
        about_label.setTextFormat(Qt.TextFormat.RichText)
        about_label.setWordWrap(True)
        content_layout.addWidget(about_label)
        
        # 版权信息
        copyright_label = QLabel(COPYRIGHT)
        copyright_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyright_label.setStyleSheet("color: #666;")
        content_layout.addWidget(copyright_label)
        
        # 设置滚动区域
        scroll.setWidget(content)
        layout.addWidget(scroll)
        
    def create_separator(self):
        """创建分隔线"""
        separator = QLabel()
        separator.setStyleSheet("""
            background-color: #ddd;
            min-height: 1px;
            max-height: 1px;
        """)
        return separator
