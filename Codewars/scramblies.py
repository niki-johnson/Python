from collections import Counter


def scramble(s1, s2):

    for item in set(s2):
        if item not in s1:
            return False

    for l in set(s2):
        if s1.count(l) < s2.count(l):
            return False

    return True


def scramble2(s1, s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2) - Counter(s1)) == 0


def scramble2(s1, s2):
    return all(s1.count(x) >= s2.count(x) for x in set(s2))


print(scramble('katas', 'stakaa'))
