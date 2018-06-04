# @Author: SashaChernykh
# @Date: 2018-06-04 08:01:23
# @Last Modified time: 2018-06-04 11:54:56
"""pygments CSV csv_lexer.py.

http://pygments.org/docs/lexerdevelopment/
https://github.com/FSund/pygments-custom-cpplexer
"""
from pygments.lexer import RegexLexer
from pygments.lexer import bygroups
from pygments.token import *


class CsvLexer(RegexLexer):
    """Simply CSV lexer.

    Based on Adobe user code:
    https://stackoverflow.com/a/25508711/5951529

    Extends:
        RegexLexer

    Variables:
        name {str} -- name of lexer:
        http://pygments.org/docs/api/#pygments.lexer.Lexer.name
        aliases {list} -- language names, that I can use in GFM block:
        https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#code-highlighting
        filenames {list} -- extensions, in which I can use this lexer
        tokens {dict} -- regular expressions for lexer
    """

    name = 'Csv'
    aliases = ['csv']
    filenames = ['*.csv']

    tokens = {
        'root': [
            (r'^[^,\n]*', Operator, 'second'),
        ],
        'second': [
            (r'(,)([^,\n]*)', bygroups(Punctuation, Literal.Number), 'third'),
        ],
        'third': [
            (r'(,)([^,\n]*)', bygroups(Punctuation, Keyword), 'fourth'),
        ],
        'fourth': [
            (r'(,)([^,\n]*)', bygroups(Punctuation, Name.Constant), 'fifth'),
        ],
        'fifth': [
            (r'(,)([^,\n]*)', bygroups(Punctuation, Literal.String.Single), 'unsupported'),
        ],
        'unsupported': [
            (r'.+', Punctuation),
        ],
    }
