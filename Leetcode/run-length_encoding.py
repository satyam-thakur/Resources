def runlength_encoding(string):
    if not string:
        return ""

    encoded_string = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            encoded_string.append(f"{string[i - 1]}{count}")
            count = 1

    encoded_string.append(f"{string[-1]}{count}")

    return "".join(encoded_string)

runlength_encoding("aabcccccaaa")
