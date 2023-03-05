# Classroom_Bell

Play some sound at assigned time each day, like the bell in a classroom.

## Requirements

Currently only for Windows. Requires python. Requies a music player (I use ffplay from ffmpeg).

> pip install pystray
> 
> pip install datetime

## How to use

- Prepare an `icon.png` and `sound.mp3`, and place them beside the code.
  
- Modify the code to specify the system command for playing the sound.
  
- Modify the `time_list` to specify the hour:time you want to play the sound.
  
- Run with `pythonw.exe` to bring it to background. You may also create a bat file with `START /B C:<PATH TO PYTHON>\pythonw.exe bell_windows.py` so one click does everything.
  
- The icon should appear in the system tray. Right-click it to exit.
