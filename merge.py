
import os
import time
def merger(file_list,cutter=None,len_file=None,file_name=None):
    video_list=[]
    print("Merging Clip files...\n")



    if cutter == 0: #we can split video by cutter. if we don't we always get videos minutes by times of 90 second
        file = open("ffmpeg\\concat.txt", "w") # we're writing videos files location to a text file to merge them with ffmpeg
        for i in file_list:
            file.write(f"file 'file:Move\\{i}'\n")
        file.close()
        time.sleep(1)
        os.system(f'"ffmpeg\\bin\\ffmpeg.exe -f concat -safe 0 -i ffmpeg\\concat.txt -vcodec copy -acodec copy C:\\Users\\{str(os.getlogin())}\\Desktop\\{str(file_name)}.mp4 2> ffmpeg\\out.txt"')
        #we're using ffmpeg code to merge videos.


        for i in file_list:
            os.remove(f"Move\\{i}")


    else:
         # we're getting video by cut. if we don't we always get videos minutes by times of 90 second.
        os.system(f"ffmpeg\\bin\\ffmpeg.exe -ss 00:00:00 -to 00:0{str(int(cutter/60))}:{str(int(cutter%60))} -i Move\\{file_list[len(file_list) - 1]} -c copy Cut\\cut.mp4 2> ffmpeg\\out.txt")
        #then we're saving this to videos files.

        try:
            file = open("ffmpeg\\concat.txt", "w") # we're writing videos files location to a text file to merge them with ffmpeg
            for i in file_list[0:len(file_list)-1]:
                file.write(f"file 'file:Move\\{i}'\n")
            file.write(f"file 'file:Cut\\cut.mp4'\n") # and last video that we cutted before.
            file.close()
        except IndexError: #if we have only cut.mp4 video
            file = open("ffmpeg\\concat.txt", "w")
            file.write(f"file 'file:Cut\\cut.mp4'\n")
            file.close()
        os.system(f'"ffmpeg\\bin\\ffmpeg.exe -f concat -safe 0 -i ffmpeg\\concat.txt -vcodec copy -acodec copy C:\\Users\\{str(os.getlogin())}\\Desktop\\{str(file_name)}.mp4 2> ffmpeg\\out.txt"') #merging videos with ffmpeg code again.

        os.remove("Cut\\cut.mp4") #and we're deleting files after progress.
        time.sleep(1)

        for i in file_list:
            os.remove(f"Move\\{i}")









