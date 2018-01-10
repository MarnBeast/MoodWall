#!/usr/bin/env python2

import numpy

class Mood:

	def __init__(self, xLen, yLen, zLen):
		self.xLen = xLen
		self.yLen = yLen
		self.zLen = zLen

		self.visual = numpy.zeros((xLen, yLen, zLen)) 

	def tick(self,tickSpeedMs):
		print "tick Mood"
