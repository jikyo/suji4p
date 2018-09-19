suji
-----

suji is a converter library from Japanese number notation to numerical value.
Japanese number notation can include Kansuji.
The string `二兆30万五千十7` will be converted to an integer `2000000005017`.
And also, `三割二部五厘`  will be float `0.325`.
suji is a one-pass parser.
That is, suji parse a source text from the head to the end only once.
This library is pure Python code with no dependencies.

Installation
-----

.. code-block:: BashLexer

    $ git clone https://github.com/jikyo/suji4p.git
    $ cd suji4p
    $ pip install .


Usage
-----

.. code-block:: python

    >>> import suji
    >>> suji.converter.values('価格は二兆30万五千十7円になります。')
    [2000000305017]
    >>> suji.converter.values('こんにちは')
    []


.. code-block:: python

    >>> from suji import converter
    >>> converter.values('価格は二兆30万五千十7円になります。')
    [2000000305017]
    >>> converter.values('こんにちは')
    []
