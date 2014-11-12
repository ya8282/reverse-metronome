import time
import math

def read_input(break_char='.'):
    tm = []
    while True:
        user_input = raw_input('[ input %s to exit ]' % break_char)
        if user_input == break_char:
            break
        tm.append(time.time())
    return tm

def calc_intervals(time_diffs, trim_start=True, is_bpm=False):
    intervals = []
    if len(time_diffs) < 2:
        raise Exception("Not enough data points to make an accurate measurement.\n")
    tdata = time_diffs[1:] if trim_start else time_diffs
    num_timings = len(tdata)
    for i in xrange(0, num_timings):
        if i < num_timings - 1:
            delta = tdata[i+1] - tdata[i]
            if is_bpm:
                intervals.append(60/delta if delta !=0 else 0)
            else:
                intervals.append(delta)    

    avg = sum(intervals) * 1.0 / num_timings if num_timings != 0 else 0.0
    stddev = math.sqrt(sum(map(lambda x: (x - avg)**2, intervals)) / num_timings if num_timings !=0 else 0.0)
    
    return avg, stddev 

if __name__ == "__main__":

    print "Press return on every beat when ready\n"
    tm = read_input()

    avg_sec, stddev_sec = calc_intervals(tm)
    avg_bpm, stddev_bpm = calc_intervals(tm, is_bpm=True)
       
    print "Average Seconds: %.1f\nAverage BPM: %.1f\nStd. Dev. Seconds: %.2f\nStd. Dev. BPM: %.2f\n" % (avg_sec, avg_bpm, stddev_sec, stddev_bpm)
 
