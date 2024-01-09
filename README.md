# Classroom_Bell

Play some sound at assigned time each day, like the bell in a classroom.

## For Windows

### Requirements

Requires python. Requies a music player (I use ffplay from ffmpeg).

> pip install pystray
> 
> pip install datetime

### Usage

- Prepare an `icon.png` and `sound.mp3`, and place them beside the code.
  
- Modify the code to specify the system command for playing the sound.
  
- Modify the `time_list` to specify the hour:time you want to play the sound.
  
- Run with `pythonw.exe` to bring it to background. You may also create a bat file with `START /B C:<PATH TO PYTHON>\pythonw.exe bell_windows.py` so one click does everything.
  
- The icon should appear in the system tray. Right-click it to exit.
  

## For Android

An initial version is uploaded (2024-01-09).

This part is built on this [Document for Android Studio](https://developer.android.com/training/scheduling/alarms?hl=zh-cn).

### Usage

- Download and install the APK. It should not ask for sensitive permissions and should not be able to connect to network.
  
- Start the app and tap on the (only) button to switch on. When re-entering the app, the button will show the status (on/off) of the alarms.
  
- The phone will show a notification and play a sound at pre-defined times. Current version does not support modification of the schedule. You can modify the code and build your own.
  
- You may disable banners, vibrations, and notifications in your phone's settings, if they are available.
  
- The sound is played using system media player. This means that 1) the volume is controlled by "media"; 2) the sound is played even if you put your phone into "vibrate" or "silent" mode.
  
- For some phones the sound and the notifications do not go off at accurate times, or even do not go off at all. It is suggested that this app be allowed to run at background without constraints. It should not consume much battery.
  

### Note

- I only have one phone so I cannot ensure this app runs fine on other phones.
  
- It seems difficult to ensure the alarm is played on time when a higher level of API is used. Using a lower level does not have this problem; however, it prevents publishing on the play store. Current version probably will raise a security warning during installation due to unknown developer.
  
