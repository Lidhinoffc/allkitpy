from moviepy import VideoFileClip


def gif(input_file, save):
    """
    Convert video to GIF.
    """

    clip = VideoFileClip(input_file)

    clip.write_gif(save)

    clip.close()