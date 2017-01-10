# -*- coding: utf-8 -*-
import re
import sys

__title__ = 'f'
__version__ = '0.1.0'
__author__ = 'mozillazg'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2016 mozillazg'


class F(object):
    def __init__(self):
        self.__title__ = __title__
        self.__version__ = __version__
        self.__author__ = __author__
        self.__license__ = __license__
        self.__copyright__ = __copyright__
        self.__name__ = 'f'
        self.__file__ = __file__
        self.__package__ = __package__
        # self.__loader__ = __loader__
        PY3 = (sys.version_info[0] == 3)
        if PY3:
            self.text_bytes = bytes
            self.text_str = str
        else:
            self.text_bytes = str
            self.text_str = unicode     # noqa
        self.re_code = re.compile(r'#\{([^\}]+)\}')
        self.sys = sys
        self.eval = eval
        self.map = map

    def __call__(self, template_str, namespace=None):
        if namespace is None:
            namespace = self.sys._getframe(1).f_locals

        str_list = []
        for string, code in self.get_chucks(template_str):
            str_list.append(string)

            if code:
                gened_str = self.eval(code, namespace, namespace)
                str_list.append(gened_str)

        return ''.join(self.map(self.to_str, str_list))

    def to_str(self, obj):
        if isinstance(obj, self.text_str):
            return obj
        elif isinstance(obj, self.text_bytes):
            return self.text_str(obj, 'utf-8')
        else:
            return self.text_str(obj)

    def get_chucks(self, text):
        matchs = self.re_code.finditer(text)
        pos = 0
        for match in matchs:
            yield text[pos:match.start()], match.group(1)
            pos = match.end()
        yield text[pos:], ''


sys.modules['f'] = F()
