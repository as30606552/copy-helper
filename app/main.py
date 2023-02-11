import json

from params import Properties, Messages, Data
from ui import init_app, start_app, ColumnsWindow, RowsWindow


def _load_file(directory: str, filename: str) -> dict:
    with open(f'{directory}/{filename}.json', encoding='utf-8') as file:
        return json.load(file)


def create_columns_window(props: Properties, msgs: Messages, data: Data):
    window = ColumnsWindow(
        msgs.main_window_caption,
        props.rows_spacing,
        props.row_height,
        props.font_size,
        props.critical_value_size
    )
    for i, column in enumerate(data):
        window.create_column(column.name)
        for row in column:
            window.add_entry(i, row.value)
    window.show()


def create_rows_window(props: Properties, msgs: Messages, data: Data):
    window = RowsWindow(
        msgs.main_window_caption,
        props.rows_spacing,
        props.row_height,
        props.font_size,
        props.critical_value_size
    )
    for column in data:
        for row in column:
            window.add_entry(row.name, row.value)
    window.show()


def main(resources_dir: str):
    props = Properties(_load_file(resources_dir, 'properties'))
    msgs = Messages(_load_file(resources_dir, 'messages'))
    data = Data(_load_file(resources_dir, 'data'))

    init_app()

    if props.mode == 'columns':
        create_columns_window(props, msgs, data)
    elif props.mode == 'rows':
        create_rows_window(props, msgs, data)

    start_app()


if __name__ == '__main__':
    main('../resources')
