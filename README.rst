====
suji
====

suji is a converter library from Japanese number notation to numerical value, and from numerical notation to Japanese Kansuji notation.


To convert from Japanese number notation to numerical string or value:
------------------------------------------------------------

Japanese number notation can include Kansuji.
The string `１つの価格が二兆30万五千十7円になります。` will be converted to two integers, `1` and `2000000005017`.
And also, `打率は三割二部五厘です。`  will be a float `0.325`.


**value:**

The return value is a converted str.
If the input string has no number notation, `value` returns the input str.


**values:**

The return value is a list of result objects.
If the input string has no number notation, suji returns a empty list.
The result object has three keys: `val`, `beg`, and `end`:

:val: the numerical value of the number notation.
:beg: the start postion of the found number notation at the input string.
:end: the end postion of the found number notation.


To convert from numeric notation to Japanese Kanji notation:
------------------------------------------------------------

The string `二兆30万五千十7円になります。` will be converted to the Kansuji string, `二兆三十万五千十七`.
The boolean flag `one` is interpreted as whether to display the first character `一` or not.
The output of `suji.kansuji('1000万')` will be converted to `一千万` (as default),
and the output of `suji.kansuji('1000万', False)` will be converted to `千万`.
Note that suji does *not* support numerical notation after the decimal point.
If the inpust string is `32.01`, the output will `三十二`, not `三十二割一厘`.


**kansuji:**

The retun value is a covnerted str.
If the input string has no number notation, `kansuji` returns the input str.


**kansujis:**

The return value is a list of result objects.
If the input string has no number notation, `kansujis` returns a empty list.
The result object has three keys: `val`, `beg`, and `end`:

:val: the Kansuji notation string
:beg: the start postion of the found number notation at the input string.
:end: the end postion of the found number notation.


suji is a one-pass parser.
That is, suji parse a source text from the head to the end only once.
This library is pure Python code with no dependencies.


Installation:
-------------

    $ pip install suji


Usage:
------

.. code-block:: python

    >>> import suji

    >>> suji.value('１つの価格が二兆30万五千十7円になります。')
    1つの価格が2000000305017円になります。
    >>> suji.value('一千万です。')
    10000000です。
    >>> suji.value('こんにちは')
    こんにちは

    >>> suji.values('１つの価格が二兆30万五千十7円になります。')
    [{'val': 1, 'beg': 0, 'end': 1}, {'val': 2000000305017, 'beg': 6, 'end': 15}]
    >>> suji.values('打率は三割二分五厘です。')
    [{'val': 0.32500000000000007, 'beg': 3, 'end': 9}]
    >>> suji.values('こんにちは')
    []

    >>> suji.kansuji('価格は￥10,000,056です。')
    価格は￥一千万五十六です
    >>> suji.kansuji('価格は￥10,000,056です。', False)
    価格は￥千万五十六です
    >>> suji.kansuji('こんにちは')
    こんにちは

    >>> suji.kansujis('価格は￥10,000,056です。')
    [{'val': '一千万五十六', 'beg': 4, 'end': 14}]
    >>> suji.kansujis('価格は￥10,000,056です。', False)
    [{'val': '千万五十六', 'beg': 4, 'end': 14}]
    >>> suji.kansujis('こんにちは')
    []
