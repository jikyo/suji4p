suji
-----

suji is a converter library from Japanese number notation to numerical value.
Japanese number notation can include Kansuji.
The string `１つの価格が二兆30万五千十7円になります。` will be converted to two integers, `1` and `2000000005017`.
And also, `打率は三割二部五厘です。`  will be a float `0.325`.
The return value is a list of result objects.
If the input string has no number notation, suji returns a empty list.
The result object has three keys: `val`, `beg`, and `end`:

:val: the numerical value of the number notation.
:beg: the start postion of the found number notation at the input string.
:end: the end postion of the found number notation.

suji is a one-pass parser.
That is, suji parse a source text from the head to the end only once.
This library is pure Python code with no dependencies.

Installation
-----

(in preparation)

.. code-block:: BashLexer

    $ git clone https://github.com/jikyo/suji4p.git
    $ cd suji4p
    $ pip install .


Usage
-----

.. code-block:: python

    >>> import suji
    >>> suji.values('１つの価格が二兆30万五千十7円になります。')
    [{'val': 1, 'beg': 0, 'end': 1}, {'val': 2000000305017, 'beg': 6, 'end': 15}]
    >>> suji.values('打率は三割二分五厘です。')
    [{'val': 0.32500000000000007, 'beg': 3, 'end': 9}]
    >>> suji.values('こんにちは')
    []

