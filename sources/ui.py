import sys
from typing import Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLayout, QGridLayout, QLabel, QPushButton

_app: Optional[QApplication] = None


def init_app():
    global _app
    _app = QApplication(sys.argv)


def start_app():
    global _app
    sys.exit(_app.exec())


class _Window:

    def __init__(self, title: str, spacing: int, row_height: int, font_size: int, critical_value_size: int):
        self.__widget = QWidget()
        self.__widget.setWindowTitle(title)
        self.__spacing = spacing
        self.__row_height = row_height
        self.__font_size = font_size
        self.__critical_value_size = critical_value_size

    def show(self):
        self.__widget.move(0, 0)
        self.__widget.setFixedHeight(self.__widget.height())
        self.__widget.show()

    def _vertical_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        self.__init_layout(layout)
        return layout

    def _horizontal_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        self.__init_layout(layout)
        return layout

    def _grid_layout(self) -> QGridLayout:
        layout = QGridLayout()
        self.__init_layout(layout)
        return layout

    def _label(self, text: str) -> QLabel:
        label = QLabel(text, self.__widget)
        self.__init_widget(label, len(text))
        return label

    def _copy_button(self, text: str) -> QPushButton:
        button = QPushButton(text, self.__widget)
        self.__init_widget(button, len(text))
        # noinspection PyUnresolvedReferences
        button.clicked.connect(lambda: _app.clipboard().setText(text))
        return button

    def _set_layout(self, layout: QLayout):
        self.__widget.setLayout(layout)

    def __init_layout(self, layout: QLayout):
        layout.setSpacing(self.__spacing)
        layout.setContentsMargins(self.__spacing, self.__spacing, self.__spacing, self.__spacing)

    def __init_widget(self, widget: QWidget, value_size: int):
        font = widget.font()
        font.setPointSize(self.__font_size - value_size // self.__critical_value_size)
        widget.setFont(font)
        widget.setFixedHeight(self.__row_height)


class ColumnsWindow(_Window):

    def __init__(self, title: str, spacing: int, row_height: int, font_size: int, critical_value_size: int):
        super().__init__(title, spacing, row_height, font_size, critical_value_size)
        self.__columns: list[QVBoxLayout] = []
        self.__main_layout = self._horizontal_layout()
        self._set_layout(self.__main_layout)

    def create_column(self, name: str):
        layout = self._vertical_layout()
        layout.addWidget(self._label(name), alignment=Qt.AlignHCenter)
        layout.addStretch()
        self.__columns.append(layout)
        self.__main_layout.addLayout(layout)

    def add_entry(self, column: int, value: str):
        layout = self.__columns[column]
        layout.insertWidget(layout.count() - 1, self._copy_button(value))


class RowsWindow(_Window):

    def __init__(self, title: str, spacing: int, row_height: int, font_size: int, critical_value_size: int):
        super().__init__(title, spacing, row_height, font_size, critical_value_size)
        self.__main_layout = self._grid_layout()
        self._set_layout(self.__main_layout)
        self.__last_entry_index = 0

    def add_entry(self, name: str, value: str):
        self.__main_layout.addWidget(self._label(name), self.__last_entry_index, 0)
        self.__main_layout.addWidget(self._copy_button(value), self.__last_entry_index, 1)
        self.__last_entry_index += 1
