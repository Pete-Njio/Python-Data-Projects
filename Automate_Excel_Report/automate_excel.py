import pandas as pd
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter



df = pd.read_excel('supermarket_sales.xlsx')

df = df[['Gender', 'Product line', 'Total']]

pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)


pivot_table.to_excel('pivot_table.xlsx', sheet_name='Report', startrow=2)

wb = load_workbook('pivot_table.xlsx')
sheet = wb['Report']

min_column = wb.active.min_column
max_column = wb.active.max_column
min_row = wb.active.min_row
max_row = wb.active.max_row

barchart = BarChart()

data = Reference(sheet,
    min_col=min_column+1,
    max_col=max_column,
    min_row=min_row,
    max_row=max_row
)

categories = Reference(sheet,
    min_col=min_column,
    max_col=min_column,
    min_row=min_row+1,
    max_row=max_row
)

for i in range(min_column+1, max_column+1):
    letter = get_column_letter(i)
    sheet[f"{letter}{max_row+1}"] = f'=SUM({letter}{min_row+1}:{letter}{max_row})'
    sheet[f'{letter}{max_row+1}'].number_format = '"R"#,##0'


barchart.add_data(data, titles_from_data=True)
barchart.set_categories(categories)

sheet.add_chart(barchart, "B10")

barchart.title = "Sales by Product line"
barchart.title.overlay = False
barchart.style = 10
barchart.legend.overlay = False

wb.save('pivot_table.xlsx')