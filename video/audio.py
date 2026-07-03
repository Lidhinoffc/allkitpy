from moviepy import VideoFileClip, AudioFileClip


def add_audio(video_file, audio_file, save):
    """
    Replace video audio.
    """

    video = VideoFileClip(video_file)

    audio = AudioFileClip(audio_file)

    final = video.with_audio(audio)

    final.write_videofile(save)

    video.close()
    audio.close()
    final.close()