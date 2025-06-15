import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import os
from pathlib import Path
from typing import Optional, Union
import sys
import json
from datetime import datetime

class Logger:
    """
    高级日志封装类
    
    功能特点：
    - 支持控制台和文件日志
    - 多日志级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    - 日志文件轮转 (按大小或时间)
    - 支持 JSON 格式日志
    - 线程安全
    - 彩色控制台输出
    
    示例用法:
    >>> log = Logger.get_logger(name="my_app")
    >>> log.info("系统启动")
    >>> log.error("发生错误", extra={"user": "admin"})
    """
    
    # 颜色配置
    COLOR_MAP = {
        'DEBUG': '\033[36m',    # 青色
        'INFO': '\033[32m',     # 绿色
        'WARNING': '\033[33m',  # 黄色
        'ERROR': '\033[31m',    # 红色
        'CRITICAL': '\033[1;31m', # 红色加粗
        'RESET': '\033[0m'      # 重置颜色
    }
    
    _instances = {}
    
    def __init__(
        self,
        name: str = "default",
        log_level: str = "INFO",
        log_file: Optional[Union[str, Path]] = None,
        file_log_level: str = "DEBUG",
        console_log_level: str = "INFO",
        max_bytes: int = 10 * 1024 * 1024,  # 10MB
        backup_count: int = 5,
        when: str = "midnight",  # 时间轮转间隔
        interval: int = 1,
        json_format: bool = False,
        color_console: bool = True
    ):
        """
        初始化日志记录器
        
        :param name: 日志记录器名称
        :param log_level: 全局日志级别
        :param log_file: 日志文件路径
        :param file_log_level: 文件日志级别
        :param console_log_level: 控制台日志级别
        :param max_bytes: 日志文件最大字节数(大小轮转)
        :param backup_count: 保留的备份文件数
        :param when: 时间轮转间隔 (S-秒, M-分, H-小时, D-天, midnight-午夜)
        :param interval: 轮转间隔数值
        :param json_format: 是否使用JSON格式
        :param color_console: 控制台是否使用彩色输出
        """
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        
        # 防止重复添加handler
        if not self.logger.handlers:
            self._setup_handlers(
                log_file=log_file,
                file_log_level=file_log_level,
                console_log_level=console_log_level,
                max_bytes=max_bytes,
                backup_count=backup_count,
                when=when,
                interval=interval,
                json_format=json_format,
                color_console=color_console
            )
        
        # 添加自定义方法
        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.critical = self.logger.critical
        self.exception = self.logger.exception
        self.log = self.logger.log
    
    @classmethod
    def get_logger(cls, name: str = "default", **kwargs) -> 'Logger':
        """获取或创建日志记录器实例 (单例模式)"""
        if name not in cls._instances:
            cls._instances[name] = cls(name, **kwargs)
        return cls._instances[name]
    
    def _setup_handlers(
        self,
        log_file: Optional[Union[str, Path]],
        file_log_level: str,
        console_log_level: str,
        max_bytes: int,
        backup_count: int,
        when: str,
        interval: int,
        json_format: bool,
        color_console: bool
    ):
        """配置日志处理器"""
        
        # 确保日志目录存在
        if log_file:
            log_file = Path(log_file)
            log_file.parent.mkdir(parents=True, exist_ok=True)
        
        # 创建格式化器
        if json_format:
            formatter = self._json_formatter()
            console_formatter = self._json_formatter(color=color_console)
        else:
            formatter = self._text_formatter()
            console_formatter = self._text_formatter(color=color_console)
        
        # 文件处理器 (按大小轮转)
        if log_file:
            file_handler = RotatingFileHandler(
                filename=log_file,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding='utf-8'
            )
            file_handler.setLevel(file_log_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            
            # 添加时间轮转处理器 (二选一)
            # time_handler = TimedRotatingFileHandler(
            #     filename=log_file,
            #     when=when,
            #     interval=interval,
            #     backupCount=backup_count,
            #     encoding='utf-8'
            # )
            # time_handler.setFormatter(formatter)
            # self.logger.addHandler(time_handler)
        
        # 控制台处理器
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(console_log_level)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
    
    def _text_formatter(self, color: bool = False) -> logging.Formatter:
        """创建文本格式格式化器"""
        if color:
            class ColoredFormatter(logging.Formatter):
                def format(self, record):
                    levelname = record.levelname
                    message = super().format(record)
                    return f"{Logger.COLOR_MAP.get(levelname, '')}{message}{Logger.COLOR_MAP['RESET']}"
            
            return ColoredFormatter(
                fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
        else:
            return logging.Formatter(
                fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
    
    def _json_formatter(self, color: bool = False) -> logging.Formatter:
        """创建JSON格式格式化器"""
        class JsonFormatter(logging.Formatter):
            def format(self, record):
                log_data = {
                    'timestamp': datetime.now().isoformat(),
                    'logger': record.name,
                    'level': record.levelname,
                    'message': record.getMessage(),
                    'module': record.module,
                    'function': record.funcName,
                    'line': record.lineno,
                    'thread': record.threadName,
                    'process': record.processName
                }
                
                # 添加额外字段
                if hasattr(record, 'extra'):
                    log_data.update(record.extra)
                
                if color:
                    levelname = record.levelname
                    colored_msg = f"{Logger.COLOR_MAP.get(levelname, '')}{json.dumps(log_data)}{Logger.COLOR_MAP['RESET']}"
                    return colored_msg
                return json.dumps(log_data, ensure_ascii=False)
        
        return JsonFormatter()
    
    def set_level(self, level: str):
        """设置日志级别"""
        self.logger.setLevel(level.upper())
    
    def add_file_handler(
        self,
        log_file: Union[str, Path],
        level: str = "DEBUG",
        max_bytes: int = 10 * 1024 * 1024,
        backup_count: int = 5
    ):
        """添加额外的文件日志处理器"""
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding='utf-8'
        )
        file_handler.setLevel(level.upper())
        
        if any(isinstance(h, logging.FileHandler) for h in self.logger.handlers):
            formatter = self.logger.handlers[0].formatter
        else:
            formatter = self._text_formatter()
        
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def add_console_handler(self, level: str = "INFO"):
        """添加额外的控制台日志处理器"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level.upper())
        
        if any(isinstance(h, logging.StreamHandler) for h in self.logger.handlers):
            formatter = self.logger.handlers[0].formatter
        else:
            formatter = self._text_formatter(color=True)
        
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)


# 使用示例
if __name__ == "__main__":
    # 基本使用
    log = Logger.get_logger(name="my_app")
    log.info("系统启动")
    
    # 带额外字段
    log.error("用户登录失败", extra={"user": "admin", "ip": "192.168.1.1"})
    
    # 文件日志
    file_logger = Logger.get_logger(
        name="file_logger",
        log_file="logs/app.log",
        json_format=True
    )
    file_logger.info("这是一条JSON格式的日志", extra={"service": "auth"})
    
    # 异常记录
    try:
        1 / 0
    except Exception as e:
        log.exception("发生除零错误")
    
    # 动态添加处理器
    logger = Logger.get_logger(name="dynamic")
    logger.add_file_handler("logs/important.log", level="ERROR")
    logger.error("这条错误会记录到重要日志文件")