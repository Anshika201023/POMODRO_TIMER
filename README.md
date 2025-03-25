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
 
**PREVIEW OF POMODRO APPLICATION:**
![image](https://github.com/user-attachments/assets/323bdeff-1964-49e3-88e7-848e1a37a3e2)

Setting the work and break time and the notes size is decreased:    ![image](https://github.com/user-attachments/assets/3f659104-c2a9-4c11-b760-8dc19fadf135)

Timer is running for first work timer:   ![image](https://github.com/user-attachments/assets/138397c4-9110-4983-9011-41ce6977217d)
Timer is running for break timer:     ![Screenshot 2025-03-26 020235](https://github.com/user-attachments/assets/788414f8-287a-472a-a036-922476c90050)


Notification is showing end  of break timer(it will also show for work session also):   ![Screenshot 2025-03-26 020750](https://github.com/user-attachments/assets/fa2f00c5-eea6-4a61-b5ef-7f5571218ed3)

Notes section:   ![image](https://github.com/user-attachments/assets/4c99d569-f61e-4c0d-bb77-284d1f40e803)

Volume slider(first was at 0.50 now is at 0.2):   ![image](https://github.com/user-attachments/assets/24ee4a96-c4ab-4bdc-8eca-1c08d21dffa5)





