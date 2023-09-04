import json
import os
import time


def remove_color(string, char):
    while char in string:
        index = string.find(char)
        string = string[:index] + string[index + 2:]
    return string


def main():
    count = 0
    try:
        with open("chatlog.json", encoding="utf-8") as f:
            json_file = json.load(f)
    except BaseException as e:
        print(e)
        return
    if "messages" in json_file:
        messages = json_file["messages"]
    else:
        return

    # Open File
    fp = open("chatlog.txt", mode="w+", encoding="utf-8")

    # Every Line
    for message in messages:
        try:
            result = ""
            message = message["extra"]
            is_time = True
            # Every Part
            for msg in message:
                if is_time:
                    # Unix Time
                    result += ("[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(msg["insertion"]) / 1000)) + "] ")
                    is_time = False
                else:
                    # Type Of Message
                    if "translate" in msg:
                        if msg["translate"] == "chat.type.text":
                            if isinstance(msg["with"][1], type("")):
                                result += ("<" + msg["with"][0]["insertion"] + "> " + msg["with"][1])
                            else:
                                result += ("<" + msg["with"][0]["insertion"] + "> " + msg["with"][1]["text"])
                        elif msg["translate"] == "multiplayer.player.joined":
                            result += (msg["with"][0]["insertion"] + " joined the game")
                        elif msg["translate"] == "multiplayer.player.left":
                            result += (msg["with"][0]["insertion"] + " left the game")
                        elif msg["translate"] == "commands.message.display.outgoing":
                            result += ("[me -> " + msg["with"][0]["insertion"] + "] " + msg["with"][1]["text"])
                        elif msg["translate"] == "commands.message.display.incoming":
                            result += ("[" + msg["with"][0]["insertion"] + " -> me] " + msg["with"][1]["text"])
                        else:
                            result += ("[" + msg["with"][0]["insertion"] + "] ! " + msg["translate"] + " !")
                            for t in msg["with"]:
                                result += (" " + t["text"])
                    elif "extra" in msg:
                        for m in msg["extra"]:
                            if isinstance(m, type("")):
                                result += m
                            else:
                                if "translate" in m:
                                    result += ("[" + m["with"][0]["insertion"] + "] ! " + m["translate"] + " !")
                                    for t in m["with"]:
                                        result += (" " + t["text"])
                                elif "extra" in m:
                                    for _m in m["extra"]:
                                        if "extra" in _m:
                                            for __m in _m["extra"]:
                                                result += (__m["text"])
                                        else:
                                            result += _m["text"]
                                else:
                                    result += m["text"]
                    else:
                        result += msg["text"]
            result = remove_color(result, "§")
            fp.write(result)
            fp.write("\n")
            print(result)
            count += 1
        except BaseException as e:
            print(e)
    # Close File
    fp.close()
    print("\n\n" + str(count) + "messages have been processed successfully! \"chatlog.txt\" has been saved in the "
                                "same folder. \n")


if __name__ == "__main__":
    os.system("cls")
    print("This tool is made by dodo939. Before use this tool, make sure you have read \"README.md\" in the same "
          "folder. If not, please close this window and read it first. \n")
    os.system("pause")
    os.system("cls")
    print("Processing...")
    time.sleep(1)
    main()
    os.system("pause")
