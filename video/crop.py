from moviepy import VideoFileClip


def crop(input_file, x1, y1, x2, y2, save):
    """
    Crop video.
    """

    clip = VideoFileClip(input_file)

    clip = clip.cropped(
        x1=x1,
        y1=y1,
        x2=x2,
        y2=y2
    )

    clip.write_videofile(save)

    clip.close()