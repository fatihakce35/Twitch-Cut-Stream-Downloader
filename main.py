from functions import *

from merge import merger

from download_link import get_download_link
from downloader import downloader
from chrome_settings import chrome_settings


delete_videos()
chrome_info=chrome_settings()


start_second_stream,end_second_stream,part_of_video,stream_id,file_name1,seconds=stream_info()

download_list=get_download_link(start_second_stream,end_second_stream,seconds,stream_id,chrome_info)



downloaded_files,file_list=downloader(download_list,chrome_info)
downloaded_files=sorted(downloaded_files, key=lambda x: int(x.split('.')[0]))

merger(downloaded_files,int((end_second_stream-start_second_stream)%90),len(file_list),file_name1)

enter=input("The vod cut downloaded succesfully. You can find it your dekstop. Thank you :)")

"""

-you must be sure you've loggin your twitch account or any twitch account

-you must be sure the stream can avaliable to clip. some streamers are putting settings that only subscribers
can get clip.

- be sure you're using chrome browser and you've been set your chrome settings correctly.
"""