from selenium.webdriver import Chrome
import time


web = Chrome()

def main(url):

    web.get(url)
    web.maximize_window() # 最大窗口
    # 找到元素点击
    time.sleep(1)

    # 账号
    web.find_element_by_xpath('//*[@id="account-name"]').send_keys("[username]")
    # 密码
    web.find_element_by_xpath('//*[@id="user-pwd"]').send_keys("[passwd]")
    # 提交登录
    web.find_element_by_xpath('//*[@id="login-button-1"]').click()
    time.sleep(1)
    # 选择要爬取的班课
    web.find_element_by_xpath('//*[@id="main"]/main/section[2]/div[3]/ul/li[6]/div[2]/span[3]').click()
    time.sleep(3)
    # 选择可以查看答案的试题
    web.find_element_by_xpath('//*[@id="interaction-list-box"]/div[3]/div[1]').click()
    time.sleep(3)
    web.find_element_by_xpath('//*[@id="interaction-list-box"]/div[3]/div[2]/div/div').click()
    time.sleep(3)
    text = web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/a/span/button/span').click()
    time.sleep(3)
    # 选取数据所在xpath
    list_text = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[4]/div')
    list_tiku = []
    for title in list_text:
        # 题目
        job_xuhao = title.find_element_by_xpath('./div/div').text
        # 题目
        job_title = title.find_element_by_xpath('./div/div[2]/div[2]').text
        
        # 正确答案
        job_daan = title.find_element_by_xpath('./div/div[2]/div[4]/div/span').text

        print(job_xuhao,job_title +"\n"+"答案:"+ job_daan)

        # 提取题目选项
        list_options = title.find_elements_by_xpath('./div/div[2]/div[3]/span')      
        for job_options in list_options:
            # 答案选项A-D
            job_abcd = job_options.find_element_by_xpath('./span').text

            job_option = job_options.find_element_by_xpath('./span[2]').text

            print(job_abcd,job_option)
            

if __name__ == '__main__':
    url = "https://www.mosoteach.cn/web/index.php?c=passport"
    main(url)
