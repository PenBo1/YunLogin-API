from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
import logging

class LogTab(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._setup_logging()
        
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)
        
    def _setup_logging(self):
        """配置日志处理"""
        class QTextEditLogger(logging.Handler):
            def __init__(self, widget):
                super().__init__()
                self.widget = widget
                self.widget.setReadOnly(True)

            def emit(self, record):
                msg = self.format(record)
                self.widget.append(msg)

        log_handler = QTextEditLogger(self.log_text)
        log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(log_handler)
        
    def clear_logs(self):
        """清空日志"""
        self.log_text.clear()
