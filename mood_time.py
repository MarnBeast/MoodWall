#!/usr/bin/env python2

import time
from datetime import datetime

TEST_TIMING = False
SECONDS_IN_WEEK = 604800

# To time this correctly, we want to get time ignoring the year
# in order to match dates from last year up with this year. 
def _calc_jan1Sec():
	year_str = time.strftime("%Y")
	jan1_time = time.strptime(year_str + " Jan 01", "%Y %b %d")
	jan1_sec = time.mktime(jan1_time)
	jan1_ms = int(round(jan1_sec * 1000))

	print "TEST! TIME WAS RUN! JAN1MS WAS CALULATED TO BE {} ms!".format(jan1_ms)

	test = int(round(time.time() * 1000)) - jan1_ms
	print "THAT WOULD MAKE THE CURRENT TIMING {} ms!".format(test)
	return jan1_sec

_jan1Sec = _calc_jan1Sec()
_jan1Ms = int(round(_jan1Sec * 1000))
_epocDatetime = datetime(1970,1,1)

def datetime_to_time_sec(datetimeObj):
	return (datetimeObj - _epocDatetime).total_seconds()

def current_time_sec():
	if TEST_TIMING:
		return _jan1Sec + (time.time() % SECONDS_IN_WEEK)
	else:
		return time.time()

def current_time_ms():
	return int(round(current_time_sec() * 1000))

def current_timing_ms():
	return current_time_ms() - _jan1Ms		

def time_to_timing_ms(argTime):
	return int(round(argTime * 1000)) - _jan1Ms

def sleep_remainder(startTimingMs, targetWakeMs):
        stopTimingMs = current_timing_ms()
        timePassedMs = stopTimingMs - startTimingMs
     
	sleepTimeSec = (targetWakeMs - timePassedMs) / 1000.0
 
	print "sleep remainder of {} seconds".format(sleepTimeSec)
	time.sleep(sleepTimeSec)
