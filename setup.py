import os
import setuptools

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name='Parse',
    version='0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='Simple parser of search engines',
    # long_description=README,
    url='https://github.com/xaldey/dz00',
    author='xaldey',
    author_email='xaldey@mail.ru',
    keywords=['requests', 'BeautifulSoup', 'csv'],
    classifiers=[],
)