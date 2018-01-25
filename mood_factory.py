
import mood_time
from mood import Mood

class MoodFactory:

	def __init__(self, xLen, yLen, zLen):
		self._xLen = xLen
		self._yLen = yLen
		self._zLen = zLen
	

	def makeMood(self, moodString):
		# TODO: Temporary for testing
		return Mood(moodString, self._xLen, self._yLen, self._zLen)


