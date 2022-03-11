#!/usr/bin/env python
# @Author: SashaChernykh
# @Editor: fish2000
# @Date: 2018-06-04 08:01:23
# @Last Modified time: 2019-03-11 14:39:28 +0500
""" Pygments CSV Lexer csvlexer/csv.py
    
    * http://pygments.org/docs/lexerdevelopment/
    * https://github.com/FSund/pygments-custom-cpplexer
"""
from __future__ import print_function

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Keyword, Literal, Name, Operator, Punctuation

class CsvLexer(RegexLexer):
    
    """ Simple CSV lexer for Pygments.
        
        Extends:
            pygments.lexer.RegexLexer
        
        Class Variables:
            name {str} -- name of lexer:
                * http://pygments.org/docs/api/#pygments.lexer.Lexer.name
            aliases {list} – languages, against whose GFM block names CsvLexer will apply
                * https://git.io/fhjla
            filenames {list} – file name patterns, for whose contents CsvLexer will apply
            tokens {dict} – regular expressions internally matching CsvLexer’s components
        
        Based on StackOverflow user Adobe’s code:
            * https://stackoverflow.com/a/25508711/298171
    """
    
    name =       'Csv'
    aliases =   ['csv', 'comma-separated', 'comma-separated-values']
    filenames = ['*.csv']
    
    csv_variable = r'(,)([^,\n]*)'

    tokens = {
        'root': [
            (r'^[^,\n]*',       Operator,                                       'second'),
        ],
        'second': [
            (csv_variable,      bygroups(Punctuation, Name.Constant),           'third'),
        ],
        'third': [
            (csv_variable,      bygroups(Punctuation, Keyword.Declaration),     'fourth'),
        ],
        'fourth': [
            (csv_variable,      bygroups(Punctuation, Literal.Number),          'fifth'),
        ],
        'fifth': [
            (csv_variable,      bygroups(Punctuation, Literal.String.Single),   'sixth'),
        ],
        'sixth': [
            (csv_variable,      bygroups(Punctuation, Name.Constant),           'seventh'),
        ],
        'seventh': [
            (csv_variable,      bygroups(Punctuation, Keyword.Namespace),       'eighth'),
        ],
        'eighth': [
            (csv_variable,      bygroups(Punctuation, Literal.Number),          'ninth'),
        ],
        'ninth': [
            (csv_variable,      bygroups(Punctuation, Literal.String.Single),   'tenth'),
        ],
        'tenth': [
            (csv_variable,      bygroups(Punctuation, Keyword.Type),            'unsupported'),
        ],
        'unsupported': [
            (r'(.+)',           bygroups(Punctuation)),
        ],
    }

sample_csv_material = """
trailer,125
header,125,11,session start,0,Wed Mar  6 11:04:43 2019, + 414 msec
argument,1,0x0,sflags
argument,2,0x0,am_success
argument,3,0x0,am_failure
subject,-1,root,wheel,root,wheel,0,100339,0,0.0.0.0
return,success,0
trailer,125
header,125,11,session start,0,Wed Mar  6 18:23:18 2019, + 301 msec
argument,1,0x0,sflags
argument,2,0x0,am_success
argument,3,0x0,am_failure
subject,-1,root,wheel,root,wheel,0,100340,0,0.0.0.0
return,success,0
trailer,125
header,153,11,user authentication,0,Wed Mar  6 18:24:36 2019, + 169 msec
subject,-1,root,wheel,root,wheel,290,100000,0,0.0.0.0
text,Touch ID authentication
return,success,0
"""

def test():
    from pygments.formatters import Terminal256Formatter
    from pygments import highlight
    
    print(highlight(sample_csv_material, CsvLexer(), Terminal256Formatter()))

if __name__ == '__main__':
    import os, sys
    if os.environ.get('TM_PYTHON'):
        print("Inline test won’t work in TextMate, aborting…", file=sys.stderr)
        sys.exit(1)
    test()
