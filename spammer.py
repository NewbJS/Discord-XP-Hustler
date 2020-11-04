import pyautogui, time, random

whatToType = input("What would you like me to say? ")

howMany = input("How many times would you like me to message it? Type 'f' for me to message it forever. ")

howFast = input("How fast would you like for me to send messages? ")

time.sleep(0.3)

#x:1521 y:1036 screen:0 window:33554440

def messageShit():
    pyautogui.click(x=1521, y=1036)
    time.sleep(0.25)
    pyautogui.typewrite(whatToType + " This message was sent on " + time.asctime() + ". The next message will be sent in " + str(howFast) + " seconds.")
    pyautogui.press("enter")
    print("Just sent a new message.")
    time.sleep(int(howFast))

if howMany.lower() == "f":
    print("Messaging '" + whatToType + "' every " + howFast + " seconds, forever.")
    while True:
        messageShit()
else:
    print("Messaging '" + whatToType + "' every " + howFast + " seconds " + howMany + " times.")
    for i in range(int(howMany)):
        messageShit()