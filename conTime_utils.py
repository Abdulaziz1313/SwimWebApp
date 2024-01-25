import hfpy_utils
import statistics




def perform_conversions(times):
    converts = []
    for t in times:
        if ":" in t:
            minutes, rest = t.split(":")
            seconds, hundredths = rest.split(".")
        else:
            minutes = 0
            seconds, hundredths = t.split(".")
        converts.append(int(minutes) * 60 * 100 + int(seconds) * 100 + int(hundredths))
    average = statistics.mean(converts)
    mins_secs, hundredths = f"{(average / 100):.2f}".split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    average = f"{minutes}:{seconds:0>2}.{hundredths}"
    converts.reverse()
    times.reverse()
    from_max = max(converts)
    scaled = [hfpy_utils.convert2range(n, 0, from_max, 0, 350) for n in converts]
    return average, times, scaled 
