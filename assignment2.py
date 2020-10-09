def get_count(input_str):
    num_vowels = 0
    # your code here
    for i in input_str:
        if i in ["a", "e", "i", "o", "u" ]:
            num_vowels=num_vowels + 1
        else:
            continue
    print(num_vowels)

get_count("abracadabra")

def high_and_low(numbers):
    numlist = numbers.split(" ")
    i = 0
    highest = int(numlist[0])
    lowest = int(numlist[0])
    while i < len(numlist):
        numlist[i] = int(numlist[i])
        if numlist[i] > highest:
            highest = numlist[i]
        if numlist[i] < lowest:
            lowest = numlist[i]
        i += 1
    highest = str(highest)
    lowest = str(lowest)
    return  highest+" "+lowest



