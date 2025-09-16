# 🎥 MP4 → MOV Converter с метаданными под iPhone

Этот скрипт конвертирует видео **MP4 → MOV** с использованием NVENC и переписывает метаданные так, чтобы файл выглядел как оригинальный с iPhone.  

## ⚡ Возможности

- 🚀 Конвертация **MP4 → MOV** через `ffmpeg`  
- ✍ Переписывание метаданных в стиле Apple  
- 🛠 Очистка скрытых QuickTime-атрибутов через `exiftool`  
- ✅ Совместимость с iOS / macOS плеерами  

---

## 📦 Установка зависимостей

### 🔹 Windows
1. Установи [FFmpeg (Windows builds)](https://www.gyan.dev/ffmpeg/builds/).  
   - Скачай архив **release full**.  
   - Распакуй и добавь путь к `bin/` в **PATH**.  

2. Установи [ExifTool for Windows](https://exiftool.org/).  
   - Скачай `exiftool(-k).exe`.  
   - Переименуй в `exiftool.exe` и положи в папку из PATH (например, `C:\Windows\`).  

3. Убедись, что всё работает:
   ```powershell
   ffmpeg -version
   exiftool -ver
   ```

---

### 🔹 macOS
1. Установи Homebrew (если ещё не установлен):  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Поставь пакеты:
   ```bash
   brew install ffmpeg exiftool
   ```

3. Проверка:
   ```bash
   ffmpeg -version
   exiftool -ver
   ```

---

## ▶️ Запуск скрипта

1. Помести видеофайл `input.mp4` в папку со скриптом.  
2. Запусти:
   ```bash
   python iphonify.py
   ```
3. В результате появится:
   - `clean.mov` — промежуточный файл (удаляется автоматически)  
   - `final.mov` — итоговый файл с метаданными iPhone  

---

## 🧩 Внутренности

- **FFmpeg**: конвертирует MP4 в MOV (кодек `h264_nvenc` / `aac`)  
- **FFmpeg (metadata)**: переписывает контейнерные и потоковые метаданные  
- **ExifTool**: фиксит скрытые поля QuickTime (Software, Encoder)  

---

## ✅ Результат

- `final.mov` выглядит как оригинальное видео с iPhone  
- Метаданные соответствуют Apple QuickTime  
