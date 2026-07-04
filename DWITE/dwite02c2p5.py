import re
from collections import Counter
for i in range(5):
    text = input().upper();
    text = re.sub('[^A-Z]', '', text)
    freq =  Counter(text)
    freq = dict(sorted(freq.items()))
    freq_keys = list(freq.keys())
    freq_values = list(freq.values())
    for j in range(len(freq_keys) - 1):
        print(str(freq_keys[j]) + "-" + str(freq_values[j]) + ":", end = "")
    print(str(freq_keys[-1]) + "-" + str(freq_values[-1])) #This problem is to compute frequency and report them in alphabetical order.
