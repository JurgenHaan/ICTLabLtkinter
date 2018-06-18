import tkinter as tk
import time
import FrameController
import UnitTest

# Tkinter loop
if __name__ == "__main__":
    suite = UnitTest.unittest.TestLoader().loadTestsFromTestCase(UnitTest.RoomClassTest)
    UnitTest.unittest.TextTestRunner(verbosity=2).run(suite)
    roosterMain = FrameController.scheduleMainScreen()
    roosterMain.geometry("1200x600")
    roosterMain.title("Room signing")
    roosterMain.mainloop()