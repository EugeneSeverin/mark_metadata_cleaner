import subprocess
import shutil
import sys
import os

def check_tools():
    """Проверяем, что ffmpeg и exiftool установлены."""
    if shutil.which("ffmpeg") is None:
        sys.exit("❌ FFmpeg не найден. Установи его и добавь в PATH.")
    if shutil.which("exiftool") is None:
        sys.exit("❌ ExifTool не найден. Установи его и добавь в PATH.")

def convert_to_mov(input_file, clean_file):
    """Конвертируем MP4 → MOV с NVENC (без x264)."""
    cmd = [
        "ffmpeg", "-i", input_file,
        "-c:v", "h264_nvenc", "-profile:v", "high", "-level:v", "3.1",
        "-c:a", "aac", "-profile:a", "aac_low", "-b:a", "64k",
        "-f", "mov", clean_file
    ]
    subprocess.run(cmd, check=True)

def rewrite_metadata(clean_file, output_file):
    """Переписываем метаданные в стиле iPhone."""
    cmd = [
        "ffmpeg", "-i", clean_file,
        "-c", "copy",
        "-map_metadata", "-1",
        # контейнер
        "-metadata", "major_brand=mp42",
        "-metadata", "compatible_brands=isom/mp41/mp42",
        "-metadata", "creation_time=2025-09-16T07:01:23Z",
        "-metadata", "tagged_date=2025-09-16T07:01:24Z",
        "-metadata", "encoder=Apple QuickTime",
        # потоки
        "-metadata:s:v:0", "title=Core Media Video",
        "-metadata:s:v:0", "encoder=Apple H.264",
        "-metadata:s:a:0", "title=Core Media Audio",
        # геолокация (Wisconsin, Madison)
        "-metadata", "com.apple.quicktime.location.ISO6709=+43.0731-089.4012+0.000/",
        output_file
    ]
    subprocess.run(cmd, check=True)

def fix_with_exiftool(file_path):
    """Переписываем скрытые QuickTime-атомы (Software, Encoder)."""
    cmd = [
        "exiftool",
        "-overwrite_original",
        "-QuickTime:Software=Apple QuickTime",
        "-QuickTime:Encoder=Apple H.264",
        file_path
    ]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    check_tools()

    input_file = "input.mp4"
    clean_file = "clean.mov"
    final_file = "final.mov"

    print("▶️ Конвертация MP4 → MOV (NVENC)...")
    convert_to_mov(input_file, clean_file)

    print("✍ Переписываем метаданные (ffmpeg)...")
    rewrite_metadata(clean_file, final_file)

    print("🛠 Чистим служебные поля (ExifTool)...")
    fix_with_exiftool(final_file)

    if os.path.exists(clean_file):
        os.remove(clean_file)
        print(f"🗑 Временный файл {clean_file} удалён.")

    print(f"✅ Готово! Результат сохранён в {final_file}")
