# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name             = 'auto-resizing-text-edit',
    version          = '0.1.0',
    description      = 'A Qt widget based on QTextEdit, that changes its height automatically to accommodate the text',
    author           = 'Kamil Śliwak',
    author_email     = 'cameel2/at/gmail/com',
    url              = 'https://github.com/cameel/auto-resizing-text-edit',
    packages         = find_packages(),
    license          = 'MIT',
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Text Editors'
    ]
)
