from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

setup(
    name="govoucher",
    version="0.0.1",
    author="Yew Wee",
    author_email="ychua@thoughtworks.com",
    description=("A trial of using docopt and understanding python project"
                 "structure"),
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'console_scripts': [
            'govoucher = govoucher.cli:main',
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
)
