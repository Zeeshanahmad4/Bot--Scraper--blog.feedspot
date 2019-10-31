from selenium import webdriver
from time import sleep
import csv
import os
import sys
import urllib
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


def data(file_path, name, edition,subheading,isbn13,authors):
    fieldnames = ['Grade', 'subject', 'test', 'question', 'image']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Grade": name,
            "subject": edition,
            "test": subheading,
            "question":isbn13,
            "image":authors
})

def nameblog(file_path, name):
    fieldnames = ['Grade']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Grade": name,
})





lal = []

with open("links.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        url = row[0]
        lal.append(url)

print(len(lal))

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.set_page_load_timeout(10000)
for p in lal:
    blognamelist  = p.split("/")
    blogname      = blognamelist[-2]
    blognamefinal = "Blogs list name = {}     : blogs list url = {}".format(blogname,p)
    nameblog('final.csv', blognamefinal)
    driver.get(p)
    sleep(2)
    a = driver.find_element_by_tag_name("body")
    a.send_keys(Keys.ESCAPE)
    sleep(3)
    parent = driver.find_element_by_xpath("//*[@id='fsb']")
    childs = parent.find_elements_by_tag_name("p")
    print(len(childs))
    for i in childs:
        i_d  =  i.get_attribute("data")

        try:
            name2 = i.find_element_by_tag_name("img").get_attribute("alt")
            name = name2.encode('utf-8')
            print(name)
        except:
            name = ""

        try:
            discreption = i.text.encode('utf-8')
            print(discreption)
        except:
            discreption = ""
        
        
        try:
            logo2 = "https://i3.feedspot.com/{}.jpg".format(i_d)
            print(logo2)
        except:
            logo2 = ""
        
        
        try:
            blogurl = "https://www.feedspot.com/?followfeedid={}".format(i_d)
            print(blogurl)
        except:
            blogurl = ""

        try:
            website    = i.find_element_by_tag_name("a")
            websiteurl = website.get_attribute("href")
            print(websiteurl)
        except:
            websiteurl = ""

        data("final.csv",name,websiteurl,blogurl,logo2,discreption)
            