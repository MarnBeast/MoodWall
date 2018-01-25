
import mood_time

class MoodEngine:

	def __init__(self, journalLoader, viewController):
		self._journalLoader = journalLoader
		self._viewController = viewController

	def start(self, tickSpeedMs=100, fadeSpeedMs=10000):

		# Get started with our first two moods		
		currentJournal = self._journalLoader.getCurrentJournal()
		nextJournal = self._journalLoader.getNextJournal()
		
		fadePercent = 0.0

		while(True):
			print str(currentJournal)
			print str(nextJournal)
			
			startTimingMs = mood_time.current_timing_ms() 
			print "startTimingMs {}".format(startTimingMs)
			print "nextJournal getTimingMs {}".format(nextJournal.timingMs)
			# Check if we are transitioning into our next mood
			if startTimingMs >= nextJournal.timingMs - fadeSpeedMs / 2:
				print "A"

				# We are transitioning, but are we done transitioning?
				if startTimingMs >= nextJournal.timingMs + fadeSpeedMs / 2:
					print "B"
					# We are done transitioning, change our currentJournal
					# and load the next mood.
					currentJournal = nextJournal
					nextJournal = self._journalLoader.getNextJournal()
					fadePercent = 0
				else:
					print "C"
					# We are still transitioning
					timeDiffMs = nextJournal.timingMs + fadeSpeedMs / 2 - startTimingMs;
					fadePercent = 100.0 - timeDiffMs * 100.0 / fadeSpeedMs

			else:
				print "D"
				fadePercent = 0.0

			# Tick the moods to update their animations
			currentJournal.tick(tickSpeedMs)
			nextJournal.tick(tickSpeedMs)

			# Update the view with the new mood data
			self._viewController.updateView(currentJournal, nextJournal, fadePercent)

			# Sleep until we've hit our tick speed
			mood_time.sleep_remainder(startTimingMs, tickSpeedMs)				


	


