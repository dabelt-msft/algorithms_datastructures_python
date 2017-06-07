def replace(string):
    temp = ""
    for i in range(0, len(string)):
        if string[i] == " ":
            temp = temp + "%20"
        else:
            temp = temp + string[i]
    return temp


print(replace("Cat in space"))
