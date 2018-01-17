
import mood_time
from journal import Journal
from mood_factory import MoodFactory

class JournalLoader:

	def __init__(self, xLen, yLen, zLen):
		self._xLen = xLen
		self._yLen = yLen
		self._zLen = zLen
	
		self.moodFactory = MoodFactory(self._xLen, self._yLen, self._zLen)
	

	def getCurrentJournal(self):
		# TODO: Temporary for testing
		
		journal = Journal(self._xLen, self._yLen, self._zLen)
		journal.addMood(self.moodFactory.makeMood(), 40)
		journal.addMood(self.moodFactory.makeMood(), 60)
		return journal

	def getNextJournal(self):
		# TODO: Temporary for testing
		journal =  Journal(self._xLen, self._yLen, self._zLen, mood_time.current_time_sec() + 30.0)
		journal.addMood(self.moodFactory.makeMood(), 40)
		journal.addMood(self.moodFactory.makeMood(), 60)
		return journal
