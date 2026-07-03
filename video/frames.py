from moviepy import VideoFileClip
import os


def extract_frames(input_file, folder, fps=1):
    """
    Save frames as PNG images.
    """

    os.makedirs(folder, exist_ok=True)

    clip = VideoFileClip(input_file)

    clip.write_images_sequence(
        os.path.join(folder, "frame_%05d.png"),
        fps=fps
    )

    clip.close()