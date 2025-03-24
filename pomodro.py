import pygame
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import cv2
from tkinter import font

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("POMODORO TIMER")
        self.root.geometry("1400x800")
        self.theme = "light"  
        self.set_theme()

        pygame.mixer.init()
        self.volume_level = 0.5  # Default volume level 
        self.play_rain_sound()

        # Background Video
        self.video_path = r"C:\Users\Silky\OneDrive\Desktop\POMODRO PROJECT\vecteezy_ai-generative-the-jungle-is-a-beautiful-place-to-visit-but_33299615.mp4"   #update the path for video
        self.cap = cv2.VideoCapture(self.video_path) 
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.update_background()

        # Timer Variables
        self.work_hours = IntVar(value=0)
        self.work_minutes = IntVar(value=25)
        self.work_seconds = IntVar(value=0)
        
        self.break_hours = IntVar(value=0)
        self.break_minutes = IntVar(value=5)
        self.break_seconds = IntVar(value=0)

        self.remaining_time = 0
        self.total_time = 1  # Prevent division by zero error
        self.is_break = False
        self.running = False
        self.paused = False

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def set_theme(self):
        self.bg_color = "white" if self.theme == "light" else "#222"
        self.text_color = "black" if self.theme == "light" else "white"
        self.button_bg = "#007BFF" if self.theme == "light" else "#444"
        self.button_fg = "white"
        self.progress_color = "#007BFF" if self.theme == "light" else "#555"
        self.root.configure(bg=self.bg_color)

    def play_rain_sound(self):
        pygame.mixer.music.load(r"C:\Users\Silky\OneDrive\Desktop\POMODRO PROJECT\calming-rain-257596.mp3")   #update for backgroung sound
        pygame.mixer.music.set_volume(self.volume_level)
        pygame.mixer.music.play(-1)

    def update_background(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (1400, 800))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.bg_label.config(image=img)
            self.bg_label.image = img
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.root.after(30, self.update_background)

    def create_widgets(self):
        frame = Frame(self.root, bg=self.bg_color)
        frame.place(relx=0.5, rely=0.3, anchor=N)

        Label(frame, text="WORK TIMER", font=("Georgia", 20, "bold"), fg=self.text_color, bg=self.bg_color).grid(row=0, column=0, columnspan=3, pady=10)
        self.create_time_inputs(frame, 1, self.work_hours, self.work_minutes, self.work_seconds)

        Label(frame, text="BREAK TIMER", font=("Georgia", 20, "bold"), fg=self.text_color, bg=self.bg_color).grid(row=3, column=0, columnspan=3, pady=10)
        self.create_time_inputs(frame, 4, self.break_hours, self.break_minutes, self.break_seconds)
          #start button
        self.start_btn = Button(frame, text="START", command=self.start_timer, font=("Georgia", 16, "bold"), fg=self.button_fg, bg=self.button_bg)
        self.start_btn.grid(row=6, column=0, pady=10, padx=5)
          #pause button
        self.pause_btn = Button(frame, text="PAUSE", command=self.pause_timer, font=("Georgia", 16, "bold"), fg=self.button_fg, bg=self.button_bg)
        self.pause_btn.grid(row=6, column=1, pady=10, padx=5)
          #resume button
        self.resume_btn = Button(frame, text="RESUME", command=self.resume_timer, font=("Georgia", 16, "bold"), fg=self.button_fg, bg=self.button_bg)
        self.resume_btn.grid(row=6, column=2, pady=10, padx=5)
           #reset button
        self.reset_btn = Button(frame, text="RESET", command=self.reset_timer, font=("Georgia", 16, "bold"), fg=self.button_fg, bg=self.button_bg)
        self.reset_btn.grid(row=7, column=1, pady=10, padx=5)
            #timer label
        self.timer_label = Label(self.root, text="00:00:00", font=("Arial", 48, "bold"), fg="white", bg="black")
        self.timer_label.place(relx=0.5, rely=0.85, anchor=CENTER)
           #progress bar
        self.progress = ttk.Progressbar(self.root, length=500, mode="determinate")
        self.progress.place(relx=0.5, rely=0.95, anchor=CENTER)

        # Add a default font size
        self.notes_font = font.Font(family="Arial", size=14)
        # Notes Box - Top Right
        self.notes_label = Label(self.root, text="Notes:", font=("Helvetica", 16, "bold"), bg=self.bg_color, fg=self.text_color)
        self.notes_label.place(relx=0.98, rely=0.05, anchor=NE)  
        self.notes_box = Text(self.root, height=8, width=40, font=self.notes_font)
        self.notes_box.place(relx=0.98, rely=0.15, anchor=NE)  

       # Bold Text Button
        self.bold_btn = Button(self.root, text="B", command=self.make_bold, font=("Helvetica", 12, "bold"), width=4)
        self.bold_btn.place(relx=0.85, rely=0.35, anchor=NE)

      # Italic Text Button
        self.italic_btn = Button(self.root, text="I", command=self.make_italic, font=("Helvetica", 12, "italic"), width=4)
        self.italic_btn.place(relx=0.90, rely=0.35, anchor=NE)

      # Increase Font Size Button
        self.increase_font_btn = Button(self.root, text="A+", command=self.increase_font, font=("Helvetica", 12), width=4)
        self.increase_font_btn.place(relx=0.95, rely=0.35, anchor=NE)

      # Decrease Font Size Button
        self.decrease_font_btn = Button(self.root, text="A-", command=self.decrease_font, font=("Helvetica", 12), width=4)
        self.decrease_font_btn.place(relx=0.98, rely=0.35, anchor=NE)


        # Volume Slider
        self.volume_slider = Scale(self.root, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, label="Volume", command=self.adjust_volume)
        self.volume_slider.set(self.volume_level)
        self.volume_slider.place(relx=0.85, rely=0.9, anchor=CENTER)
      
      #functions for start, pause, resume, notes label 

    def create_time_inputs(self, frame, row, hours_var, minutes_var, seconds_var):
        font_style = ("Georgia", 20, "bold")  
        width = 7  
        Entry(frame, textvariable=hours_var, width=5).grid(row=row + 1, column=0)
        Entry(frame, textvariable=minutes_var, width=5).grid(row=row + 1, column=1)
        Entry(frame, textvariable=seconds_var, width=5).grid(row=row + 1, column=2)

    def start_timer(self):
        self.running = True
        self.paused = False
        self.is_break = False
        self.remaining_time = (self.work_hours.get() * 3600) + (self.work_minutes.get() * 60) + self.work_seconds.get()
        self.total_time = self.remaining_time
        self.run_timer()

    def pause_timer(self):
        self.paused = True

    def resume_timer(self):
        if self.paused:
            self.paused = False
            self.run_timer()

    def run_timer(self):
        if self.remaining_time >= 0 and self.running and not self.paused:
            self.update_timer_display()
            progress_value = ((self.total_time - self.remaining_time) / self.total_time) * 100
            self.progress["value"] = progress_value
            self.remaining_time -= 1
            self.root.after(1000, self.run_timer)
        elif self.running and not self.paused:
            if not self.is_break:
                messagebox.showinfo("Pomodoro Timer", "Work Session Complete! Starting Break...")
                self.is_break = True
                self.remaining_time = (self.break_hours.get() * 3600) + (self.break_minutes.get() * 60) + self.break_seconds.get()
                self.total_time = self.remaining_time
                self.run_timer()
            else:
                messagebox.showinfo("Pomodoro Timer", "Break Session Complete!")

    def reset_timer(self):
        self.running = False
        self.paused = False
        self.timer_label.config(text="00:00:00")
        self.progress["value"] = 0

    def clear_notes(self):
       self.notes_box.delete("1.0", END)
    
    def make_bold(self):
        """Apply bold formatting to selected text."""
        try:
             selected_text = self.notes_box.tag_ranges("sel")
             if selected_text:
                self.notes_box.tag_add("bold", "sel.first", "sel.last")
                self.notes_box.tag_configure("bold", font=("Arial", 14, "bold"))
        except:
             pass  # Avoid error if no text is selected

    def make_italic(self):
        """Apply italic formatting to selected text."""
        try:
             selected_text = self.notes_box.tag_ranges("sel")
             if selected_text:
                self.notes_box.tag_add("italic", "sel.first", "sel.last")
                self.notes_box.tag_configure("italic", font=("Arial", 14, "italic"))
        except:
             pass

    def increase_font(self):
        """Increase font size."""
        current_size = self.notes_font["size"]
        self.notes_font.configure(size=current_size + 2)

    def decrease_font(self):
        """Decrease font size."""
        current_size = self.notes_font["size"]
        if current_size > 8:  # Prevent too small fonts
            self.notes_font.configure(size=current_size - 2)



    def update_timer_display(self):
        hours, remainder = divmod(self.remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

    def adjust_volume(self, val):
        self.volume_level = float(val)
        pygame.mixer.music.set_volume(self.volume_level)

    def on_close(self):
        pygame.mixer.music.stop()
        self.cap.release()
        self.root.destroy()

#run the application
root = Tk()
PomodoroApp(root)
root.mainloop()
