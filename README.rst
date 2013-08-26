=======================
Auto-resizing text edit
=======================

AutoResizingTextEdit is a simple Qt widget based on QTextEdit. Its purpose is to automatically adjust editor height to match the text, with the help of a layout it's placed in.

It works with both Python 2 and Python 3 as well as PyQt 4 and PyQt 5 [2]_

Status
======

The project has not undergone extensive testing on multiple platorms yet and should be considered alpha-quality. It's already feature-complete though and, due to its simplicity and emphasis on working with Qt widget system rather than subverting it, should be safe for general use.

The code has only been tested on Arch Linux so far.

Installation
============

setup.py
--------

The repository contains standard setup.py script (using setuptools). To install run:

.. code-block:: bash

    python setup.py install --root=/your/python/site-packages/path --optimize=1

For a complete command reference see `setuptools documentation`_.

PyPI
----

If you're using pip you can install the package from PyPI repository: `auto-resizing-text-edit on PyPI`_

.. code-block:: bash

    pip install auto-resizing-text-edit
    

You can install the PyQt 4 versions that way as well:

.. code-block:: bash

   pip install git+https://github.com/cameel/auto-resizing-text-edit.git@pyqt4-v0.1.0

AUR
---

If you're using Arch Linux you can get a PKGBUILD from AUR: `python-auto-resizing-text-edit in AUR`_

Dependencies
============

- Python >= 2.7
- PyQt 5 or PyQt 4 [1]_ [2]_

.. [1] Note that PyQt is not listed explicitly in setup.py. That's because it can't be easily installed from PyPI and setup.py/pip fails trying to do so. Moreover, it does not provide the .egg-info which makes setuptools fail to detect it even if you have already installed it from a different source. For these reasons you're expected to install PyQt yourself, possibly from your distribution's software repository. If you're installing in a virtualenv you can use --system-site-packages option or copy globally installed PyQt to it.

.. [2] Only PyQt 5 version is provided as PyPI package but you can find versions ported to PyQt 4 under tags prefixed with pyqt4 (e.g. pyqt4-v0.1.0).

Usage
=====

It's as simple as:

.. code-block:: python

    from auto_resizing_text_edit import AutoResizingTextEdit

    editor = AutoResizingTextEdit()

The widget also provides a simple way to constrain its minimum width to a specific number of lines (provided that all the text in the editor uses the same font; if not, you're on your own here):

.. code-block:: python

    editor.setMinimumLines(3)

That's all there is to it. You put it in a layout and forget about it:

.. code-block:: python

    from PyQt5.QtWidgets import QWidget, QVBoxLayout

    widget = QWidget()
    editor.setParent(widget)

    layout = QVBoxLayout(widget)
    layout.addWidget(editor)
    layout.addStretch()

    widget.setLayout(layout)

If you need more or just want to see the editor in action, there are a few simple but complete examples in examples/ directory.

License
=======

Copyright © Kamil Śliwak

Released under the `MIT License`_.

.. _`auto-resizing-text-edit on PyPI`: https://pypi.python.org/pypi/auto-resizing-text-edit
.. _`python-auto-resizing-text-edit in AUR`: https://aur.archlinux.org/packages/python-auto-resizing-text-edit
.. _`setuptools documentation`: https://pythonhosted.org/setuptools/setuptools.html#command-reference
.. _`MIT License`: http://opensource.org/licenses/MIT
