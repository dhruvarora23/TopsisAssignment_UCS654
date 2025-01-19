from setuptools import setup, find_packages

setup(
    name='Topsis-Dhruv-102203834',
    version='0.1.0',
    author='Dhruv Arora',
    author_email='dhruvarora2309@gmail.com',
    description='A Python package to implement the Topsis algorithm.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dhruvarora23/TOPSIS/',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
)
