# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
chrome_options.add_argument('--user-agent=' + user_agent)
prefs = {"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = '/opt/google/chrome/chrome'

csv_file = open('playlist.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])
web = webdriver.Chrome(chrome_options=chrome_options)

page_url = 'https://music.163.com/#/discover/playlist'#'https://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
while page_url != 'javascript:void(0)':
    print('GET PAGE: ' + page_url)
    web.get(page_url)
    try:
        web.switch_to.frame('contentFrame')
        data = web.find_element_by_id('m-pl-container').find_elements_by_tag_name('li')
        for i in range(len(data)):
            nb = data[i].find_element_by_class_name('nb').text
            # if '万' in nb and int(nb.split("万")[0]) > 500:
            if '万' in nb:
                nb = int(nb.split("万")[0]) * 10000
            msk = data[i].find_element_by_css_selector('a.msk')
            writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])
    except Exception as e:
        print("Exception Found: " + str(e))
        continue
    else:
        page_url = web.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')

csv_file.close()