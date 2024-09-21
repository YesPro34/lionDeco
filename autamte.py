import moviepy.editor as mp
import os

def compress_video(input_path, output_path, target_resolution=(1280, 720), bitrate="800k"):
    # Load the video
    video = mp.VideoFileClip(input_path)
    
    # Resize the video (optional, based on the target resolution)
    video_resized = video.resize(newsize=target_resolution)

    # Write the video with reduced bitrate
    video_resized.write_videofile(output_path, codec='libx264', bitrate=bitrate, audio_codec="aac")
    
    print(f"Compressed video saved as {output_path}")

# Path to the original video and where to save the compressed version
input_video_path = 'public/videos/about-video.mp4'
output_video_path = 'public/videos/compressed-about-video.mp4'

# Compress the video
compress_video(input_video_path, output_video_path, target_resolution=(1280, 720), bitrate="800k")
