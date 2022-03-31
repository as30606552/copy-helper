from params import Properties, Messages, Data
from ui import init_app, start_app, ColumnsWindow, RowsWindow

if __name__ == '__main__':
    props = Properties()
    msgs = Messages()
    data = Data()

    init_app()

    if props.mode == 'columns':
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
    elif props.mode == 'rows':
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

    start_app()
