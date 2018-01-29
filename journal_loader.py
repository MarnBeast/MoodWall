
import csv
from datetime import datetime

import mood_time
from journal import Journal
from mood_factory import MoodFactory

class JournalLoader:

	def __init__(self, xLen, yLen, zLen, journalCsv):
		self._xLen = xLen
		self._yLen = yLen
		self._zLen = zLen
		self._journalCsv = journalCsv
	
		self._moodFactory = MoodFactory(self._xLen, self._yLen, self._zLen)
		self._journalList = []

		self._testJournal =  Journal(self._xLen, self._yLen, self._zLen, 0)
		self._testJournal.addMood(self._moodFactory.makeMood("TestMood"), 100)
	



	def loadJournals(self):
		journalList = []
		first = True
	
		with open(self._journalCsv, 'rb') as csvfile:
			journalReader = csv.reader(csvfile)	

			for row in journalReader:
				if first:
					first = False
					continue

				journal = Journal(self._xLen, self._yLen, self._zLen)
				
				print "{} {} {} {} {} {} {} {}".format( \
					row[0], row[1], row[2], row[3], \
					row[4], row[5], row[6], row[7])

				# Timestamp = row[0]
				journal.work_text = row[1].strip()
				journal.misc_text = row[2].strip()
				journal.eventful = int(row[3])
				journal.moods = self.parseMoodList(row[4], journal)
				
				date = row[5]
				time = row[6]
				journal.setTimeSec(self.parseDateTime(date, time))				
				journal.weights = [int(w) for w in row[7].split(",")]
	
				journalList.append(journal)

		self._journalList = journalList
		print "list: " + str(len(journalList)) + " self: " + str(len(self._journalList))
		return journalList


	def parseDateTime(self, dateStr, timeStr):
		parseStr = "{} {}".format(dateStr, timeStr)
		datetimeObj = datetime.strptime(parseStr, '%m/%d/%Y %I:%M:%S %p')
		return mood_time.datetime_to_time_sec(datetimeObj)


	def parseMoodList(self, moodListStr, journal):
		moodList = []
		
		moodStrings = moodListStr.split(",")
		for moodString in moodStrings:
			mood = self._moodFactory.makeMood(moodString.strip())
			moodList.append(mood)

		return moodList

	def getCurrentJournal(self):
		currentTimingMs = mood_time.current_timing_ms()
		retJournal = self._testJournal

		#print "curr self: " + str(len(self._journalList))
		for journal in self._journalList:
			if retJournal is self._testJournal:
				retJournal = journal

			#print "now " + str(currentTimingMs) + " then " + str(journal.timingMs) + " " + str(journal)
			if currentTimingMs > journal.timingMs and \
			   journal.timingMs > retJournal.timingMs:
				retJournal = journal
				
		#print "CurrentJournal: " + str(retJournal)
		return retJournal		
	
	def getNextJournal(self):
		currentTimingMs = mood_time.current_timing_ms()
		retJournal = self._testJournal

		#print "next self: " + str(len(self._journalList))
		for journal in self._journalList:
	
			#print "now " + str(currentTimingMs) + " then " + str(journal.timingMs) + " " + str(journal)	
			if currentTimingMs < journal.timingMs:
				if retJournal is self._testJournal or \
				   journal.timingMs < retJournal.timingMs:
					retJournal = journal

		#print "NextJournal: " + str(retJournal)				
		return retJournal		
	
	
