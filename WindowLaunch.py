from WindowManager import WindowManager
import time
import tkinter as tk



class WindowLaunch:
    def __init__(self):
        self.window_manager = WindowManager()
        self.X = 0
        self.Y = 0
        self.SizeX = 0
        self.SizeY = 0
        self.IsMaximized = False
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.ExePath = "Missing.exe"
        self.LoadFromFile = False

        try:
            self.LoadFromConfig()
            self.LoadFromFile = True

        except:
            self.LoadFromFile = False
            print("No config file found")

   


    def create_buttons(self):
        self.root.title("Window Launch")
        button1 = tk.Button(self.root, text="Launch saved window", command=self.Launch)
        button1.pack()
        
        button2 = tk.Button(self.root, text="Save window", command=self.button2_action)
        button2.pack()

        button3 = tk.Button(self.root, text="Present Window", command=self.SetupWindow)
        button3.pack()
        
    
    def Launch(self):
        # Launch window
        if self.LoadFromFile:
            self.window_manager.launch_process(self.ExePath)
            time.sleep(0.5)
            self.window_manager.set_active_window()
            
            if self.IsMaximized:
                self.window_manager.get_window().maximize()
                print("Maximized window")
            else:
                self.window_manager.move_window(self.X, self.Y)
                self.window_manager.resize_window(self.SizeX, self.SizeY)
                print("Resized window")
            print(f"Launched '{self.window_manager.get_window_title()}' at coordinates: {self.X}x{self.Y}, With a size of {self.SizeX}x{self.SizeY}")
        else:
            print("No window saved")

        pass

    def SetupWindow(self):
        self.window_manager.get_window().maximize()
        pass
        
    def button2_action(self):
        # Add your code here for the action of Button 2
        print("Saving window... in 5 seconds")
        time.sleep(5)
        self.window_manager.set_active_window()
        self.X, self.Y = self.window_manager.get_window_coordinates_TL()
        self.SizeX, self.SizeY = self.window_manager.get_window_size()
        print(f"'{self.window_manager.get_window_title()}' saved at coordinates: {self.X}x{self.Y}, With a size of {self.SizeX}x{self.SizeY}")
        if self.window_manager.get_window().isMaximized:
            self.IsMaximized = True
            print("Window is maximized")
        else:
            self.IsMaximized = False
            print("Window is not maximized")

        self.ExePath = self.window_manager.get_executable()
        self.SaveToConfig()
        print("Window saved!")
        pass

    def SaveToConfig(self):
        # Save the window to a config file
        file = open("proc.conf", "w")
        file.write(f"X={self.X}\nY={self.Y}\nSizeX={self.SizeX}\nSizeY={self.SizeY}\nIsMaximized={self.IsMaximized}\nExePath={self.ExePath}")
        file.close()
        print("Saved to proc.conf")
        pass

    def LoadFromConfig(self):
        # Load the window from a config file
        file = open("proc.conf", "r")
        lines = file.readlines()
        for line in lines:
            if "X=" in line:
                self.X = int(line.split("=")[1])
            elif "Y=" in line:
                self.Y = int(line.split("=")[1])
            elif "SizeX=" in line:
                self.SizeX = int(line.split("=")[1])
            elif "SizeY=" in line:
                self.SizeY = int(line.split("=")[1])
            elif "IsMaximized=" in line:
                self.IsMaximized = bool(line.split("=")[1])
            elif "ExePath=" in line:
                self.ExePath = line.split("=")[1]
        print("Loaded from proc.conf")
        pass

    
    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = WindowLaunch()
    window.create_buttons()
    window.mainloop()

