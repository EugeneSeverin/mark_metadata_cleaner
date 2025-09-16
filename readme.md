# 🎥 MP4 → MOV Converter с айфоновскими метаданными

Скрипт конвертирует видео **MP4 → MOV** с параметрами и метаданными в стиле iPhone.  

---

## ⚡ Возможности

- 🎨 Добавление айфоновских метаданных в MP4 через `AtomicParsley`  
- 🚀 Конвертация **MP4 → MOV** через `ffmpeg` (H.264 + AAC)  
- 🛠 Дополнение QuickTime-атрибутов через `exiftool`  
- ✅ Результат неотличим от оригинала с iPhone  

---

## 📦 Установка зависимостей

### 🔹 Windows
1. Установи [FFmpeg (Windows builds)](https://www.gyan.dev/ffmpeg/builds/).  
   - Скачай архив **release full**.  
   - Распакуй и добавь путь к `bin/` в **PATH**.  

2. Установи [ExifTool for Windows](https://exiftool.org/).  
   - Скачай `exiftool(-k).exe`.  
   - Переименуй в `exiftool.exe` и положи в папку из PATH (например, `C:\Windows\`).  

3. Установи **AtomicParsley**:  
   - Скачай [релиз с GitHub](https://github.com/wez/atomicparsley/releases).  
   - Положи `AtomicParsley.exe` в папку из PATH.  

4. Проверка:
   ```powershell
   ffmpeg -version
   exiftool -ver
   AtomicParsley -v
   ```

---

### 🔹 macOS
1. Установи Homebrew (если ещё не установлен):  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Поставь пакеты:
   ```bash
   brew install ffmpeg exiftool atomicparsley
   ```

3. Проверка:
   ```bash
   ffmpeg -version
   exiftool -ver
   AtomicParsley -v
   ```

---

## ▶️ Запуск скрипта

1. Помести видеофайл `input.mp4` в папку со скриптом.  
2. Запусти:
   ```bash
   python convert.py
   ```
3. В результате появится:
   - `input.mp4` (перезаписанный AtomicParsley)  
   - `final.mov` (итоговый MOV с айфоновскими метаданными)  

---

## 🧩 Внутренности

1. **AtomicParsley**  
   - Добавляет теги (title, artist, album, iPhone 13 Pro, iOS 16.6.1 и др.)  
   - Работает только с MP4/M4V/M4A  

2. **FFmpeg**  
   - Конвертирует MP4 в MOV  
   - Видео: H.264 High@L4.0 (`libx264`)  
   - Аудио: AAC LC 128 kbps  

3. **ExifTool**  
   - Дописывает скрытые QuickTime-атрибуты (Make, Model, Software, CreationDate)  

---

## ✅ Результат

- `final.mov` полностью совместим с iOS и macOS  
- Метаданные и теги идентичны реальным iPhone-видео  
- Можно сразу загружать в соцсети и сервисы без ошибок  
