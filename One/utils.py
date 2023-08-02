def median(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 0:
        m1 = sorted_data[n//2-1]
        m2 = sorted_data[n//2]
        return (m1 + m2)/2
    else:
        return sorted_data[n//2]

def mean(data):
    return sum(data)/len(data)

def trimmed_mean(data, trim_perc):
    trimmed_data = []
    trim = int(len(data) * trim_perc/100)
    for i in range(trim, len(data)-trim):
        trimmed_data.append(data[i])
    return mean(trimmed_data)