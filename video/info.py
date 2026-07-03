from moviepy import VideoFileClip


def duration(input_file):
    clip = VideoFileClip(input_file)

    value = clip.duration

    clip.close()

    return value


def resolution(input_file):
    clip = VideoFileClip(input_file)

    value = clip.size

    clip.close()

    return value


def fps(input_file):
    clip = VideoFileClip(input_file)

    value = clip.fps

    clip.close()

    return value


def metadata(input_file):
    clip = VideoFileClip(input_file)

    data = {
        "duration": clip.duration,
        "fps": clip.fps,
        "resolution": clip.size,
    }

    clip.close()

    return data