import statistics

data = [10, 20, 20, 30, 40, 40, 40, 50, 60]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev = statistics.stdev(data)
variance = statistics.variance(data)

print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", stdev)
print("Variance:", variance)
