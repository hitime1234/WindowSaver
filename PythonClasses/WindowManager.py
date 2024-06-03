import subprocess
import time
import pyautogui
import psutil


class WindowManager:
    def __init__(self):
        self._window = None

    def launch_notepad(self):
        subprocess.Popen("notepad.exe")
        time.sleep(0.5)
        self._window = pyautogui.getActiveWindow()
        return self._window

    def move_window(self, x, y):
        self._window.moveTo(x, y)

    def resize_window(self, width, height):
        self._window.resizeTo(width, height)
        
    def get_window_id(self):                
        pid = -1
        process_name = self.get_window_title()
        for proc in psutil.process_iter():
            for item in process_name.split(" ")[len(process_name.split(" "))-1].split("."):
                if item.lower() in proc.name().lower():
                    print(proc.name())
                    pid = proc.pid
                    return pid
        return pid
    

    def get_window_title(self):
        title = self._window.title
        return title
    
    def get_window_size(self):
        sizeX, sizeY = (self.get_window_coordinates_BR()[0] - self.get_window_coordinates_BL()[0]), (self.get_window_coordinates_BL()[1] - self.get_window_coordinates_TL()[1])
        return sizeX, sizeY
    
    def get_window(self):
        return self._window
    
    def set_window(self, window):
        self._window = window
        return self._window
        
    
        
    
    # Get the coordinates of the window
    def get_window_coordinates_TL(self):
        top_left = self._window.topleft.x, self._window.topleft.y
        return top_left
    def get_window_coordinates_BR(self):
        bottom_right = self._window.bottomright.x, self._window.bottomright.y
        return bottom_right
    def get_window_coordinates_TR(self):
        top_right = self._window.topright.x, self._window.topright.y
        return top_right
    def get_window_coordinates_BL(self):
        bottom_left = self._window.bottomleft.x, self._window.bottomleft.y
        return bottom_left
    
    def close_window(self):
        self._window.close()

    def launch_process(self, process):
        subprocess.Popen(process)
        self._window = pyautogui.getActiveWindow()
        return self._window

    def set_active_window(self):
        self._window = pyautogui.getActiveWindow()
        return self._window

    
    #Get Executable
    def get_executable(self):
        pid = self.get_window_id()
        path = psutil.Process(pid).exe()
        return path

    





# Path: main.py
# Import the WindowManager class from windowManager.py
# Create an instance of the WindowManager class
# Launch Notepad and get the active window
# Test Class Methods
if __name__ == "__main__":
    # Create an instance of the WindowManger class
    wm = WindowManager()

    # Launch Notepad and get the active window
    np = wm.launch_notepad()

    # Get the top left coordinates of the active window
    current_cord = np.topleft
    print(current_cord)

    # Move the window to new coordinates
    wm.move_window(900, 200)

    # Resize the window
    wm.resize_window(1000, 100)

    # Get the updated top left and bottom right coordinates of the window
    current_cord = np.topleft
    print(current_cord)
    current_cord = np.bottomright
    print(current_cord)
    print(wm.get_window_size())
    print(wm.get_executable())
    # Close the window
    wm.close_window()


