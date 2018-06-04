"""Install custom csv lexer.

Instructions

http://www.iamjonas.me/2013/03/custom-syntax-in-pygments.html
https://stackoverflow.com/a/39540683/5951529
"""
from setuptools import find_packages
from setuptools import setup

setup(
    name='csvlexer',
    version='0.1.0',
    packages=find_packages(),
    entry_points="""
  [pygments.lexers]
  csvlexer = csvlexer.csv:CsvLexer
  """,
)
