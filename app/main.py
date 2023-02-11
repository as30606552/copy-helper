import json

from params import Properties, Messages, Data
from ui import init_app, start_app, ColumnsWindow, RowsWindow


def _load_file(directory: str, filename: str) -> dict:
    with open(f'{directory}/{filename}.json', encoding='utf-8') as file:
        return json.load(file)


def create_columns_window(props: Properties, msgs: Messages, data: Data) -> ColumnsWindow:
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
    return window


def create_rows_window(props: Properties, msgs: Messages, data: Data) -> RowsWindow:
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
    return window


# Need to store the main window in this global variable not to remove it from the function scope
main_window: ColumnsWindow | RowsWindow | None = None


def main(resources_dir: str):
    props = Properties(_load_file(resources_dir, 'properties'))
    msgs = Messages(_load_file(resources_dir, 'messages'))
    data = Data(_load_file(resources_dir, 'data'))

    init_app(f'{resources_dir}/icon.svg')

    global main_window
    if props.mode == 'columns':
        main_window = create_columns_window(props, msgs, data)
    elif props.mode == 'rows':
        main_window = create_rows_window(props, msgs, data)

    start_app()


if __name__ == '__main__':
    main('../resources')
