from typing import Optional, Union, List, Dict, Tuple
from playwright.sync_api import sync_playwright, Page, BrowserContext, Browser, Locator
import time
import logging
from pathlib import Path

class PlaywrightAutomation:
    """
    Playwright 自动化封装类
    
    功能特点：
    - 支持同步 API
    - 自动管理浏览器生命周期
    - 提供常用页面操作方法
    - 内置智能等待和重试机制
    - 支持截图和视频录制
    
    示例用法:
    >>> with PlaywrightAutomation() as auto:
    >>>     auto.navigate("https://example.com")
    >>>     auto.click("#submit-btn")
    >>>     auto.fill("#username", "testuser")
    """

    def __init__(
        self,
        browser_type: str = "chromium",
        headless: bool = True,
        slow_mo: int = 100,
        viewport: Dict[str, int] = None,
        user_agent: str = None,
        trace: bool = False,
        video: bool = False
    ):
        """
        初始化 Playwright 自动化实例
        
        :param browser_type: 浏览器类型 (chromium, firefox, webkit)
        :param headless: 是否无头模式
        :param slow_mo: 操作延迟(毫秒)
        :param viewport: 视窗大小 {'width': 1920, 'height': 1080}
        :param user_agent: 自定义 User-Agent
        :param trace: 是否启用跟踪
        :param video: 是否录制视频
        """
        self.browser_type = browser_type.lower()
        self.headless = headless
        self.slow_mo = slow_mo
        self.viewport = viewport or {"width": 1366, "height": 768}
        self.user_agent = user_agent
        self.trace = trace
        self.video = video
        
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        
        # 配置日志
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # 创建结果目录
        self.results_dir = Path("results")
        self.results_dir.mkdir(exist_ok=True)

    def __enter__(self):
        """上下文管理器入口"""
        self.start_browser()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出"""
        self.close_browser()

    def start_browser(self):
        """启动浏览器和上下文"""
        self.playwright = sync_playwright().start()
        
        # 根据类型启动浏览器
        if self.browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(
                headless=self.headless,
                slow_mo=self.slow_mo,
                channel="chrome"
            )
        elif self.browser_type == "firefox":
            self.browser = self.playwright.firefox.launch(
                headless=self.headless,
                slow_mo=self.slow_mo
            )
        elif self.browser_type == "webkit":
            self.browser = self.playwright.webkit.launch(
                headless=self.headless,
                slow_mo=self.slow_mo
            )
        else:
            raise ValueError(f"不支持的浏览器类型: {self.browser_type}")
        
        # 创建上下文
        context_args = {
            "viewport": self.viewport,
            "record_video_dir": "results/videos" if self.video else None
        }
        if self.user_agent:
            context_args["user_agent"] = self.user_agent
            
        self.context = self.browser.new_context(**context_args)
        
        # 启用跟踪
        if self.trace:
            self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        # 创建新页面
        self.page = self.context.new_page()
        self.logger.info(f"启动 {self.browser_type} 浏览器 {'(无头模式)' if self.headless else ''}")

    def close_browser(self):
        """关闭浏览器并保存跟踪数据"""
        if self.trace and self.context:
            trace_path = self.results_dir / "trace.zip"
            self.context.tracing.stop(path=trace_path)
            self.logger.info(f"跟踪数据已保存到: {trace_path}")
        
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        self.logger.info("浏览器已关闭")

    def navigate(self, url: str, timeout: int = 30000):
        """导航到指定URL"""
        self.logger.info(f"导航到: {url}")
        self.page.goto(url, timeout=timeout)
        self.page.wait_for_load_state("networkidle")

    def click(self, selector: str, timeout: int = 10000):
        """点击元素"""
        self.logger.info(f"点击元素: {selector}")
        self.page.click(selector, timeout=timeout)

    def double_click(self, selector: str, timeout: int = 10000):
        """双击元素"""
        self.logger.info(f"双击元素: {selector}")
        self.page.dblclick(selector, timeout=timeout)

    def fill(self, selector: str, text: str, timeout: int = 10000):
        """填充文本到输入框"""
        self.logger.info(f"在 {selector} 中输入: {text}")
        self.page.fill(selector, text, timeout=timeout)

    def type(self, selector: str, text: str, delay: int = 100, timeout: int = 10000):
        """模拟键盘输入"""
        self.logger.info(f"在 {selector} 中键入: {text}")
        self.page.type(selector, text, delay=delay, timeout=timeout)

    def wait_for_selector(self, selector: str, timeout: int = 10000) -> Locator:
        """等待元素出现并返回定位器"""
        self.logger.info(f"等待元素: {selector}")
        return self.page.locator(selector).wait_for(timeout=timeout)

    def get_text(self, selector: str, timeout: int = 10000) -> str:
        """获取元素文本"""
        self.logger.info(f"获取元素文本: {selector}")
        return self.page.locator(selector).text_content(timeout=timeout).strip()

    def get_attribute(self, selector: str, attr: str, timeout: int = 10000) -> Optional[str]:
        """获取元素属性"""
        self.logger.info(f"获取元素属性: {selector}@{attr}")
        return self.page.locator(selector).get_attribute(attr, timeout=timeout)

    def screenshot(self, name: str = None, full_page: bool = False):
        """截取页面截图"""
        if not name:
            name = f"screenshot_{int(time.time())}.png"
        path = self.results_dir / name
        self.page.screenshot(path=path, full_page=full_page)
        self.logger.info(f"截图已保存到: {path}")

    def select_option(self, selector: str, value: str, timeout: int = 10000):
        """选择下拉框选项"""
        self.logger.info(f"在下拉框 {selector} 中选择: {value}")
        self.page.select_option(selector, value=value, timeout=timeout)

    def hover(self, selector: str, timeout: int = 10000):
        """鼠标悬停元素"""
        self.logger.info(f"悬停元素: {selector}")
        self.page.hover(selector, timeout=timeout)

    def press_key(self, key: str):
        """按下键盘按键"""
        self.logger.info(f"按下按键: {key}")
        self.page.keyboard.press(key)

    def scroll_to_element(self, selector: str, timeout: int = 10000):
        """滚动到指定元素"""
        self.logger.info(f"滚动到元素: {selector}")
        self.page.locator(selector).scroll_into_view_if_needed(timeout=timeout)

    def execute_script(self, script: str, *args):
        """执行JavaScript脚本"""
        self.logger.info(f"执行脚本: {script[:50]}...")
        return self.page.evaluate(script, args)

    def switch_to_frame(self, selector: str):
        """切换到iframe"""
        self.logger.info(f"切换到iframe: {selector}")
        frame = self.page.frame_locator(selector)
        return frame

    def wait_for_timeout(self, milliseconds: int):
        """强制等待"""
        self.logger.info(f"等待 {milliseconds} 毫秒")
        self.page.wait_for_timeout(milliseconds)

    def reload_page(self):
        """重新加载页面"""
        self.logger.info("重新加载页面")
        self.page.reload()
        self.page.wait_for_load_state("networkidle")

    def get_current_url(self) -> str:
        """获取当前页面URL"""
        return self.page.url

    def get_page_title(self) -> str:
        """获取页面标题"""
        return self.page.title()

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        """检查元素是否可见"""
        try:
            self.page.locator(selector).wait_for(timeout=timeout)
            return self.page.locator(selector).is_visible()
        except:
            return False

    def is_checked(self, selector: str) -> bool:
        """检查复选框/单选框是否被选中"""
        return self.page.locator(selector).is_checked()

    def upload_file(self, selector: str, file_path: str):
        """上传文件"""
        self.logger.info(f"上传文件: {file_path} 到 {selector}")
        self.page.locator(selector).set_input_files(file_path)

    def clear_input(self, selector: str):
        """清空输入框"""
        self.logger.info(f"清空输入框: {selector}")
        self.page.locator(selector).clear()

    def drag_and_drop(self, source: str, target: str):
        """拖放元素"""
        self.logger.info(f"拖放 {source} 到 {target}")
        self.page.locator(source).drag_to(self.page.locator(target))

    def get_all_cookies(self) -> List[Dict]:
        """获取所有cookies"""
        return self.context.cookies()

    def add_cookie(self, cookie: Dict):
        """添加cookie"""
        self.context.add_cookies([cookie])

    def clear_cookies(self):
        """清除所有cookies"""
        self.context.clear_cookies()

    def mock_api_response(self, url_pattern: str, response: Dict, status: int = 200):
        """模拟API响应"""
        self.logger.info(f"模拟API响应: {url_pattern} -> {status}")
        self.page.route(url_pattern, lambda route: route.fulfill(
            status=status,
            content_type="application/json",
            body=json.dumps(response)
        ))


# 使用示例
if __name__ == "__main__":
    with PlaywrightAutomation(headless=False, trace=True) as auto:
        # 打开网页
        auto.navigate("https://example.com")
        
        # 检查页面标题
        print("页面标题:", auto.get_page_title())
        
        # 截图
        auto.screenshot("example.png")
        
        # 模拟搜索操作
        auto.fill('input[name="q"]', "Playwright自动化")
        auto.click('input[type="submit"]')
        
        # 等待结果
        auto.wait_for_selector("#search-results", timeout=15000)
        
        # 获取结果数量
        results = auto.get_text("#result-stats")
        print("搜索结果:", results)