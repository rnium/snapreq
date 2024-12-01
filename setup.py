# setup.py
from setuptools import setup, find_packages

setup(
    name='snapreq',
    version='1.0.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        "rich>=13.9",
        "requests>=2.32",
    ],
    entry_points={
        'console_scripts': [
            'snap=snapreq.cli:main',
        ],
    },
    author='Md. Saiful Islam Roni',
    description='A sample CLI based API client',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/rnium/snapreq",
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
