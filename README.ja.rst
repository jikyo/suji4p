suji
-----

suji は日本語や数字で表記された数値表現の文字列を実際の数値へ変換するライブラリです。
漢数字を数値変換できます。
文字列 `１つの価格が二兆30万五千十7円になります。` から値 `1` と `2000000005017` を抽出します。
また、 `打率は三割二分五厘です。` を値 `0.325` に抽出します。
返却される値は、結果オブジェクトのリストです。
入力文字列に数値表現がない場合、suji は空リストを返却します。
結果オブジェクトは3つキー、 `val` 、 `at` 、 `len` をもちます。
3つのキーはそれぞれ次の意味をもちます:

:val: 数値表現の値
:at:  入力文字列に見つかった数値表現の開始位置
:len: 入力文字列に見つかった数値表現の長さ

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
    >>> suji.converter.values('１つの価格が二兆30万五千十7円になります。')
    [{'val': 1, 'beg': 0, 'end': 1}, {'val': 2000000305017, 'beg': 6, 'end': 15}]
    >>> suji.converter.values('打率は三割二分五厘です。')
    [{'val': 0.32500000000000007, 'beg': 3, 'end': 9}]
    >>> suji.converter.values('こんにちは')
    []


.. code-block:: python

    >>> from suji import converter
    >>> converter.values('１つの価格が二兆30万五千十7円になります。')
    [{'val': 1, 'beg': 0, 'end': 1}, {'val': 2000000305017, 'beg': 6, 'end': 15}]
    >>> converter.values('打率は三割二分五厘です。')
    [{'val': 0.32500000000000007, 'beg': 3, 'end': 9}]
    >>> converter.values('こんにちは')
    []
