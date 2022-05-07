import time
from selenium import webdriver
import os

def downloader(download_list,chrome_info={}): # we got download list from download_link.py
    file_list = os.listdir("Clips")
    print(f"\n{len(download_list)} clips will be downloaded\n")
    for i in download_list:

        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={chrome_info['location']}")
        options.add_argument('--profile-directory=Default')
        prefs = {"download.default_directory": f"{os.getcwd()}\Clips"}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--log-level=3")
        driver = webdriver.Chrome(executable_path=f"driver//chromedriver{chrome_info['version']}.exe", options=options)

        driver.set_window_position(-10000, 0)
        driver.get(f"{i}")
        time.sleep(8)

        #here we're downloading clips by using selenium.
        counter=0
        while (1):
            file_list = os.listdir("Clips")
            if len(file_list) == 0:
                time.sleep(1)
                file_list = os.listdir("Clips")

            if file_list[0].endswith(".crdownload"):
                time.sleep(1)
                file_list = os.listdir("Clips")

            if file_list[0].endswith(".mp4"):
                os.replace(f"Clips\\{file_list[0]}", f"Move\\{file_list[0]}")
                time.sleep(2.5)
                counter+=1
                driver.quit()
                break
        print(f"\t{len(os.listdir('Move'))} has been downloaded.")

    for i in os.listdir("Move"):
        split_name = i.split("-")[3] #here we're editing videos file names. because of that, we can do it our progress well.
        os.rename(f'Move\\{i}', f'Move\\{split_name}')
    #here we're changing download location to default
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={chrome_info['location']}")
    options.add_argument('--profile-directory=Default')
    prefs = {"download.default_directory": f"C:\\Users\\{os.getlogin()}\\Downloads"}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(executable_path=f"driver//chromedriver{chrome_info['version']}.exe", options=options)
    time.sleep(1)
    driver.quit()



    return os.listdir("Move"),file_list
    #move file contain videos files.