import os
from setuptools import setup

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='request-parser',
    version='0.1',
    packages=['parser'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='Simple parser of search engines',
    # long_description=README,
    url='https://github.com/xaldey/dz00',
    author='xaldey',
    author_email='xaldey@mail.ru',
    keywords = ['json', 'requests', 'BeautifulSoup', 'csv'],
    classifiers = [],
)