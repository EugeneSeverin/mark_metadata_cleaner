import subprocess
import shutil
import sys
import os

def check_tools():
    """Проверяем, что ffmpeg, exiftool и AtomicParsley установлены."""
    for tool in ["ffmpeg", "exiftool", "AtomicParsley"]:
        if shutil.which(tool) is None:
            sys.exit(f"❌ {tool} не найден. Установи его и добавь в PATH.")

def fix_with_atomicparsley(file_path):
    """AtomicParsley работает только с MP4/M4V/M4A."""
    cmd = [
        "AtomicParsley", file_path, "--overWrite",
        "--title", "Core Media Video",
        "--artist", "Apple",
        "--album", "iPhone 13 Pro",
        "--comment", "Recorded on iOS 16.6.1",
        "--stik", "Camera",
        "--genre", "Video"
    ]
    subprocess.run(cmd, check=True)

def convert_to_mov(input_mp4, final_mov):
    """Конвертация MP4 → MOV с айфоноподобными параметрами и метаданными."""
    cmd = [
        "ffmpeg", "-i", input_mp4,
        # Видео как у iPhone: H.264 High@L4.0
        "-c:v", "libx264", "-profile:v", "high", "-level:v", "4.0",
        "-pix_fmt", "yuv420p",
        "-preset", "medium", "-crf", "20",
        # Аудио: AAC LC (mp4a-40-2)
        "-c:a", "aac", "-profile:a", "aac_low", "-b:a", "128k",
        # Сбрасываем старые метаданные
        "-map_metadata", "-1",
        # Добавляем айфоновские
        "-metadata", "com.apple.quicktime.make=Apple",
        "-metadata", "com.apple.quicktime.model=iPhone 13 Pro",
        "-metadata", "com.apple.quicktime.software=iOS 16.6.1",
        "-metadata", "com.apple.quicktime.creationdate=2025-09-16T07:01:23+0000",
        "-metadata", "major_brand=mp42",
        "-metadata", "compatible_brands=isom/mp41/mp42",
        "-metadata", "creation_time=2025-09-16T07:01:23Z",
        "-metadata", "tagged_date=2025-09-16T07:01:24Z",
        "-metadata", "encoder=Apple QuickTime",
        # Потоки
        "-metadata:s:v:0", "title=Core Media Video",
        "-metadata:s:v:0", "encoder=Apple H.264",   # Затираем x264 core
        "-metadata:s:a:0", "title=Core Media Audio",
        # Гео
        "-metadata", "com.apple.quicktime.location.ISO6709=+43.0731-089.4012+0.000/",
        final_mov
    ]
    subprocess.run(cmd, check=True)

def fix_with_exiftool(file_path):
    """Дописываем QuickTime-атрибуты."""
    cmd = [
        "exiftool",
        "-overwrite_original",
        "-QuickTime:Make=Apple",
        "-QuickTime:Model=iPhone 13 Pro",
        "-QuickTime:Software=iOS 16.6.1",
        "-QuickTime:CreationDate=2025:09:16 07:01:23",
        file_path
    ]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    check_tools()

    input_file = "input.mp4"
    final_file = "final.mov"

    print("🎨 Добавляем метаданные (AtomicParsley, MP4)...")
    fix_with_atomicparsley(input_file)

    print("✍ Конвертируем MP4 → MOV с айфоноподобными параметрами...")
    convert_to_mov(input_file, final_file)

    print("🛠 Чистим и дописываем поля (ExifTool, MOV)...")
    fix_with_exiftool(final_file)

    print(f"✅ Готово! Результат сохранён в {final_file}")
