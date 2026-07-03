from moviepy import VideoFileClip


def compress(input_file, save, bitrate="1000k"):
    """
    Compress video using bitrate.
    """

    clip = VideoFileClip(input_file)

    clip.write_videofile(
        save,
        bitrate=bitrate
    )

    clip.close()