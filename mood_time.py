#!/usr/bin/env python2

import time


# To time this correctly, we want to get time ignoring the year
# in order to match dates from last year up with this year. 
def _calc_jan1ms():
	year_str = time.strftime("%Y")
	jan1_time = time.strptime(year_str + " Jan 01", "%Y %b %d")
	jan1_sec = time.mktime(jan1_time)
	jan1_ms = int(round(jan1_sec * 1000))

	print "TEST! TIME WAS RUN! JAN1MS WAS CALULATED TO BE {} ms!".format(jan1_ms)

	test = int(round(time.time() * 1000)) - jan1_ms
	print "THAT WOULD MAKE THE CURRENT TIMING {} ms!".format(test)
	return jan1_ms

_jan1Ms = _calc_jan1ms()


def current_time_sec():
	return time.time()

def current_time_ms():
	return int(round(time.time() * 1000))

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
