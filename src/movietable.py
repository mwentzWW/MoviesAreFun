from dash import dash_table
import pandas as pd

def movie_table(df: pd.DataFrame) -> dash_table.DataTable:

    dt = dash_table.DataTable(df.to_dict('records'), 
            [{"name": i, "id": i} for i in df.columns],
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 10)

    return dt