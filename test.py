# -*- coding: utf-8 -*-
import pytest

import f


test_cases = (
    ('', None, ''),
    ('', {'a': 5}, ''),
    ('a', None, 'a'),
    ('a', {'a': 5}, 'a'),
    ('#{a}', None, '2'),
    ('hello #{a}', None, 'hello 2'),
    ('#{a} hello', None, '2 hello'),
    ('hello #{a} world', None, 'hello 2 world'),
    ('#{a}', {'a': 5}, '5'),
    ('#{a + b}', None, '5'),
    ('#{a * b}', None, '6'),
    ('hello #{a + b} #{c} aa #{d}', None, 'hello 5 hello aa world'),
    ('#{a + b}', {'a': 5, 'b': 3}, '8'),
    ('#{c}', None, 'hello'),
    ('#{c}', {'c': 'hello2'}, 'hello2'),
    ('#{c + "world"}', None, 'helloworld'),
    ('#{c * 2}', None, 'hellohello'),
    ('#{c + d}', None, 'helloworld'),
    ('#{c + " " + d}', None, 'hello world'),
    ('#{c + " " + d}', {'c': 'hello', 'd': '22'}, 'hello 22'),
    ('#{c + " " + "world"}', None, 'hello world'),
    ('北京', {'h': '北京'}, f.to_str('北京')),
    ('#{h}', {'h': '北京'}, f.to_str('北京')),
    ('北京', {'h': '北京'}, f.to_str('北京')),
    ('#{h}', {'h': '北京'}, f.to_str('北京')),
)


@pytest.mark.parametrize('tpl, namespace, output', test_cases)
def test_f(tpl, namespace, output):
    a = 2          # noqa
    b = 3          # noqa
    c = 'hello'    # noqa
    d = 'world'    # noqa
    assert f(tpl, namespace=namespace) == output
