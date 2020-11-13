import requests, time, random, json
from authkey import authKey

whereTo = input("Where would you like to send these messages? Enter the channel ID. ")

URL = "https://discordapp.com/api/v8/channels/" + whereTo.strip() + "/messages"

whatToType = input("What would you like me to say? ")

howMany = input(
    "How many times would you like me to message it? Type 'f' for me to message it forever. "
)


howFast = input("How fast would you like for me to send messages? ")

timeLeft = int(howFast)

currentID = None

def editMsg(target, text):
    res = requests.patch(
        url="https://discordapp.com/api/v8/channels/"
        + whereTo.strip()
        + "/messages/"
        + str(target),
        json={
            "content": whatToType
            + " The next message will be sent in "
            + str(text)
            + " seconds."
        },
        headers={
            "authorization": authKey
        },
    )
    print(res.status_code)
    return res.ok


def sendMsg():
    res = requests.post(
        url=URL,
        data={
            "content": whatToType
            + " This message is currently loading.",
            "nonce": 77354876 + random.randint(11111, 99999),
            "tts": False,
        },
        headers={
            "authorization": authKey
        },
    )
    if res.ok:
        print("Just sent a message.")
        global currentID
        currentID = json.loads(res.text)["id"]

    else:
        print("Response was not okay.")


if howMany == "f":
    print("Sending '" + whatToType + "' every " + str(howFast) + " seconds, forever.")
    while True:
        sendMsg()
        startTime = time.time()
        while time.time() - startTime < int(howFast):
            editMsg(currentID, int(timeLeft - (time.time() - startTime)))
            if editMsg:
                time.sleep(1)
            else:
                time.sleep(2.5)

else:
    print(
        "Sending '"
        + whatToType
        + "' every "
        + str(howFast)
        + " seconds, "
        + howMany
        + " times."
    )
    for i in range(int(howMany)):
        sendMsg()
        startTime = time.time()
        while time.time() - startTime < int(howFast):
            editMsg(currentID, int(timeLeft - (time.time() - startTime)))
            time.sleep(1)
