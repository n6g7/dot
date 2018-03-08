import crayons


class ColouredString(object):
    def __init__(self, string):
        self.string = string

    def __format__(self, format):
        if format == '':
            return self.string
        return str(getattr(crayons, format)(self.string))


def print_line(message, *args, level=0, **kwargs):
    args = [ColouredString(arg) for arg in args]
    kwargs = {
        key: ColouredString(kwargs[key])
        for key in kwargs
    }

    print('{indent}{message}'.format(
        indent='   ' * level,
        message=message.format(*args, **kwargs)
    ))
