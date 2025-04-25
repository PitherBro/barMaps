#!/bin/python3

import os,sys
from pathlib import Path
import subprocess
import gdown
import webbrowser



root = Path(os.path.dirname( __file__ ))
mapsFolder=root/'maps/'

'''
#import another module from anywhere
modPath = root/"module"
sys.path.append(modPath)
'''

if __name__ == "__main__":
    # print(__name__)
    # determine OS for paths

    # ask if we need to pull files,
    urlID = "16eBcMpkgMTV9mlKxYmNda64X_dmCFdkk"
    url = "https://drive.google.com/drive/folders/16eBcMpkgMTV9mlKxYmNda64X_dmCFdkk?usp=drive_link"# "https://drive.google.com/drive/folders/" + urlID
    # https://drive.google.com/uc?id=16eBcMpkgMTV9mlKxYmNda64X_dmCFdkk&export=download
    # download to 'maps/' folder
    output_path = str(mapsFolder)
    # webbrowser.register('firefox')
    # webbrowser.open_new(url)
    os.system(f"""firefox --new-window {url}""")
    # webbrowser.open(url=url, new=1,)
    

    # https://www.intodeeplearning.com/how-to-download-files-or-folders-in-gdrive-in-python/
    # downloadResponse = gdown.download_folder(url, output=mapsFolder, remaining_ok=True, quiet=True,skip_download=True)
    
    ### Other Resources
    # https://gist.github.com/swyoon/5601cd17bcc2ada8599bfa7549e6f698
    # https://www.intodeeplearning.com/how-to-download-files-or-folders-in-gdrive-in-python/
    # https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url
    # https://stackoverflow.com/questions/25010369/wget-curl-large-file-from-google-drive/39225039#39225039
    
    # gdown.download_folder(url=url, output=output_path, remaining_ok=True)
    # gdown.download(url=url,\
    #                 format="zip",\
    #                 output=output_path,\
    #                 verify=False,
    #                 resume=False,\
    #                 quiet=False,\
    #                 fuzzy=True)
    # # print(downloadResponse)
    # get the zip files
    # https://stackoverflow.com/questions/1606795/catching-stdout-in-realtime-from-subprocess
    # formats the subprocess into a list of strings
    response = str(subprocess.Popen(["bash",f"{root/'scripts/linux/unzip.sh'}"], stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read(),'utf-8').split()

    # extract to game folder

    print(response)
