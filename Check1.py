# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 09:18:14 2021

@author: 10912210
"""
from selenium import webdriver
import requests


link='97XOubA6z8Z8LDSncX0XqMNZHlaoeqU4VvNVaeKM1D6','YV6wk1YR82W2Xz3dsARrAkmDEEkuVElt3mjFqq9ZCqa','6SISxxSALMB6o6DL9BCz6rM0IcMREZwkKAm5m0jTkvY'


user='10903205' 

class file_check(object):
    driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"

    def __init__(self):
        option = webdriver.ChromeOptions()
        # 設定不顯示頁面，隱式執行（測試程式碼時建議將這樣註釋掉，可以直觀地看到自己在那一個步驟出bug了）
        option.add_argument('--headless')
        # 設定不載入圖片，加快載入速度
        prefs = {'profile.managed_default_content_settings.images': 2}
        option.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path=file_check.driver_path,options=option)
        


    
    def login(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://familyweb.wistron.com/whrs/login.aspx')
        self.driver.find_element_by_id('userpass').send_keys(user)#填入'somekeys'
        self.driver.find_element_by_css_selector("input[value=' 登入 '").click()
        self.driver.find_element_by_xpath('//*[@id="loginform"]/div/a[2]').click()
        b=0
        #計算最大tr        
        trs = self.driver.find_elements_by_xpath('//*[@id="loginform"]/table[2]/tbody/tr')
        # print(len(trs))
        for i in range(2,len(trs)+1):

            # if self.driver.find_element_by_xpath('//*[@id="loginform"]/table[2]/tbody/tr['+str(i)+']/td[4]').text != '無發燒  ' :
            if self.driver.find_element_by_xpath('//*[@id="loginform"]/table[2]/tbody/tr['+str(i)+']/td[4]').text == '':
                if self.driver.find_element_by_xpath('//*[@id="loginform"]/table[2]/tbody/tr['+str(i)+']/td[3]').text != '10710146':
                    a=self.driver.find_element_by_xpath('//*[@id="loginform"]/table[2]/tbody/tr['+str(i)+']').text
                    print(self.driver.find_element_by_xpath('//*[@id="loginform"]/table[2]/tbody/tr['+str(i)+']').text)
                    b=1
                    line(self,a)
                    
                    
                    # /html/body/table/tbody/tr[7]/td[2]/a
                    # /html/body/table/tbody/tr[7]/td[2]/a
                    # headers = {
                    #     "Authorization": "Bearer " + "97XOubA6z8Z8LDSncX0XqMNZHlaoeqU4VvNVaeKM1D6",
                    #     "Content-Type": "application/x-www-form-urlencoded"
                    # }
                 
                    # params = {"message":'尚未回報人員\n'+ a}
                 
                    # r = requests.post("https://notify-api.line.me/api/notify",
                    #                   headers=headers, params=params)
                    # print(r.status_code)  #200
                    
            else:
                pass
     
        if b==0:
            print('無')
            a='無'
            line(self,a)
            # headers = {
            #     "Authorization": "Bearer " + "97XOubA6z8Z8LDSncX0XqMNZHlaoeqU4VvNVaeKM1D6",
            #     "Content-Type": "application/x-www-form-urlencoded"
            # }
         
            # params = {"message":'尚未回報人員\n無'}
         
            # r = requests.post("https://notify-api.line.me/api/notify",
            #                   headers=headers, params=params)
            # print(r.status_code)  #200
        self.driver.quit()
        
        
        
        
def line(self,a):
    # a=self.driver.find_element_by_xpath('//*[@id="loginform"]/table[2]/tbody/tr['+str(i)+']').text
    
    for i in link:
        headers = {
            "Authorization": "Bearer " + i,
            "Content-Type": "application/x-www-form-urlencoded"
        }
     
        params = {"message":'尚未回報人員\n'+ a}
     
        r = requests.post("https://notify-api.line.me/api/notify",
                          headers=headers, params=params)
        print(r.status_code)  #200
    
    

if __name__ == '__main__':

    file = file_check()
    file.login()
