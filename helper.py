import genius


string_helper = genius.tools.StringHelper()


def transform_seg_words(words):
    s_t = '%s\t%s\t%s'
    result = []
    for word in words:
        word = string_helper.fullwidth_to_halfwidth(word.strip())
        marker = string_helper.mark_text(word)
        length = len(word)
        if marker in ('ALPHA', 'DIGIT', 'PUNC') or length == 1:
            result.append('%s\t%s\t%s' % (word, marker, 'S'))
        elif length == 2:  # B E
            s1 = s_t % (word[0], marker, 'B')
            s2 = s_t % (word[1], marker, 'E')
            result.append(s1)
            result.append(s2)
        elif length == 3:  # B B1 E
            s1 = s_t % (word[0], marker, 'B')
            s2 = s_t % (word[1], marker, 'B1')
            s3 = s_t % (word[2], marker, 'E')
            result.append(s1)
            result.append(s2)
            result.append(s3)
        elif length == 4:  # B B1 B2 E
            s1 = s_t % (word[0], marker, 'B')
            s2 = s_t % (word[1], marker, 'B1')
            s3 = s_t % (word[2], marker, 'B2')
            s4 = s_t % (word[3], marker, 'E')
            result.append(s1)
            result.append(s2)
            result.append(s3)
            result.append(s4)
        else:
            for index, char in enumerate(word):
                if index == 1:  # B
                    s = s_t % (char, marker, 'B')
                elif index == 2:  # B1
                    s = s_t % (char, marker, 'B1')
                elif index == 3:  # B2
                    s = s_t % (char, marker, 'B2')
                elif index == length - 1:  # E
                    s = s_t % (char, marker, 'E')
                else:  # M
                    s = s_t % (char, marker, 'M')
                result.append(s)
    return result


def transform_pos_words(words):
    result = []
    for word in words:
        word = word.strip()
        word, tagging = word.split('/')
        s = '%s\t%s\t%s' % (word, string_helper.mark_text(word), tagging)
        result.append(s)
    return result
