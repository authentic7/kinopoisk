# -*- encdoding: utf-8 -*-

unhtml_map = {
    '&quot;': '"', '&laquo;': '"', '&raquo;': '"', '&#34;': '"', '&#8220;': '"',
    '&#171;': '"', '&#187;': '"', '&#039;': '\'', '&#39;': '\'', '&amp;': '&',
    '&copy;': '(c)', '&bull;': '*', '&#151;': '-', '&#8211;': '-', '&#8212;': '-',
    '&#45;': '-', '&mdash;': '-', '&lt;': '<', '&gt;': '>', '&nbsp;': ' ', '&#160': ' ',
    '\n': '', '\r': '', '&#124;': '|', '&#033;': '!', '&#33;': '!', '&#58;': ':', '&#x3a;': ':',
    '&lsaquo;': '<', '&rsaquo;': '>'
}

headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/34.0.1847.132 Safari/537.36', 'Connection': 'close'}


def unhtml(input_string):
    """
    Заменяет HTML последовательности в строке на символы из таблицы ASCII для хранения
    в БД и читаемого отображения в толстом клиенте
    """
    return input_string.replace('&nbsp', '')
