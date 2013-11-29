#!/usr/bin/env python

from setuptools import setup, find_packages

tests_require = [
    'django',
]

setup(
    name='django-modelnotice',
    version=".".join(map(str, __import__('modelnotice').__version__)),
    author='anscii',
    author_email='nt.aknt@gmail.com',
    description="Generic users' Model notices in Django",
    url='http://github.com/anscii/django-modelnotice',
    install_requires=[
        'django',
    ],
    #tests_require=tests_require,
    #extras_require={'test': tests_require},
    #test_suite='modelnotice.runtests.runtests',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)