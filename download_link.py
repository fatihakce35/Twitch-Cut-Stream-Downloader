from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from buttons import *
from functions import *
def get_download_link(start_second_stream,end_second_stream,seconds,stream_id,chrome_info={}):
    download_list=[] #here we have a download list. we're gonna put links in this list.
    part_of_video = int(seconds / 90)
    print(f"\n{part_of_video} clip will be created.\n")
    for i in range(0, part_of_video):

        if start_second_stream >= end_second_stream:
            break
        #chrome settings
        begining = second_to_time(start_second_stream)
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={chrome_info['location']}")
        options.add_argument('--profile-directory=Default')
        options.add_argument("--log-level=3")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])


        driver = webdriver.Chrome(executable_path=f"driver//chromedriver{chrome_info['version']}.exe", options=options)

        driver.set_window_position(-10000, 0)

        #here opening twitch by time. we can get clips that we want
        driver.get(f"https://www.twitch.tv/videos/{stream_id}?t={begining[0]}h{begining[1]}m{begining[2]}s")
        time.sleep(3)

        #sometimes if you open a stream video, that can be alert (this is for mature..). so we added a button to past this
        try:
            mature_accept = driver.find_element(by=By.XPATH,
                                                value=MatureAccept_button)
            if mature_accept.is_displayed():
                mature_accept.click()
            else:
                pass
        except Exception as e:
            pass

        start_time = time.time()
        while (1):

            if int(time.time() - start_time) >= 15 and len(driver.window_handles) != 2:
                driver.refresh()
                start_time = time.time()
            # 'alt + x' is creating a twitch clip page. so we're doing this
            if len(driver.window_handles)!=2:
                clip_page_key = ActionChains(driver)
                clip_page_key.key_down(Keys.ALT).send_keys("x").key_up(Keys.ALT).perform()
                break

        time.sleep(1)
        while (1):
            try:
                #changing window to clip page
                driver.switch_to.window(driver.window_handles[1])
                break
            except IndexError:
                continue
        time.sleep(1)
        download_url = ""
        start_time = time.time()
        while (1):
            try:
                # in the clip page of twitch, there is a downloand link in html code. because of that we're parsing html
                if int(time.time() - start_time) >= 18 and len(driver.window_handles) != 1:
                    start_second_stream += 1
                    driver.quit()
                    break
                # in the clip page of twitch, there is a downloand link in html code. because of that we're parsing html
                element = driver.find_element(by=By.XPATH, value=download_button)
                if element.is_displayed():
                    element = element.get_attribute('outerHTML')

                    try:
                        element = element.split(" ")
                        element[3] = element[3].split('"')
                        download_url = element[3][1]
                        # now we get a downloand link of a part of stream. (that is a 90 seconds clip. we're gonna merge them later)
                        break
                    except IndexError:
                        continue
            except Exception as e:
                continue

        #if statments for downloand link is valid or not.
        if not "raw_media/vod" in download_url:
            part_of_video += 1
        else:
            download_list.append(download_url)
            time.sleep(1)

            start_second_stream += 90
        print(f"\t{len(download_list)} has been created")
        driver.quit()
    #then, we're returning download list to downloader.py file
    return download_list