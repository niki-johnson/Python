import datetime


def format_duration(seconds):

    if seconds < 60:
        if seconds > 1:
            return f'{seconds} seconds'
        elif seconds == 0:
            return ''
        return f'{seconds} second'

    elif seconds < 3600:
        min = seconds % 3600/60
        sec = seconds % 3600 % 60
        if int(min) > 1:
            return f'{int(min)} minutes and {format_duration(int(sec))}'
        elif int(min) == 1:
            return f'{int(min)} minutes'
        else:
            return f'{int(min)} minute and {format_duration(int(sec))}'

    elif seconds < 3600*24:

        horas = seconds//3600
        sec = seconds % 3600
        if int(horas) > 1:
            return f'{int(horas)} hours, {format_duration(int(sec))}'
        elif int(horas) == 1:
            return f'{int(horas)} hour'
        else:
            return f'{int(horas)} hour, {format_duration(int(sec))}'

    elif seconds < 3600*24*365:

        dias = seconds//(3600*24)
        sec = seconds % (3600*24)
        if int(dias) > 1:
            return f'{int(dias)} days, {format_duration(int(sec))}'
        elif int(dias) == 1:
            return f'{int(dias)} day'
        else:
            return f'{int(dias)} day, {format_duration(int(sec))}'

    else:
        anos = seconds // (3600*24*365)
        sec = seconds % (3600*24*365)
        print(sec)
        if int(anos) > 1:
            return f'{int(anos)} years, {format_duration(int(sec))}'
        elif int(anos) == 1:
            return f'{int(anos)} year'
        else:
            return f'{int(anos)} year, {format_duration(int(sec))}'


def make_readable2(s):
    return '{:02}{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


print(format_duration(3661))
