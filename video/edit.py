from moviepy import VideoFileClip


def trim(input_file, start, end, save):
    """
    Trim video.
    """

    clip = VideoFileClip(input_file)

    clip = clip.subclipped(start, end)

    clip.write_videofile(save)

    clip.close()


def resize(input_file, width, height, save):
    """
    Resize video.
    """

    clip = VideoFileClip(input_file)

    clip = clip.resized((width, height))

    clip.write_videofile(save)

    clip.close()


def rotate(input_file, angle, save):
    """
    Rotate video.
    """

    clip = VideoFileClip(input_file)

    clip = clip.rotated(angle)

    clip.write_videofile(save)

    clip.close()