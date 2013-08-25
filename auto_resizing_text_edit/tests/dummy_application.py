""" This module provides an instance of QApplication to be used by unit tests.
    Qt does not seem to work properly if QApplication is destroyed after each test.

    Import this module from any unit test that needs access to the application object.
    Even if no test is using the object directly, at least one should import it to ensure
    that the object gets created.
"""

import sys

from PyQt4.QtGui import QApplication

application = QApplication(sys.argv)
