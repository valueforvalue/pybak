try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple utility script to backup one or many directories.',
    'author': 'Jeremy Morris',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'valueforvalue76@gmail.com',
    'version': '0.1',
    'install_requires': ['nose','pyyaml'],
    'packages': ['pybak'],
	'license': 'MIT'
    'scripts': [],
    'name': 'pybak'
}

setup(**config)