""" This example demonstrates how AutoResizingTextEdit interacts with other widgets in the same layout.
    It also shows how to use lineCountToWidgetHeight(). """

import sys
from PyQt4.QtGui             import QApplication, QWidget, QTextEdit, QVBoxLayout, QSizePolicy
from auto_resizing_text_edit import AutoResizingTextEdit

application = QApplication(sys.argv)

widget        = QWidget()
top_editor    = AutoResizingTextEdit(widget)
middle_editor = QTextEdit(widget)
bottom_editor = AutoResizingTextEdit(widget)

top_editor.setMinimumLines(3)

layout = QVBoxLayout(widget)
layout.addWidget(top_editor)
layout.addWidget(middle_editor)
layout.addWidget(bottom_editor)

widget.setLayout(layout)
widget.show()

sys.exit(application.exec_())
