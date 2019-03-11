""" Install custom csv lexer
    
    Instructions:
    
    * http://www.iamjonas.me/2013/03/custom-syntax-in-pygments.html
    * https://stackoverflow.com/a/39540683/298171
"""
import sys, os
from setuptools import find_packages, setup

# HOST PYTHON VERSION
PYTHON_VERSION = float("%s%s%s" % (sys.version_info.major, os.extsep,
                                   sys.version_info.minor))

# CONSTANTS
PROJECT_NAME = 'pygments-csv-lexer'
AUTHOR_NAME = 'Alexander Böhn'
AUTHOR_USER = 'fish2000'

GITHUB = 'github.com'
GMAIL = 'gmail.com'

AUTHOR_EMAIL = '%s@%s' % (AUTHOR_USER, GMAIL)
PROJECT_GH_URL = 'https://%s/%s/%s' % (GITHUB,
                                       AUTHOR_USER,
                                       PROJECT_NAME)
PROJECT_DL_URL = '%s/zipball/master' % PROJECT_GH_URL

KEYWORDS = ('pygmemts',
            'tabular data', PROJECT_NAME,
                            AUTHOR_USER,
            'tables',
            'comma-separated values',
            'syntax highlighting',
            'syntax coloring', 'csv',
            'lexer', 'regex', 'regular expressions')

# PROJECT DIRECTORY
CWD = os.path.dirname(__file__)
BASE_PATH = os.path.join(
            os.path.abspath(CWD), PROJECT_NAME)

def project_content(filename):
    import io
    filepath = os.path.join(CWD, filename)
    if not os.path.isfile(filepath):
        raise IOError("""File %s doesn't exist""" % filepath)
    out = ''
    with io.open(filepath, 'r') as handle:
        out += handle.read()
    if not out:
        raise ValueError("""File %s couldn't be read""" % filename)
    return out

# PROJECT VERSION & METADATA
__version__ = "<undefined>"
try:
    exec(compile(
        open(os.path.join(BASE_PATH,
            '__version__.py')).read(),
            '__version__.py', 'exec'))
except:
    __version__ = '0.1.2'

# PROJECT DESCRIPTION
LONG_DESCRIPTION = project_content('README.md')

# SOFTWARE LICENSE
LICENSE = 'MIT'

# REQUIRED INSTALLATION DEPENDENCIES
INSTALL_REQUIRES = [
    'Pygments>=2.1.0']

# PYPI PROJECT CLASSIFIERS
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: OS Independent',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7']

setup(
    name=PROJECT_NAME,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    
    version=__version__,
    description=__doc__,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    
    keywords=" ".join(KEYWORDS),
    url=PROJECT_GH_URL, download_url=PROJECT_DL_URL,
    license=LICENSE, platforms=['any'],
    classifiers=CLASSIFIERS,
    
    packages=find_packages(),
    package_data={ '' : ['*.*'] },
    include_package_data=True,
    zip_safe=True,
    
    install_requires=INSTALL_REQUIRES,
    entry_points="""
    [pygments.lexers]
    csv = csvlexer.csv:CsvLexer
""")
