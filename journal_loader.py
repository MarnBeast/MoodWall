
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
		journals = self.loadJournals()
		return journals[0]		
	
	def getNextJournal(self):
		# TODO: Temporary for testing
		journal =  Journal(self._xLen, self._yLen, self._zLen, mood_time.current_time_sec() + 30.0)
		journal.addMood(self._moodFactory.makeMood("TMood"), 40)
		journal.addMood(self._moodFactory.makeMood("UMood"), 60)
		return journal

'''
	def getCurrentJournal(self):
		with open(self._journalCsv, 'rb') as csvfile:
			journalReader = csv.reader(csvfile)
			
			column = 0
			journal = Journal(self._xLen, self._yLen, self._zLen)
			moodList = []

			for cell in journalReader:

				if column = 8:
					column = 0

				if column = 0:
					# Timestamp (ignore)

				else if column = 1:
					# Work text
					journal.work_text = cell

				else if column = 2:
					# Not Work text
					journal.mist_text = cell

				else if column = 3:
					# Eventful
					journal.eventful = int(cell)

				else if column = 4:
					# Mood
					moodList = parseMoodList(cell, journal)

				else if column = 5:
					# Date

				else if column = 6:
					# Time

				else if column = 7:
					# Mood Weights 
					journal.weights = cell.split(",")


				column+=1




		# TODO: Temporary for testing
		
		journal = Journal(self._xLen, self._yLen, self._zLen)
		journal.addMood(self._moodFactory.makeMood(), 40)
		journal.addMood(self._moodFactory.makeMood(), 60)
		return journal
'''

