f
=============================

|Build| |Coverage|

.. \|Pypi version\|

Ruby-Style String Interpolation for Python.


* GitHub: https://github.com/mozillazg/f
* License: MIT license
* Python version: 2.6, 2.7, pypy, pypy3, 3.3, 3.4, 3.5, 3.6

.. \PyPI: https://pypi.python.org/pypi/f


Usage
--------

.. code-block:: python

    >>> import f
    >>> a = 2
    >>> b = 3
    >>> f('#{a}')
    '2'
    >>> f('#{a + b}')
    '5'


.. |Build| image:: https://img.shields.io/travis/mozillazg/f/master.svg
   :target: https://travis-ci.org/mozillazg/f
.. |Coverage| image:: https://img.shields.io/coveralls/mozillazg/f/master.svg
   :target: https://coveralls.io/r/mozillazg/f
.. .. |PyPI version| image:: https://img.shields.io/pypi/v/f.svg
..    :target: https://pypi.python.org/pypi/f
