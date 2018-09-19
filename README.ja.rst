suji
-----

suji は日本語で表記された数値表現を実際の数値に変換するライブラリです。
漢数字にも対応しています。
文字列 `二兆30万五千十7` を値 `2000000005017` に変換します。
また、 `三割二部五厘` を値 `0.325` に変換します。
suji は one-pass パーサーです。
すなわち、入力テキストを先頭から末尾まで一度だけしか走査しません。
このライブラリは依存関係のない Python ネイティブのライブラリです。

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
