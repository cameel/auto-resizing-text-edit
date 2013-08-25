""" This example demonstrates how a single AutoResizingTextEdit adjusts its size. """

import sys
from PyQt5.QtWidgets         import QApplication, QWidget, QVBoxLayout
from auto_resizing_text_edit import AutoResizingTextEdit

application = QApplication(sys.argv)

widget = QWidget()
editor = AutoResizingTextEdit(widget)

layout = QVBoxLayout(widget)
layout.addWidget(editor)
layout.addStretch()

widget.setLayout(layout)
widget.show()

sys.exit(application.exec_())
