import tkinter as tk
import DaySchedule as daySchedule

class scheduleMainScreen(tk.Tk):
    def __init__(self):
        # Inits frame
        tk.Tk.__init__(self)

        # Creates empty variable for the frame
        self._frame = None

        # Fills the frame with day schedule
        self.switch_frame(daySchedule.scheduleDay)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one.

        #Stores new frame in a variable
        new_frame = frame_class(self)

        # Checks if the current frame isn't empty. If it isn't empty, it destroys the frame
        if self._frame is not None:
            self._frame.destroy()

        # Stores new frame and display
        self._frame = new_frame
        self._frame.pack()
