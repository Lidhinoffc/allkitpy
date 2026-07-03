from moviepy import VideoFileClip


def convert(input_file, save):
    """
    Convert a video to another format.
    """

    video = VideoFileClip(input_file)

    video.write_videofile(save)

    video.close()