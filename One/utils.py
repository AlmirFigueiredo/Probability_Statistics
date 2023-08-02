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
    data_sorted = sorted(data)
    quantity_to_exclude = int(len(data)*trim_perc/100)
    trim_init = quantity_to_exclude
    trim_final = len(data)-quantity_to_exclude
    trimmed_data = data_sorted[trim_init : trim_final]
    return sum(trimmed_data)/len(trimmed_data)
