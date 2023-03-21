from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import os


@pytest.mark.parametrize(('area, expect, fileName'),
                        [("東京都","東京都庁の天気予報","screenshot1.png"),
                        ("沖縄県","沖縄県の天気予報","screenshot2.png")])


def test_GoogleSearch(area,expect,fileName):    
    driver = webdriver.Chrome()

    #GoogleのTOPページを開く 
    driver.get('https://google.co.jp/')
    time.sleep(3)
    driver.maximize_window()

    searchElement = driver.find_element("name", "q")

    #「selenium」と入力して検索する
    searchElement.send_keys("天気")
    searchElement.submit()
    time.sleep(3)

    #検索結果にある、seleniumのサイトURLをクリックする
    text = driver.find_element(By.XPATH,"//h3[text()='全国の天気 - ウェザーニュース']")
    text.click()
    time.sleep(3)
    #ページタイトルを検証する
    assert driver.title == "【ウェザーニュース】天気予報 - 台風・地震・防災情報"

    #天気を見たい場所を検索する
    searhArea = driver.find_element(By.ID,"search_pc")
    searhArea.send_keys(area)
    searhArea.submit()
    time.sleep(3)
    
    #検索後の文字を検証する
    assert driver.find_element(By.CLASS_NAME,"index__tit").text == expect

    #スクリーンショットを取る
    driver.save_screenshot(fileName)

    driver.quit()