import fileinput

def reduce(text):
    reduced = ""
    prev = text[0]
    count = 1
    same = False
    for i in range(1, len(text)):
        if i == len(text) - 1:
            if prev == text[i]:
                count += 1
                if count % 2 != 0:
                    reduced += text[i]
            elif same == True:
                if count % 2 != 0:
                    reduced += prev
                reduced += text[i]

        if text[i] != prev:
            if same == True:
                if count % 2 != 0:
                    reduced += prev
                same = False
                count = 1
            else:
                reduced += prev

        elif text[i] == prev:
            count += 1
            same = True
        prev = text[i]
    return "Empty String" if len(reduced) == 0 else reduced

for line in fileinput.input():
    pass

print(reduce(line))