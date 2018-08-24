import random
import words


def silly_string(nouns, verbs, templates):
    # Your code should choose a random
    # sentence template from the templates
    # list.
    #
    # Then it should create a string based on
    # that template, but with random nouns
    # and verbs in place of the {{noun}} and
    # {{verb}} markers in it.
    #
    # Then it should return the resulting
    # string instead of this one:

    template = random.choice(templates)
    index = 0
    output = []
    while index < len(template):
        if template[index: index + 8] == "{{noun}}":
            output.append(random.choice(nouns))
            index += 8
        elif(template[index: index + 8] == "{{verb}}"):
            output.append(random.choice(verbs))
            index += 8
        else:
            output.append(template[index])
            index += 1
    return "".join(output)


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
                       words.templates))
