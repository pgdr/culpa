from setuptools import setup

setup(
    name='culpa',
    packages=['culpa'],
    version='0.0.2',
    install_requires=['pandas', 'xlrd'],
    entry_points={
        'console_scripts': ['culpa=culpa:main']
        }
    )
