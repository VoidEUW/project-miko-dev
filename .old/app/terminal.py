import os

class Terminal:
    def __init__(self) -> None:
        self.state = 0

    async def start(self):
        while self.state == 0:
            command = input("Miko> ")
            await self.awaitCommand(command)
        self.state = -1

    async def awaitCommand(self, command: str):
        if len(command) > 0:
            words = command.split()
            match words[0]:
                case "bot":
                    if words[1] != None and words[1] == "-lang":
                        if words[2] != None:
                            print(words[2])
                            pass
                        else:
                            print("Current language")
                            pass
                case "exit":
                    print("exiting...")
                    exit()
                case _:
                    print(f"'{command}': Wrong Command!")
        else:
            return