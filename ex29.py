class Song(object):

	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:		
			print line

happy_bday = Song(["Happy Birthday to you"
		    "I dont want to get sued"
		    "So I'll stop right here"])

bulls_on_parade = "They rally around the family With pockets ful of shells"

test = Song(bulls_on_parade)

happy_bday.sing_me_a_song()

test.sing_me_a_song()
