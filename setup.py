from distutils.core import setup

from os import path

from .utilsx import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='utilsx',
    packages=['utilsx'],
    version=__version__,
    license='MIT',
    description='The public Xiler python utility library.',
    long_description=long_description,
    author='Xiler Network - Arthurdw',
    author_email='mail.arthurdw@gmail.com',
    url='https://github.com/XilerNet/UtilsX',
    download_url='https://github.com/XilerNet/UtilsX/archive/v0.0.0.tar.gz',
    keywords=["Xiler", "utils"],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
