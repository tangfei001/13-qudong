**课时173-Python对log文件的操作**

import  logging
from selenium import  webdriver
import  unittest




def log(log_content):
    # 定义文件
    logFile = logging.FileHandler('log.md', 'a',encoding='utf-8')
    # log格式
    fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
    logFile.setFormatter(fmt)

    # 定义日志
    logger1 = logging.Logger('logTest', level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)

class Ui(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        log('初始化浏览器')

    def test_001(self):
        log('开始测试')
        pass

    def tearDown(self):
        log('测试结束')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

