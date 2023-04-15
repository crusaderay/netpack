from setuptools import setup, find_packages

setup(
    name='netpack',
    version='0.0.1',
    description='A Python package for performing network-related tasks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dongjie Zhang',
    author_email='crusade.ray@gmail.com',
    url='https://github.com/yourusername/netpack',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
