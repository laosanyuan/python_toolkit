import subprocess


def enhance_audio_quality(input_file_path, output_file_path):
    """
    使用FFmpeg提升音频质量至至少320kbps比特率和44.1kHz采样率。

    参数:
    - input_file_path: 输入音频文件路径（MP3或WAV格式）
    - output_file_path: 输出音频文件路径（处理后的MP3文件）

    注意: 确保输入文件为MP3或WAV格式，推荐使用WAV以获得最佳效果。
    """
    # FFmpeg命令构建，转换为高质量MP3
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file_path,  # 输入文件
        "-vn",  # 如果是视频文件，移除视频流
        "-ab", "320k",  # 设置音频比特率为320kbps
        "-ar", "44100",  # 设置采样率为44.1kHz
        "-f", "mp3",  # 输出格式为MP3
        output_file_path  # 输出文件路径
    ]

    # 执行FFmpeg命令
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("音频质量提升完成。")
    except subprocess.CalledProcessError as e:
        print(f"音频处理过程中发生错误: {e}")
        return False

    return True


# 示例调用
input_path = "D://定风波.mp3"
output_path = "D://定风波2.mp3"
enhance_audio_quality(input_path, output_path)
