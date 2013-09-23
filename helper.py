import genius
from genius.word import Word


string_helper = genius.tools.StringHelper()

group_marker = genius.process.BaseSegmentProcess()


def transform_seg_words(words):
    s_t = '%s\t%s\t%s'
    result = []
    for terms in words:
        text = string_helper.fullwidth_to_halfwidth(terms.strip())
        terms = group_marker.process(Word(text))
        length = len(terms)
        if length == 1:
            result.append('%s\t%s\t%s' % (terms[0].text, terms[0].marker, 'S'))
        elif length == 2:  # B E
            s1 = s_t % (terms[0].text, terms[0].marker, 'B')
            s2 = s_t % (terms[1].text, terms[1].marker, 'E')
            result.append(s1)
            result.append(s2)
        elif length == 3:  # B B1 E
            s1 = s_t % (terms[0].text, terms[0].marker, 'B')
            s2 = s_t % (terms[1].text, terms[1].marker, 'B1')
            s3 = s_t % (terms[2].text, terms[2].marker, 'E')
            result.append(s1)
            result.append(s2)
            result.append(s3)
        elif length == 4:  # B B1 B2 E
            s1 = s_t % (terms[0].text, terms[0].marker, 'B')
            s2 = s_t % (terms[1].text, terms[1].marker, 'B1')
            s3 = s_t % (terms[2].text, terms[2].marker, 'B2')
            s4 = s_t % (terms[3].text, terms[3].marker, 'E')
            result.append(s1)
            result.append(s2)
            result.append(s3)
            result.append(s4)
        else:
            for index, term in enumerate(terms):
                if index == 0:  # B
                    s = s_t % (term.text, term.marker, 'B')
                elif index == 1:  # B1
                    s = s_t % (term.text, term.marker, 'B1')
                elif index == 2:  # B2
                    s = s_t % (term.text, term.marker, 'B2')
                elif index == length - 1:  # E
                    s = s_t % (term.text, term.marker, 'E')
                else:  # M
                    s = s_t % (term.text, term.marker, 'M')
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
