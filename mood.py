#!/usr/bin/env python2

import numpy

class Mood:

	def __init__(self, name, xLen, yLen, zLen):
		self.name = name
		self.xLen = xLen
		self.yLen = yLen
		self.zLen = zLen

		self.visual = numpy.zeros((xLen, yLen, zLen)) 

	def tick(self,tickSpeedMs):
		print "tick Mood"

	def __str__(self):
		return self.name
