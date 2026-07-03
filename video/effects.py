from moviepy import VideoFileClip
from moviepy.video.fx.MultiplySpeed import MultiplySpeed


def speed(input_file, factor, save):
    """
    Change playback speed.
    """

    clip = VideoFileClip(input_file)

    clip = clip.with_effects(
        [MultiplySpeed(factor=factor)]
    )

    clip.write_videofile(save)

    clip.close()


def reverse(input_file, save):
    """
    Reverse video.
    """

    clip = VideoFileClip(input_file)

    clip = clip.time_transform(
        lambda t: clip.duration - t
    )

    clip.write_videofile(save)

    clip.close()


def mute(input_file, save):
    """
    Remove audio.
    """

    clip = VideoFileClip(input_file)

    clip = clip.without_audio()

    clip.write_videofile(save)

    clip.close()