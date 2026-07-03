from moviepy import VideoFileClip


def extract_audio(input_file, save):
    """
    Extract audio from video.
    """

    clip = VideoFileClip(input_file)

    clip.audio.write_audiofile(save)

    clip.close()