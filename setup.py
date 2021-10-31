from setuptools import setup

setup(
    name='algotester',
    version='0.1.0',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'algotester = algotester:cli',
        ],
    },
)
