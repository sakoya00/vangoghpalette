from selenium import webdriver
import argparse
import os
import csv
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-url','--url', help='url of artworks')
args, unknown = parser.parse_known_args()
url = args.url
url = "https://en.wikipedia.org/wiki/List_of_works_by_Vincent_van_Gogh"
driver = webdriver.Chrome()
driver.get(url)
pause_time= 3
prev_height = driver.execute_script("return document.body.scrollHeight")

while True:
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(pause_time)
current_height= driver.execute_script("return document.body.scrollHeight")
if current_height == prev_height:
	break
current_height= prev_height

anchor_tags= driver.find_elements_by_tag_name('a')
img_urls= []

for tag in anchor_tags:
    if "image" in tag.get_attribute("class"):
        continue
    img_urls.append(tag.get_attribute("href"))

iu2 = np.array(img_urls)

with open('outputFile.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in range(0, iu2.shape[0]):
        my_list = []
        my_list.append(iu2[row])
        writer.writerow(my_list)
