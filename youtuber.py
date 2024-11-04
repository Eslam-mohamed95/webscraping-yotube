from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from pytube import YouTube
'''

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
page= driver.get("https://www.youtube.com/watch?v=CQ2fMMNQ47c&ab_channel=Wegz%D9%88%D9%8A%D8%AC%D8%B2")
video = driver.find_element(by= By.CLASS_NAME,value= "html5-video-container").find_element(by= By.TAG_NAME,value= "video")
url = video.get_attribute("src").replace("blob:", "")
if "blob" in url :
    url.replace("blob:", "").strip()
else :pass
print(url)
'''
try :
    ytb =YouTube("https://www.youtube.com/watch?v=CQ2fMMNQ47c&ab_channel=Wegz%D9%88%D9%8A%D8%AC%D8%B2")
    stream = ytb.streams.get_highest_resolution()
    stream.download(output_path="/home/kali/Desktop", filename="wegz")
    print(" thank you waiting \n video downloaded")
except Exception as e:
    print(f"error is {e}")



