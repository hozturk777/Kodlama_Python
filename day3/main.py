class Human:
    name = "Hüseyin"
    def __init__(self):
        print("init kısmı\n")
    
    def __str__(self) -> str:
        return f"STR : {self.name}"

    def talkHuman(self, sentence):
        print(f"{self.name} {sentence}")

    def walkHuman(self):
        print("Human is Walking ...")

human = Human() #instance
human.talkHuman("Merhaba")
human.walkHuman()
print(human)
 