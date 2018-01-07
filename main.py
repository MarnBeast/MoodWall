#!/usr/bin/env python2

from mood_loader import MoodLoader
from view_controller import ViewController
from mood_engine import MoodEngine

def main():

	tickSpeedMs = 100
	fadeSpeedMs = 10000

	xLen = 30
	yLen = 60
	zLen = 1

	moodLoader = MoodLoader(xLen, yLen, zLen)
	viewController = ViewController()

	moodEngine = MoodEngine(moodLoader, viewController)
	moodEngine.start(tickSpeedMs, fadeSpeedMs)


if __name__ == '__main__':
	main()
