import sys
fileName, timeA, timeB, timeC, timeD = sys.argv
times = list(map(int, [timeA, timeB, timeC, timeD]))

sortedTimes = sorted(times, reverse=ture)
print(sortedTimes)

for time in enumerate(sortedTimes):
    aiueo
