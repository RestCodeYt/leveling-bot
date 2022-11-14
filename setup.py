from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name = 'leveling-bot',
    version = '0.1',
    description = 'A Discord leveling bot in Python.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'RestCode#6208',
    python_requires = '>=3.8.0',
    url = 'https://github.com/RestCodeYt/leveling-bot',
    install_requires = ['discord'],
    license = 'MIT'
)
