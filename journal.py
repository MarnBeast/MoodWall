#!/usr/bin/env python2

import mood_time
from mood import Mood
import numpy

class Journal(Mood):

	def __init__(self, xLen, yLen, zLen, timeSec=0.0):

		Mood.__init__(self, "Journal", xLen, yLen, zLen)
		
		self.setTimeSec(timeSec)	
		self.moods = []
		self.weights = []
		self.work_text = ""
		self.misc_text = ""
		self.eventful = 0

	def addMood(self, mood, percent):
		self.moods.append(mood)
		self.weights.append(percent)

	def tick(self,tickSpeedMs):
		print "tick Mood {}".format(self.timingMs)

	def setTimeSec(self, timeSec):
		if timeSec > 0.0:
			self.timeSec = timeSec
		else:
			self.timeSec = mood_time.current_time_sec()

		self.timingMs = mood_time.time_to_timing_ms(self.timeSec)
		

	def __str__(self):
		moodStr = [str(mood) for mood in self.moods]
		weightStr = [str(weight) for weight in self.weights]
		return "Journal(TimingMs: {} Moods: {} Weights: {}".format(str(self.timingMs), moodStr, weightStr)

