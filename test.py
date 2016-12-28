# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

import f

if not f.AS_FUNC:
    f = f.f


test_cases = (
    ('', None, ''),
    ('', {'a': 5}, ''),
    ('a', None, 'a'),
    ('a', {'a': 5}, 'a'),
    ('#{a}', None, '2'),
    ('#{a}', {'a': 5}, '5'),
    ('#{a + b}', None, '5'),
    ('#{a + b}', {'a': 5, 'b': 3}, '8'),
    ('#{c}', None, 'hello'),
    ('#{c}', {'c': 'hello2'}, 'hello2'),
    ('#{c + "world"}', None, 'helloworld'),
    ('#{c + d}', None, 'helloworld'),
    ('#{c + " " + d}', None, 'hello world'),
    ('#{c + " " + d}', {'c': 'hello', 'd': '22'}, 'hello 22'),
    ('#{c + " " + "world"}', None, 'hello world'),
    ('北京', {'h': '北京'}, '北京'),
    ('#{h}', {'h': '北京'}, '北京'),
)


@pytest.mark.parametrize('tpl, namespace, output', test_cases)
def test_f(tpl, namespace, output):
    a = 2          # noqa
    b = 3          # noqa
    c = 'hello'    # noqa
    d = 'world'    # noqa
    assert f(tpl, namespace=namespace) == output
