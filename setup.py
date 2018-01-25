#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-clever-selects',
    version='0.8.0',
    description='Chained select box widget for Django framework using AJAX requests.',
    long_description=open('README.rst').read(),
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/artscoop/django-clever-selects',
    packages=[
        'clever_selects',
        'clever_selects.templatetags'
    ],
    include_package_data=True,
    install_requires=(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Alpha'
    ],
    license='BSD License',
    keywords = "django clever chained selects",
)
