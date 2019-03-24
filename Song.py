# ex40_3

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
	
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

new_lyrics = ["Un, dos, tres cuatro, somos cuatro",
              "Todos juntos, juntos los cuatro",
			  "Y a Bremen vamos con esta canción",
			  "Con esta canción"]
			 
trotamundos_bremen = Song(new_lyrics)
trotamundos_bremen.sing_me_a_song()