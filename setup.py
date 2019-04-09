from setuptools import setup

def _reqs():
    reqs = []
    with open('requirements.txt', 'r') as f:
        reqs = [pkg.strip() for pkg in f.readlines()]
    return reqs

setup(
    name='culpa',
    packages=['culpa'],
    version='0.0.3',
    install_requires=_reqs(),
    entry_points={
        'console_scripts': ['culpa=culpa:main']
        },
    test_suite='tests',
    )
