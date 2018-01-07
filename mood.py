#!/usr/bin/env python2

import mood_time

class Mood:

	def __init__(self, xLen, yLen, zLen, timeSec=0.0):
		self._xLen = xLen
		self._yLen = yLen
		self._xLen = zLen

		if timeSec > 0.0:
			self._timeSec = timeSec
		else:
			self._timeSec = mood_time.current_time_sec()

		self._timingMs = mood_time.time_to_timing_ms(self._timeSec)

	def getTime(self):
		return self._timeSec 

	def getTimingMs(self):
		return self._timingMs

	def tick(self,tickSpeedMs):
		print "tick Mood {}".format(self.getTimingMs())
