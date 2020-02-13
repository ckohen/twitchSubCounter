# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#           Twitch Sub Counter (for sub points)             #
#           Made by ckohen                                  #
#                                                           #
#               Version 1.0 2/13/2020                       #
#                                                           #
#      If this stops working, contact ckohen on Twitch      #
#   This requires python ver 3.7, firefox, and geckodriver  #
#   Python dependencies: selenium                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Change Variables For Your System Here
# # # # # # # # # #
geckoDriverPath = "" # Full path to the geckodriver executable
firefoxProfilePath = "" #Location of firefox profile (you should login)
subCountFile = ""    # The full path to the file you would like to update the sub count in
updateFrequency = 60    # The amount of time to wait (in seconds) in between automatic updates
# # # # # # # # # #


from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time, ctypes

myappid = u'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Set Up Geckodriver to run in background
def initialize():
    options = Options()
    options.headless = True
    global driver 
    try:
        driver = webdriver.Firefox(firefox_profile = firefoxProfilePath, options = options, executable_path = geckoDriverPath)
    except:
        return False
    driver.implicitly_wait(30)
    return True

dashboard = "https://dashboard.twitch.tv/u/ckohen/stream-manager"
lookingFor = "Subscribers"


# Handles Page Refreshes
def refreshPage():
    try:
        driver.get(dashboard)
    except:
        return False
    try:
        counters = driver.find_elements_by_css_selector(".sunlight-tile")
    except:
        return False
    subCount = False
    for element in counters:
        title = element.find_element_by_css_selector(".sunlight-tile__title").get_attribute("title")
        if title == lookingFor:
            subCount = element.find_element_by_css_selector(".sunlight-tile-body-text").get_attribute("title")
        else:
            pass
    if subCount:
        return subCount
    else:
        return False


# Handles File Output
def updateFile(subCount):
    if subCount:
        pass
    else:
        return False
    try:
        fout = open(subCountFile, "w+")
    except:
        return False
    
    fout.write(subCount)
    fout.close()
    return True

def update(*args):
    count = refreshPage()
    updateFile(count)
    app.after(updateFrequency * 1000, update)

def updateNow(*args):
    count = refreshPage()
    updateFile(count)

def start():
    lines = []
    try:
        fin = open("assets\settings.cfg")
        lines = fin.readlines()
        i = 0
        while i < 3:
            lines[i] = lines[i][:-1]
            i += 1
    except:
        messagebox.showerror("Error", "Please enter variables into options")
        return
    
    print(lines)
    global geckoDriverPath, firefoxProfilePath, subCountFile, updateFrequency
    geckoDriverPath = lines[0]
    firefoxProfilePath = lines[1]
    subCountFile = lines[2]
    updateFrequency = int(lines[3])

    if initialize():
        pass
    else:
        messagebox.showerror("Error", "Invalid file paths detected, please update in options")
        return
    app.after(1000, update)
    updateNowBtn["text"] = "Update Now"
    updateNowBtn["command"] = updateNow

def stop():
    try:
        driver.quit()
    except:
        pass
    sys.exit()
    return


# UX
def on_enterq(e):
    quitBtn['background'] = '#7a797a'

def on_leaveq(e):
    quitBtn['background'] = '#4c4c4c'
    
def on_enteru(e):
    updateNowBtn['background'] = '#7a797a'

def on_leaveu(e):
    updateNowBtn['background'] = '#4c4c4c'

app = Tk("Twitch Sub Point Counter")
app.title("Twitch Sub Point Counter")
app.configure(bg = "#3a393a")
app.resizable(False, False)

updateNowBtn = Button(app, text="Start", command = start, default = ACTIVE)
updateNowBtn.grid(column = 1, row = 1, padx = 20, pady = 20)
updateNowBtn.configure(bg = "#4c4c4c", foreground = "white", activebackground = "#1f1e1f", padx=10, pady=10, border = 0, font = "Helvetica 40 bold")
quitBtn = Button(app, text="Quit", command = stop)
quitBtn.grid(column = 3, row = 1, padx = 20, pady = 20)
quitBtn.configure(bg = "#4c4c4c", foreground = "white", activebackground = "#1f1e1f", padx = 10, pady=10, border = 0, font = "Helvetica 40 bold")

updateNowBtn.focus()
app.bind('<Return>', updateNow)
quitBtn.bind("<Enter>", on_enterq)
quitBtn.bind("<Leave>", on_leaveq)
updateNowBtn.bind("<Enter>", on_enteru)
updateNowBtn.bind("<Leave>", on_leaveu)


# Menu bar options for setup

def quickSetup():
    global geckoDriverPath, firefoxProfilePath, subCountFile, updateFrequency
    messagebox.showinfo("Quick Setup", "A Series of Three File Dialogs will open, please open files in the following order:\n\nGeckoDriver.exe\nFirefox Profile (Folder)\nOutput File\n\nNote: Currently Only Writes Sub Count to File, does not keep exsisting file data")
    geckoDriverPath = filedialog.askopenfilename(title = "Geckodriver.exe", filetypes = [("Executable", "*.exe")])
    firefoxProfilePath = filedialog.askdirectory(title = "Firefox Profile")
    subCountFile = filedialog.asksaveasfilename(title = "Output File", filetypes = [("Text File", "*.txt"),("All Files", "*")])
    updateFrequency = simpledialog.askinteger(title = "Auto Update Frequency", prompt = "Enter the amount of time (in seconds) between auto refreshes (min. 30):", initialvalue = 60, parent = app, minvalue = 30)
    lines = ["\n", "\n", "\n", ""]
    try:
        fin = open("assets\settings.cfg")
        lines = fin.readlines()
        fin.close()
    except:
        pass
    if geckoDriverPath:
        lines[0] = geckoDriverPath + "\n"
    if firefoxProfilePath:
        lines[1] = firefoxProfilePath + "\n"
    if subCountFile:
        lines[2] = subCountFile + "\n"
    if updateFrequency:
        lines[3] = str(updateFrequency)

    fout = open("assets\settings.cfg", "w+")
    fout.writelines(lines)
    fout.close()
    return

def changeGecko():
    lines = ["\n", "\n", "\n", ""]
    try:
        fin = open("assets\settings.cfg")
        lines = fin.readlines()
        fin.close()
    except:
        pass
    global geckoDriverPath
    geckoDriverPath = filedialog.askopenfilename(title = "Geckodriver.exe", filetypes = [("Executable", "*.exe")])
    if geckoDriverPath:
        lines[0] = geckoDriverPath + "\n"
    fout = open("assets\settings.cfg", "w+")
    fout.writelines(lines)
    fout.close()
    return
    
def changeFirefox():
    lines = ["\n", "\n", "\n", ""]
    try:
        fin = open("assets\settings.cfg")
        lines = fin.readlines()
        fin.close()
    except:
        pass
    global firefoxProfilePath
    firefoxProfilePath = filedialog.askdirectory(title = "Firefox Profile")
    if firefoxProfilePath:
        lines[1] = firefoxProfilePath + "\n"
    fout = open("assets\settings.cfg", "w+")
    fout.writelines(lines)
    fout.close()
    return

def changeOutput():
    lines = ["\n", "\n", "\n", ""]
    try:
        fin = open("assets\settings.cfg")
        lines = fin.readlines()
        fin.close()
    except:
        pass
    global subCountFile
    messagebox.showinfo("Output File", "Note: Currently Only Writes Sub Count to File, does not keep exsisting file data")
    subCountFile = filedialog.asksaveasfilename(title = "Output File", filetypes = [("Text File", "*.txt"),("All Files", "*")])
    if subCountFile:
        lines[2] = subCountFile + "\n"
    fout = open("assets\settings.cfg", "w+")
    fout.writelines(lines)
    fout.close()
    return

def changeTime():
    lines = ["\n", "\n", "\n", ""]
    try:
        fin = open("assets\settings.cfg")
        lines = fin.readlines()
        fin.close()
    except:
        pass
    global updateFrequency
    updateFrequency = simpledialog.askinteger(title = "Auto Update Frequency", prompt = "Enter the amount of time (in seconds) between auto refreshes (min. 30):", initialvalue = 60, parent = app, minvalue = 30)
    if updateFrequency:
        lines[3] = str(updateFrequency)
    fout = open("assets\settings.cfg", "w+")
    fout.writelines(lines)
    fout.close()
    return

menubar = Menu(app)
optionsmenu = Menu(menubar, tearoff = 0)
optionsmenu.add_command(label="Quick Setup", command = quickSetup)
optionsmenu.add_command(label="Change Geckodriver", command = changeGecko)
optionsmenu.add_command(label="Change Firefox Profile", command = changeFirefox)
optionsmenu.add_command(label="Change Output File", command = changeOutput)
optionsmenu.add_command(label="Change Update Time", command = changeTime)
menubar.add_cascade(label="Options", menu = optionsmenu)

app.config(menu=menubar)
app.iconbitmap("assets\subcounter.ico")
app.mainloop()
try:
    driver.quit()
except:
    pass