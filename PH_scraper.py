from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import re
# setting the playlist file name
ph_list_file = "ph_list_file.txt"
# attempt to remove and make the file to clean it out from previous use
try:
    os.system("rm " + ph_list_file)
    os.system("touch " + ph_list_file)
except:
    print("Failed to make or delete file")
    quit()
# ask user for the playlist ID
PH_URL_ID = input("Input URL of Playlist ID : ")
# options for webdriver
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=192x108")

driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
driver.set_page_load_timeout(60)
print("Loading...")
# set playlist URL
PH_URL = "https://www.pornhub.com/playlist/" + PH_URL_ID
print(PH_URL)
# start Webdriver
driver.get(PH_URL)

# set up regex to identify only links to videos
regex = "https://www.pornhub.com/view.+"

print('Working...')
# grab and sanitized the title of the playlist
try:
    pl_tile_name_meta = driver.find_element_by_xpath('//*[@id="playlistTopHeader"]/h1/a')
    # print(pl_tile_name_meta)
    pl_tile_name_txt = pl_tile_name_meta.get_attribute("text")
    pl_tile_name_txt = pl_tile_name_txt.replace(",", "").replace("'", "").replace('"', "").replace(" ", "_")
    print(pl_tile_name_txt)
except:
    print("Failed at tile grab!")
    driver.close()
    quit()
# creating playlist info list and putting that into a file
ply_list_info = [PH_URL, PH_URL_ID, pl_tile_name_txt]

print(ply_list_info)
print(ply_list_info, file=open("ply_list_info.txt", "w"))

# try and grab all the links on the page specifying that they must have text associated with them
# further specifying that they must be a video link
# this removes duplicate links associated with title and the thumbnail
try:
    for meta in driver.find_elements_by_xpath('//a[@href]'):
        # print(meta)
        if meta.text == "":
            pass
        else:
            # getting the links
            href_str = meta.get_attribute('href')

            if re.search(regex, href_str) is not None:

                ph_link_to_split = meta.get_attribute('href')
                # strip off the &pkey=4628031 "playlist key"
                ph_link = str(ph_link_to_split).split('&')
                the_link = ph_link[0]
                # print to term
                print(meta.text)
                print(the_link)
                # make as list print to file
                ph_list = [the_link, meta.text]
                print(ph_list, file=open(ph_list_file, "a"))

            else:
                pass

except:
    print('End')

driver.close()
