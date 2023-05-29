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

Coming soon.

This part is built on this [Document for Android Studio](https://developer.android.com/training/scheduling/alarms?hl=zh-cn).

### Usage

- Download and install the APK. It should not ask for sensitive permissions and should not be able to connect to the network.
  
- Start the app and tap on the (only) button to switch on. When re-entering the app, the button will show the status (on/off) of the alarms.
  
- The phone will show a notification and play a sound at pre-defined times. Current version does not support modification of the schedule. You can modify the code and build your own.
  
- You may disable banners, vibrations, and notifications in your phone's settings, if they are provided by your phone. If you put your phone into "vibrate" or "silent" mode, the sound will not be played.
  
- If you kill the app, the alarms will be canceled.
  

### Note

- I only have one phone so I cannot test to ensure the app runs fine on other phones.
  
- It seems difficult to ensure the alarm is played on time when a higher level of API is used. Using a lower level does not have this problem; however, it prevents publishing through the play store.
  
- It seems that different models have different policies on controlling the app activities. You may need to allow "run in background" and disable "start automatically".
