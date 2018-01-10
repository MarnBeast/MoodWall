
import mood_time
from journal import Journal

class MoodLoader:

	def __init__(self, xLen, yLen, zLen):
		self._xLen = xLen
		self._yLen = yLen
		self._zLen = zLen
	

	def getCurrentMood(self):
		# TODO: Temporary for testing
		return Journal(self._xLen, self._yLen, self._zLen)

	def getNextMood(self):
		# TODO: Temporary for testing
		return Journal(self._xLen, self._yLen, self._zLen, mood_time.current_time_sec() + 30.0)

