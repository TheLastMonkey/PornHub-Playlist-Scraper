# PornHub Playlist Scraper
As the name implies this script will scrape the links to the videos from PornHub playlist.
It puts all those links into a file for downloading. This allows you to download the videos
separate from the initial scrape so that you can pick up downloading where you left off.

Each playlist has its own folder with the video files in it to keep things a bit more
organized. Playlist name and video titles are preserved and special characters are sanitized.
Spaces are replaced with underscores. The playlist ID number is added to the folder for the
playlist for convenience.

## Requirements
* Python 3.7
* Linux
* Selenium Chrome Webdriver  (Not Included)

#### INFO
os.system - Is used to make, delete and wget a files.
#### Instructions
**_First_** use the file _**PH_scraper.py**_ and when you're ready to start or resume
downloading the videos use the **_DL_vids.py_**

_**PH_scraper.py**_
Will ask you for the playlist ID.
the playlist ID will be located at the end of the URL of the playlist. See example
https://www.pornhub.com/playlist/**92450201** **<---** **Playlist ID**
This will generate one information file named **_ply_list_info.txt_** and one more file
named **_ph_list_file.txt_** which will contain lists of _video page links_ and _video titles_.

**_DL_vids.py_**
This script will Loop through the **_ph_list_file.txt_** file and scrape the video page and
download the video into a folder named **vids** and then a folder named the playlist name and
will also contain the playlist ID number for reference an organization.

#### TODO
* The file will likely be used if I decide to add playlist saving.
* Testing for more potential bugs and errors.
* Streamline code.









## Disclaimer
None of the files or scrubs here are intended to do or allow you
to do anything illegal. This project is for research purposes only
and does not come with a warranty or guarantee or license. This
project does not contain all the files it needs to be able to
function. Run at your own risk. I take no responsibility for damage
or laws that may or may not be broken in the use of this project.
By viewing and downloading this you take full responsibility for
any actions taken on your device.


#### license
You Do You. If you want to modify this project go for it, steal it, fix it whatever.
