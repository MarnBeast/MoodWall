
import mood_time

class MoodEngine:

	def __init__(self, moodLoader, viewController):
		self._moodLoader = moodLoader
		self._viewController = viewController

	def start(self, tickSpeedMs=100, fadeSpeedMs=10000):

		# Get started with our first two moods		
		currentMood = self._moodLoader.getCurrentMood()
		nextMood = self._moodLoader.getNextMood()
		
		fadePercent = 0.0

		while(True):
			startTimingMs = mood_time.current_timing_ms() 
			print "startTimingMs {}".format(startTimingMs)
			print "nextMood getTimingMs {}".format(nextMood.getTimingMs())
			# Check if we are transitioning into our next mood
			if startTimingMs >= nextMood.getTimingMs() - fadeSpeedMs / 2:
				print "A"

				# We are transitioning, but are we done transitioning?
				if startTimingMs >= nextMood.getTimingMs() + fadeSpeedMs / 2:
					print "B"
					# We are done transitioning, change our currentMood
					# and load the next mood.
					currentMood = nextMood
					nextMood = self._moodLoader.getNextMood()
					fadePercent = 0
				else:
					print "C"
					# We are still transitioning
					timeDiffMs = nextMood.getTimingMs() + fadeSpeedMs / 2 - startTimingMs;
					fadePercent = 100.0 - timeDiffMs * 100.0 / fadeSpeedMs

			else:
				print "D"
				fadePercent = 0.0

			# Tick the moods to update their animations
			currentMood.tick(tickSpeedMs)
			nextMood.tick(tickSpeedMs)

			# Update the view with the new mood data
			self._viewController.updateView(currentMood, nextMood, fadePercent)

			# Sleep until we've hit our tick speed
			mood_time.sleep_remainder(startTimingMs, tickSpeedMs)				


	


