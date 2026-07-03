from moviepy import VideoFileClip


def split(input_file, duration, output_prefix):
    """
    Split video into equal-length clips.

    Parameters
    ----------
    input_file : str
    duration : int | float
        Duration of each clip in seconds.
    output_prefix : str
    """

    clip = VideoFileClip(input_file)

    total = clip.duration

    start = 0
    part = 1

    while start < total:

        end = min(start + duration, total)

        sub = clip.subclipped(start, end)

        sub.write_videofile(
            f"{output_prefix}_{part}.mp4"
        )

        sub.close()

        start = end
        part += 1

    clip.close()