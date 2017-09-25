from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
print("="*5+"\n")
print("台灣地區-地名中翻英\n\n使用說明：請輸入台灣地區的中文地名，並按下ENTER鍵即可得該地名之翻譯。\n\n翻譯來源：{siteName}\n網址：{url}\n".format(siteName="內政部地政司-地名資訊服務網",url="http://gn.moi.gov.tw/GeoNames/Translation/Translation.aspx"))
print("="*5+"\n")

while True:
	driver.get('http://gn.moi.gov.tw/GeoNames/Translation/Translation.aspx')

	elem = driver.find_element_by_id('ContentPlaceHolder1_txt_geoNames')
	
	target = input("請輸入你想翻譯的地名：")
	if target:
		elem.send_keys(target)
		time.sleep(1)
		elem = driver.find_element_by_id('ContentPlaceHolder1_btn_single_Search')
		elem.send_keys(Keys.ENTER)
		time.sleep(1)

		resource = driver.page_source
		soup = BeautifulSoup(resource,'html.parser')
		table = soup.find('table',{'id':"ContentPlaceHolder1_gv_translationSingleResult"})
		tr = table.select('tr th')

		for i in range(len(tr)):
			if tr[i].string == "建議譯寫": 
				print("官方建議譯寫為：{result}\n".format(result = 
					table.select('tr td')[i].string))
				break
	else:
		print("您沒有輸入地名！\n")




