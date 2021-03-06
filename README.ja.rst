====
suji
====

suji は日本語や数字で表記された数値表現の文字列を実際の数値へ変換するライブラリです。
また、数値表現を漢数字に変換することもできます。

日本語数値表現から数値への変換:
-------------------------

漢数字を数値変換できます。
文字列 `１つの価格が二兆30万五千十7円になります。` から値 `1` と `2000000005017` を抽出します。
また、 `打率は三割二分五厘です。` を値 `0.325` に抽出します。


**value:**

返却される値は文字列です。
入力文字列に数値表現がない場合、 `value` は入力文字列を返却します。


**values:**

返却される値は、結果オブジェクトのリストです。
入力文字列に数値表現がない場合、 `values` は空リストを返却します。
結果オブジェクトは3つキー、 `val` 、 `beg` 、 `end` をもちます。
3つのキーはそれぞれ次の意味をもちます:

:val: 数値表現の値
:beg: 入力文字列で見つかった数値表現の開始位置
:end: 入力文字列で見つかった数値表現の終了位置


日本語数値表現から漢数字への変換:
---------------------------

文字列 `二兆30万五千十7円になります。` は `二兆三十万五千十七` へ変換されます。
bool 値であるフラグ `one` は `一` を表示するか否かを指定します。
`suji.kansuji('1000万')` は `一千万` に変換されます (これはデフォルトです)。
`suji.kansuji('1000万', False)` は `千万` に変換されます。
小数点以下の表記には *対応していない* ことに注意してください。
その為、 `32.01` は `三十二` に変換され、 `三十二割一厘` ではありません。


**kansuji:**

返却される値は文字列です。
入力文字列に数値表現がない場合、 `kansuji` は入力文字列を返却します。


**kansujis:**

返却される値は、結果オブジェクトのリストです。
入力文字列に数値表現がない場合、 `kansujis` は空リストを返却します。
結果オブジェクトは3つキー、 `val` 、 `beg` 、 `end` をもちます。
3つのキーはそれぞれ次の意味をもちます:

:val: 漢数字文字列
:beg: 入力文字列で見つかった数値表現の開始位置
:end: 入力文字列で見つかった数値表現の終了位置


suji は one-pass パーサーです。
すなわち、入力テキストを先頭から末尾まで一度だけしか走査しません。
このライブラリは依存関係のない Python ネイティブのライブラリです。


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
