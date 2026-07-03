from moviepy import (
    VideoFileClip,
    ImageClip,
    CompositeVideoClip
)


def watermark(input_file, image, save):
    """
    Add image watermark.
    """

    video = VideoFileClip(input_file)

    logo = (
        ImageClip(image)
        .with_duration(video.duration)
        .with_position(("right", "bottom"))
    )

    final = CompositeVideoClip(
        [video, logo]
    )

    final.write_videofile(save)

    video.close()
    final.close()