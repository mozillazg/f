# -*- coding: utf-8 -*-
import re
import sys

__title__ = 'f'
__version__ = '0.0.1'
__author__ = 'mozillazg'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2016 mozillazg'

re_code = re.compile(r'#\{([^\}]+)\}')


def get_chucks(text):
    matchs = list(re_code.finditer(text))
    if matchs:
        p = 0
        for match in matchs:
            yield text[p:match.start()], match.group(1)
            p = match.end() + 1
    else:
        yield text, ''


def f(template_str, namespace=None):
    if namespace is None:
        namespace = sys._getframe(1).f_locals

    str_list = []
    for string, code in get_chucks(template_str):
        str_list.append(string)
        if code:
            str_list.append(str(eval(code, namespace, namespace)))

    return ''.join(str_list)

sys.modules['f'] = f

f.__title__ = __title__
f.__version__ = __version__
f.__author__ = __author__
f.__license__ = __license__
f.__copyright__ = __copyright__
f.__file__ = __file__
