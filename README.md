# POMODRO_TIMER
PROJECT ON POMODRO FULLY BASED ON PYTHON.

Libraries used: tkinter(GUI Developement), pygame(audio management), PIL and cv2(for video management).

Back-end is made from tkinter python GUI library. Front-end is made from python language.
This project focuses on work and break timer. The work timer is set initially on 25 minutes and break timer is set on 5 minutes. The user can change the time inputs for both according to them. After the work timer is finished a notification will pop and then break timer will start immdiately after clicking the notification.

There is a video playing on the background. In this code, a picture of rain forest is there but that can be changed according to the video that will be replaced in place of video path. Video playing is handled by cv2 library so that it plays smoothly and is on loop until the application is exited.
A background noise is also used that is played repeatedly by using pygame library. In this code, rain sound is used which can again be replaced.

Following buttons are present in the application:
1) Start- Starts the timer.
2) Reset- After the work and break timer are finished reset button is used for resetting the time inputs and again running the timer.
3) Pause- Pauses the the timer.
4) Resume- Resumes the timer from where the timer is paused.
5) Volume slider- Initially set on 0.5. User can use the slider to lower the sound or to max the sound.
6) Progress bar- Starts when the timer starts seperately for work or break timer. Reset button is also used to reset the progress bar.
7) Notes section- Users can use this section to write notes. There is a bold, italic and increase or decrease the notes box size. When the application is exited, notes are deleted but not when the reset button is used. Whenver the user wants to write notes that they want to memorise then this section is useful.
 
