from setuptools import setup, find_packages
import sys
import os

# Get the path of the 'src' directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))

# Add 'src' directory to the sys.path
sys.path.append(src_path)

# Add the path of the 'src' directory to the PYTHONPATH
PYTHONPATH = os.environ.get('PYTHONPATH', '')

# Define the name of your library
name = 'ctda'

# Define the version of your library
version = '0.0.1'

# Define the author and contact email
author = 'Lorenzo Liuzzo'
email = 'lorenzoliuzzo@outlook.com'

# Define a short description of your library
description = ''

# Read the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()

# Define the dependencies, if any
dependencies = [
    # Add any external dependencies here
    # numpy
]

setup(

    name=name,
    version=version,
    author=author,
    author_email=email,

    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lorenzoliuzzo/ctda/',
    
    license='MIT',
    packages=find_packages(where='src/'),
    package_dir={'': 'src/'},

    include_package_data=True,
    install_requires=dependencies,

    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    
    classifiers=[
        # Full list of Trove classifiers available at:
    ],

    keywords=[
        # Add keywords that define your project
    ]

)