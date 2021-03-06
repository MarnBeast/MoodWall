#!/usr/bin/env python2

from journal_loader import JournalLoader
from view_controller import ViewController
from mood_engine import MoodEngine
import mood_time

def main():

	mood_time.TEST_TIMING = True

	tickSpeedMs = 100
	fadeSpeedMs = 10000

	xLen = 30
	yLen = 60
	zLen = 1

	journalCsv = 'tempMarnsJournal.csv'
	
	journalLoader = JournalLoader(xLen, yLen, zLen, journalCsv)
	journalLoader.loadJournals()
	viewController = ViewController()

	moodEngine = MoodEngine(journalLoader, viewController)
	moodEngine.start(tickSpeedMs, fadeSpeedMs)


if __name__ == '__main__':
	main()
