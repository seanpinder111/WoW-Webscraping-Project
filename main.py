from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
import re
import csv
from os import chdir
from os import getcwd
from os.path import isfile
from os import mkdir
from os.path import exists

# GLOBAL VARIABLES
class_name = "Warrior"
url = "https://www.wowhead.com/wotlk/spells/talents/warrior?filter-any=12:13;1:3;0:0#50"

def download_image(img_address, file_name):
    # download image to working directory
    urllib.request.urlretrieve(img_address, file_name + ".jpg")

    # throttle scrape speed
    time.sleep(5)


def scrape(url):
    # initiate webdriver
    driver = webdriver.Chrome("C:/User/seanp/Downloads/chromedriver_win32/chromedriver.exe")
    driver.set_window_size(1080, 800)

    # open webpage
    driver.get(url)

    # get list
    talent_list = driver.find_elements(By.XPATH, "//*[@id='lv-spells']/div[2]/div/table/tbody/tr")
    no_talents = len(talent_list)

    # initialize lists
    addresses = []
    names = []
    img_addresses = []

    # get names and url links to each talent
    for i in range(1, 1 + no_talents):
        talent = driver.find_element(By.XPATH,
                                     "//*[@id='lv-spells']/div[2]/div/table/tbody/tr[" + str(i) + "]/td[2]/div/a")
        talent_image = driver.find_element(By.XPATH, "//*[@id='lv-spells']/div[2]/div/table/tbody/tr[" + str(
            i) + "]/td[1]/div/ins")
        addresses.append(talent.get_attribute("href"))
        names.append(talent.text)
        # search string for url with image address
        img_string = re.search("https.*\.jpg", talent_image.get_attribute("style")).group()
        img_addresses.append(img_string)

    #terminate driver
    driver.quit()

    # #dowload all talent images
    for i in range(no_talents):
        download_image(img_addresses[i],names[i])

    #populate CSV and write CSV
    if isfile('./'+ class_name + '_Talents.csv') == False:
        write_type = 'w'
    else:
        write_type = 'a'
    with open('./'+ class_name + '_Talents.csv', write_type) as cc:
        writer = csv.writer(cc)
        for i in range(no_talents):
            writer.writerow([names[i], class_name,addresses[i],names[i]+".jpg"])





def main():
    #crate new directory
    dir_path = "C:/Users/seanp/Documents/JavascriptProjects/WoW Talent Project/" + class_name + " Talents"
    if not exists(dir_path):
        mkdir(dir_path)

    # change working directory
    chdir(dir_path)

    #scrape
    scrape(url)





if __name__ == "__main__":
    main()











