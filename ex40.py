# Modules, Classes, and Objects

class Song(object) :

    def __init__(self,lyrics):
        self.lyrics = lyrics
        self.shit = "Let's add some spice to the song, shall we?"

    def sing_me_a_song(self,hop):
        for line in self.lyrics:
            print(line,hop)

happy_bday1 = Song(["Happy birthday to you"])
happy_bday2 = Song(["I don't want to get sued"])
happy_bday3 = Song(["So i'll stop right there"])

bulls_on_parade = Song(["They rally aroung the family",
                        "With pockets full of shells"])

balonku = Song(["balon ku ada 5",
                "Rupa-rupa warnanya",
                "Hijau, kuning, kelabu",
                "merah muda dan biru"])

print(happy_bday1.shit)
happy_bday1.shit = "how about add some shit"
print(happy_bday1.shit)
happy_bday1.sing_me_a_song("fucking shit")
happy_bday2.sing_me_a_song("like those shit")
happy_bday3.sing_me_a_song("you heard me shit")

'''print("")

bulls_on_parade.sing_me_a_song()

print("")

balonku.sing_me_a_song()'''
