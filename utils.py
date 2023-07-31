def median(data):
    n = len(data)
    data.sort()
    if n % 2 == 0:
        return (data[n//2] + data[n//2 + 1])/2
    else:
        return data[n//2]

def mean(data):
    return sum(data)/len(data)