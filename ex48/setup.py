try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex84',
    'author': 'rachid',
    'url': '',
    'download_url': '',
    'author_email': 'rachid.drid@gmail.com',
    'version': '0.1',
    'install_requires': 'nose'],
    'packages': ['ex48'],
    'script': [],
    'name': 'ex48'
    }

setup(**config)
