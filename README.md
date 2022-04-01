# Copy helper

A program with a UI for fast text copying.

## Configuration files

- `properties.json`: used to configure common properties.
  - You can adjust the height of the fields and the font size.
  - You can choose one of two button display modes: **columns** for displaying buttons in columns by groups without labels, **rows** for displaying buttons with labels in one column.
- `messages.json`: used to configure localized messages.
- `data.json`: used to configure data to be copied.
  - You can declare groups of fields.
  - For each field, you must specify its name and value.
  - Group names are used as column headers when **column** mode is enabled, field names are used as field captions in **rows** mode.

## Dependencies

- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro)
- [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)

## Usage

1. Install the python interpreter from the [official website](https://www.python.org/).
2. Install the PyQt5 package:
  ```shell
  pip install pyqt5
  ```
3. Install the jsonschema package:
  ```shell
  pip install jsonschema
  ```
4. Launch the application in the *sources* directory:
  ```shell
  python main.py
  ```

## Feedback

If you find a bug or have suggestions for improvement, create an issue on GitHub.
