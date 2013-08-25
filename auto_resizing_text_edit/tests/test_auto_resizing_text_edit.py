import unittest
from datetime import datetime

from PyQt4.QtGui import QTextEdit, QVBoxLayout, QWidget

from .dummy_application        import application
from ..auto_resizing_text_edit import AutoResizingTextEdit

class AutoResizingTextEditTest(unittest.TestCase):
    def setUp(self):
        self.auto_resizing_text_edit = AutoResizingTextEdit()

    def test_should_make_parent_widget_and_layout_report_having_height_for_width(self):
        parent = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.auto_resizing_text_edit)
        parent.setLayout(layout)

        self.assertTrue(layout.hasHeightForWidth())
        #self.assertTrue(parent.hasHeightForWidth())

    def test_should_keep_preferred_height_when_extra_space_is_available(self):
        size_hint     = self.auto_resizing_text_edit.sizeHint()
        parent_height = size_hint.height() + 100

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.auto_resizing_text_edit)
        layout.addStretch()

        parent = QWidget()
        self.auto_resizing_text_edit.setParent(parent)

        parent.resize(size_hint.width(), parent_height)
        parent.setLayout(layout)

        # The window needs to get shown for the size changes to be propagated to layout.
        # Show it minimized to avoid stealing focus from the console running the tests.
        parent.showMinimized()

        self.assertEqual(self.auto_resizing_text_edit.height(), size_hint.height())
        self.assertEqual(self.auto_resizing_text_edit.width(),  parent.width())

    def test_should_resize_to_match_height_for_width_when_user_enters_text(self):
        size_hint     = self.auto_resizing_text_edit.sizeHint()
        parent_height = size_hint.height() + 200

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.auto_resizing_text_edit)
        layout.addStretch()

        parent = QWidget()
        self.auto_resizing_text_edit.setParent(parent)

        parent.resize(size_hint.width(), parent_height)
        parent.setLayout(layout)

        # The window needs to get shown for the size changes to be propagated to layout.
        # Show it minimized to avoid stealing focus from the console running the tests.
        parent.showMinimized()

        assert self.auto_resizing_text_edit.height(), size_hint.height()
        assert self.auto_resizing_text_edit.width(),  parent.width()

        self.auto_resizing_text_edit.setPlainText('a\nb\nc\d')
        new_height_hint = self.auto_resizing_text_edit.heightForWidth(self.auto_resizing_text_edit.width())
        application.processEvents()

        self.assertNotEqual(new_height_hint, size_hint.height())
        self.assertEqual(self.auto_resizing_text_edit.height(), new_height_hint)
        self.assertEqual(self.auto_resizing_text_edit.width(),  parent.width())

    def test_setMinimumLines_should_set_minimum_height_to_specified_number_of_lines(self):
        for num_lines in range(5):
            minimum_size_before = self.auto_resizing_text_edit.minimumSize()

            self.auto_resizing_text_edit.setMinimumLines(num_lines)

            self.assertEqual(self.auto_resizing_text_edit.minimumSize().width(), minimum_size_before.width())
            self.assertEqual(self.auto_resizing_text_edit.minimumSize().height(), self.auto_resizing_text_edit.lineCountToWidgetHeight(num_lines))

    def test_heightForWidth_should_return_height_based_on_height_of_document_with_same_content_if_there_are_no_margins(self):
        text = (('x ' * 10) + '\n') * 10

        self.auto_resizing_text_edit.setPlainText(text)
        self.auto_resizing_text_edit.setContentsMargins(0, 0, 0, 0)

        document = self.auto_resizing_text_edit.document().clone()

        for text_width in [0, 1, 10, 20, 40, 70, 99, 100, 200, 300, 1000]:
            height_for_width = self.auto_resizing_text_edit.heightForWidth(text_width)
            document.setTextWidth(text_width)
            assert document.textWidth() == text_width

            self.assertEqual((height_for_width, text_width), (document.size().height(), text_width))

    def test_heightForWidth_should_add_margin_height(self):
        text         = (('x ' * 10) + '\n') * 10
        widget_width = 100
        text_width   = widget_width - 11 - 33

        self.auto_resizing_text_edit.setPlainText(text)
        self.auto_resizing_text_edit.setContentsMargins(11, 22, 33, 44)

        document = self.auto_resizing_text_edit.document().clone()
        document.setTextWidth(text_width)
        assert document.textWidth() == text_width

        expected_height_for_width = document.size().height() + 22 + 44

        height_for_width = self.auto_resizing_text_edit.heightForWidth(widget_width)

        self.assertEqual(height_for_width, expected_height_for_width)

    def test_heightForWidth_should_assume_minimal_document_width_if_width_is_smaller_than_margins(self):
        text = (('x ' * 10) + '\n') * 10

        self.auto_resizing_text_edit.setPlainText(text)
        self.auto_resizing_text_edit.setContentsMargins(111, 222, 333, 444)

        document = self.auto_resizing_text_edit.document().clone()
        document.setTextWidth(0)
        assert document.textWidth() == 0

        expected_height_for_width = document.size().height() + 222 + 444

        for widget_width in [0, 10, 50, 100, 200, 111 + 332, 111 + 333]:
            assert widget_width <= 111 + 333

            height_for_width = self.auto_resizing_text_edit.heightForWidth(widget_width)

            self.assertEqual((height_for_width, widget_width), (expected_height_for_width, widget_width))

    def test_sizeHint_should_return_height_matching_heightForWidth(self):
        size_hint = self.auto_resizing_text_edit.sizeHint()

        self.assertGreater(size_hint.width(), 0)
        self.assertEqual(size_hint.height(), self.auto_resizing_text_edit.heightForWidth(size_hint.height()))

    def test_lineCountToWidgetHeight_should_return_correct_widget_height(self):
        for num_lines in range(5):
            text = '\n'.join(['line'] * num_lines)
            self.auto_resizing_text_edit.setPlainText(text)

            # Use width high enough to avoid line wrapping
            expected_height = self.auto_resizing_text_edit.heightForWidth(1000)

            height = self.auto_resizing_text_edit.lineCountToWidgetHeight(num_lines)

            self.assertEqual((height, num_lines), (expected_height, num_lines))
