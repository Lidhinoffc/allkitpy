from moviepy import VideoFileClip, concatenate_videoclips


def merge(files, save):
    """
    Merge multiple videos.
    """

    clips = []

    for file in files:
        clips.append(VideoFileClip(file))

    final = concatenate_videoclips(clips)

    final.write_videofile(save)

    final.close()

    for clip in clips:
        clip.close()