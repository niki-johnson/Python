def first_non_repeating_letter(string):
    for l in string:
        if string.upper().count(l) < 2 and string.lower().count(l) < 2:
            return l
    return ''


print(first_non_repeating_letter('sTreSS'))
