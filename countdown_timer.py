#IMPORTING THE MODULES
import tkinter as tk            #Library to create a graphical user interface
import datetime as dt           #Library to work with date and time datas
import winsound as ws           #Library to play basic sounds

#CREATING COUNTDOWN CLASS
class Countdown(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        #Declaration of all basic functions
        self.create_widgets()
        self.show_widgets()
        #Setting initial timer to 0
        self.seconds_left = 0
        self.timer_on = False

    #FUNCTION TO CREATE WIDGETS
    def create_widgets(self):
        #Adding label and textbox to enter time and set focus on the textbox value
        self.label = tk.Label(self,text="Enter the time in seconds : ")
        self.entry = tk.Entry(self,justify="center")
        self.entry.focus_set()

        #Creating the basoc buttons required
        self.reset = tk.Button(self,text="RESET",command=self.reset_button)
        self.stop = tk.Button(self,text="STOP",command=self.stop_button)
        self.start = tk.Button(self,text="START",command=self.start_button)
   
    #FUNCTION TO DISPLAY THE WIDGETS   
    def show_widgets(self):
        #Packing all elements relative to one another with a y axis padding of 5
        self.label.pack(pady = 5)
        self.entry.pack(pady = 5)
        self.start.pack(pady = 5)
        self.stop.pack(pady = 5)
        self.reset.pack(pady = 5)

    #COUNTDOWN FUNCTION
    def countdown(self):
        self.label["text"] = self.convert_seconds_left_to_time()
        #If time is not 0 continue timer and reduce value one by one second
        if self.seconds_left:
            self.seconds_left -= 1
            self.timer_on = self.after(1000,self.countdown)
        #If time reaches 0 stop the timer and play the sound
        else:
            self.timer_on = False
            ws.PlaySound("TimerSound",ws.SND_FILENAME)

    #RESET BUTTON FUNCTION
    def reset_button(self):
        self.seconds_left = 0
        self.stop_timer()
        self.timer_on = False
        self.label["text"] = "Enter the time in seconds : "
        #Forgetting the widgets 
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        #Packing the widgets 
        self.start.pack(pady = 5)
        self.stop.pack(pady = 5)
        self.reset.pack(pady = 5)

    #START BUTTON FUNCTION
    def start_button(self):
        self.seconds_left = int(self.entry.get())
        self.stop_timer()
        self.countdown()
        #Forgetting the widgets
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        #Packing the widgets
        self.start.pack(pady = 5)
        self.stop.pack(pady = 5)
        self.reset.pack(pady = 5)

    #STOP BUTTON FUNCTION
    def stop_button(self):
        self.seconds_left = int(self.entry.get())
        self.stop_timer()

    #STOP TIMER FUNCTION
    def stop_timer(self):
        if self.timer_on:
            self.after_cancel(self.timer_on)
            self.timer_on = False

    #CONVERTING THE REMAINING TIME
    def convert_seconds_left_to_time(self):
        return dt.timedelta(seconds=self.seconds_left)

#CREATING THE MAIN LOOP
if __name__ == "__main__":
    #Creating the main screen for the timer window
    root = tk.Tk()

    #Initializing the timer
    countdown = Countdown(root)
    countdown.pack()

    #Running and processing all functions and application
    root.mainloop()
