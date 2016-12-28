# -*- coding: utf-8 -*-
import re
import sys

__title__ = 'f'
__version__ = '0.0.1'
__author__ = 'mozillazg'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2016 mozillazg'

re_code = re.compile(r'#\{([^\}]+)\}')

PY3 = (sys.version_info[0] == 3)
AS_FUNC = (sys.version_info >= (3, 4))
if not PY3:
    bytes = str
    str = unicode     # noqa


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
            gened_str = eval(code, namespace, namespace)
            str_list.append(gened_str)

    return ''.join(map(to_str, str_list))


def to_str(obj):
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, bytes):
        return str(obj, 'utf-8')
    else:
        return str(obj)


f.__title__ = __title__
f.__version__ = __version__
f.__author__ = __author__
f.__license__ = __license__
f.__copyright__ = __copyright__
f.__file__ = __file__
f.PY3 = PY3
f.AS_FUNC = AS_FUNC
f.to_str = to_str
f.f = f

if AS_FUNC:
    sys.modules['f'] = f
