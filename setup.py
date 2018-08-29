#!/usr/bin/env python

from pathlib import Path
from setuptools import setup, find_packages

with (Path(__file__).parent / 'README.md').open() as fp:
    long_description = fp.read()


setup(
    name='nexaas_id_django_example',
    version='1.0',
    author='Rodrigo Cacilhas',
    author_email='rodrigo.cacilhas@nexaas.com',
    description='Nexaas ID Django example',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Proprietary License',
    keywords='nexaas-id profile',
    url='https://github.com/myfreecomm/nexaas-id-django-example',
    packages=find_packages(),
    install_requires=[
        'django==2.0.0',
        'nexaas-id-client==1.0',
        'python-dotenv==0.9.1',
    ],
    dependency_links=[
        'git+https://github.com/myfreecomm/nexaas-id-client-python.git'
        '#egg=nexaas-id-client-1.0',
    ],
    tests_require=[
        'pycodestyle==2.4.0',
        'pylint==2.0.1',
        'vcrpy==1.13.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
)
