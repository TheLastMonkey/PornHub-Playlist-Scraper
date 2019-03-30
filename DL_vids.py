
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import ast
import os

# open the playlist info file
ply_list_info = open("ply_list_info.txt", "r")
print(ply_list_info)
# iterate through file to reconstruct list using ast.literal_eval
for ply_list_info_list in ply_list_info:
    ply_list_info_list = ast.literal_eval(ply_list_info_list)
# print the name of the playlist
print(ply_list_info_list[2])
# construct the playlist video path
vid_path = "./vids/" + ply_list_info_list[2] + "_ID_" + ply_list_info_list[1] + "/"
# make the playlist video path
os.system("mkdir " + vid_path)

# try to open the playlist file
try:
    assets_file = open('ph_list_file.txt')
except FileNotFoundError as e:
    print("Looks like you ran the wrong script first.")
    quit()

def main():
    # iterate through the lines in the playlist file
    for line in assets_file:
        line = ast.literal_eval(line)

        print(line)
        # set options for the webdriver
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=192x108")
        driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
        driver.set_page_load_timeout(60)
        # Activate Webdriver
        driver.get(line[0])

        time.sleep(1)
        print('Working...')
        # grabbing the source link for the video
        try:
            for ph_meta in driver.find_elements_by_xpath('//source[@src]'):
                vid_link_asset=ph_meta.get_attribute("src")
                # video name Construction and sanitation
                vidname = line[1]
                vidname = vidname.replace(' ', '_').replace("'", "").replace('"', '').replace(",", "")
                # construct video get command
                get_com = "wget -c " + vid_link_asset + " -O " + vid_path + vidname + ".mp4"
                print(get_com)
                print("Perparing Download...")
                # attempt to download video
                try:
                    os.system(get_com)
                except:
                    pass
        # skipping video if anything fails
        except:
            print('End')


        driver.close()

        
main()

