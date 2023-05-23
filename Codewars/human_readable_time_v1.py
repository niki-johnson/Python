def make_readable(seconds):
    horas = seconds//3600 if seconds//3600 < 99 else 99
    min = seconds % 3600/60 if seconds % 3600/60 < 59 else 59
    sec = seconds % 3600 % 60 if seconds % 3600 % 60 < 59 else 59
    return f'{horas:02}:{int(min):02}:{int(sec):02}'


def make_readable2(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


print(make_readable(0))
