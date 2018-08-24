########################################################################
# Lesson 22: locating a substring
# Write a function to see if a string starts
# with a given substring.


def starts_with(string, target):
    # While this version is succinct and matches
    # one of the instructor versions, it fails
    # when the `target` is longer than the `string`
    return string[0: len(target)] == target


def starts_with_v1(long, short):
    # This is an alternate solution using a for loop
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True


def starts_with_v2(long, short):
    # This is yet another version using the slice feature
    length = len(short)
    beginning = long[0: length]
    if beginning == short:
        return True
    else:
        return False


def execute_lesson_22():
    print(starts_with("tinkerbell", "tin"))
    print(starts_with_v2("tin", "tinkerbell"))
    print(starts_with_v3("tin", "tinkerbell"))
    # Uncomment the next line to see an error
    # print(starts_with_v1("tin", "tinkerbell"))


def starts_with_v3(long, short):
    # This is the third version supplied by instructor that
    # matches my version
    return long[0:len(short)] == short

########################################################################

# Lesson 23: is it a substring?
# Write a function that identifies if a `target` is a
# substring of `string`


def is_substring(sub, word):
    for i in range(len(word)):
        if sub == word[i: i + len(sub)]:
            return True
    return False


def execute_lesson_23():
    print(is_substring("bad", "abracadabra"))
    print(is_substring("dab", "abracadabra"))
    print(is_substring("pony", "pony"))
    print(is_substring("", "balloon"))
    print(is_substring("balloon", ""))

########################################################################

# Lesson 24: count substrings
# Count how many times a substring occurs in the
# main string. Account for overlaps.


def count_substring(string, target, count_overlaps):
    count = 0
    index = 0
    while index < len(string):
        if(target == string[index: index + len(target)]):
            count += 1
            # Check if overlaps should be counted and
            # increment by one (count_overlaps == Frue)
            # or by the length of target (count_overlaps == False)
            if count_overlaps:
                index += 1
            else:
                index += len(target)
        else:
            index += 1

    return count


def execute_lesson_24():
    print(count_substring("love, love, love, all you need is love",
                          "love", False))
    print(count_substring("AAAA", "AA", False))
    print(count_substring("AAAA", "AA", True))

# def execute():

########################################################################

# Lesson 25: locating substrings
# Find the position of a substring in a string.
# Handle the case where the substring isn't found.
# Two variants: locate_first and locate_all


def locate_first(target, string):
    location = -1
    for index in range(len(string)):
        if target == string[index: index + len(target)]:
            location = index
            break
    return location


def locate_all(target, string):
    locations = []
    index = 0
    while index < len(string):
        next = locate_first(target, string[index:])
        if next > -1:
            # Because the `string` gets smaller as index
            # increases, the value for next isn't the
            # true index of the substring. Add `index`
            # to `next` to get the correct value.
            locations.append(next + index)
            index += next + 1
        else:
            break
    return locations


def execute_lesson_25():
    print(locate_first("ook", "cookbook"))
    print(locate_first("base", "all your bass are belong to us"))

    print(locate_all("ook", "cookbook"))
    print(locate_all("yes", "yesyesyes"))
    print(locate_all("barb", "the upside down"))


execute_lesson_22()
execute_lesson_23()
execute_lesson_24()
execute_lesson_25()
