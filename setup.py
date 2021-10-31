from setuptools import setup

setup(
    name='algotester',
    version='0.1.0',
    #py_modules=['yourscript'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'algotester = test:cli',
        ],
    },
)
