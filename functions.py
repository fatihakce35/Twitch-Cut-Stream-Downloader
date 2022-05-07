import os
def second_maker(hour=0,minute=0,second=0): # a function that make time to second. we need this for download link.
    #example: https://clips-media-assets2.twitch.tv/raw_media/stream_id-offset-seconds.mp4
    total_second=(hour*60*60) + (minute*60) + second
    return total_second


def second_to_time(second):
    hour=int(second/3600)
    minute=int((second-3600*hour)/60)
    second=second%60
    return hour,minute,second
    #here we need seconds by hour, minute and second
    #example: https://www.twitch.tv/videos/{stream_id}?t={second_to_time[0]}h{second_to-time[1]}m{second_to_time[2]}s


def delete_videos():
    #deleting old videos files.
    for i in os.listdir("Cut"):
        os.remove(f"Cut\\{i}")
    for i in os.listdir("Clips"):
        os.remove(f"Clips\\{i}")
    for i in os.listdir("Move"):
        os.remove(f"Move\\{i}")

def stream_info():
    stream_id = input("Please enter stream id: ")
    stream_time = input("Please enter begining of stream minute (hh:mm:ss): ")
    stream_time2 = input("Please enter end of stream minute (hh:mm:ss): ")
    file_name1 = input("Please enter name of file: ")

    stream_time = stream_time.split(":")
    print(stream_time)
    stream_time2 = stream_time2.split(":")
    print(stream_time2)
    start_second_stream = second_maker(int(stream_time[0]), int(stream_time[1]), int(stream_time[2])) + 90

    end_second_stream = second_maker(int(stream_time2[0]), int(stream_time2[1]), int(stream_time2[2])) + 90
    # these progress necessary for getting stream_id, times and file names that will be named.
    start_second_stream = int(start_second_stream)
    end_second_stream = int(end_second_stream)
    seconds = int((end_second_stream - start_second_stream))
    for i in range(0, 90):
        if seconds % 90 != 0:
            seconds += i
    part_of_video = int((seconds) / 90) #we're parting videos by 90 seconds. because twitch clip system gives you clips second max 90 second.
    return start_second_stream,end_second_stream,part_of_video,stream_id,file_name1,seconds
