import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models.widgets import Tabs, Panel

# Membaca dataset dari stock market
df = pd.read_csv('Covid_19.csv', parse_dates=['Date'])

# Untuk menyimpan baris-baris tiap index di variabel jabar, jatim dan jateng
jabar = df[df.Location == 'Jawa Barat']
jatim = df[df.Location == 'Jawa Timur']
jateng = df[df.Location == 'Jawa Tengah']

# Untuk menampilkan source data jabar, jatim, jateng
source_jabar = ColumnDataSource(data=jabar)
source_jatim = ColumnDataSource(data=jatim)
source_jateng = ColumnDataSource(data=jateng)

source_jabar1 = ColumnDataSource(data=jabar)
source_jatim1 = ColumnDataSource(data=jatim)
source_jateng1 = ColumnDataSource(data=jateng)

source_jabar2 = ColumnDataSource(data=jabar)
source_jatim2 = ColumnDataSource(data=jatim)
source_jateng2 = ColumnDataSource(data=jateng)

# Membuat Figure untuk menampilkan adj close
fig1 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='New Cases',
    title='New Cases',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot adj close dari Hangseng
a = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jabar2,
    color='blue',
    legend_label='Jawa Barat'
)

# Untuk menampilkan line plot adj close dari Nasdaq
b = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jatim2,
    color='red',
    legend_label='Jawa Timur'
)

# Untuk menampilkan line plot adj close dari Nikkei
c = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jateng2,
    color='yellow',
    legend_label='Jawa Tengah'
)

# Bokeh Library
tooltips = [
            ('Index','@Location'),
            ('New Cases', '@{New Cases}{0.2f}')
]

# Menambahkan HoverTool untuk membuat fig
fig1.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan volume
fig2 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='New Deaths',
    title='New Deaths',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot Volume dari Hangseng
a = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jabar2,
    color='blue',
    legend_label='Jawa Barat'
)

# Untuk menampilkan line plot volume dari Hangseng
b = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jatim2,
    color='red',
    legend_label='Jawa Timur'
)

# Untuk menampilkan line plot volume dari Hangseng
c = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jateng2,
    color='yellow',
    legend_label='Jawa Tengah'
)

# Bokeh Library
tooltips = [
            ('Index','@Location'),
            ('New Deaths', '@{New Deaths}{0.2f}')
]

# Menambahkan HoverTool untuk membuat fig
fig2.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan day perc change
fig3 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Total Active Cases',
    title='Total Active Cases',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot day perc change dari Hangseng
a = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jabar2,
    color='blue',
    legend_label='Jawa Barat'
)

# Untuk menampilkan line plot day perc change dari Nasdaq
b = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jatim2,
    color='red',
    legend_label='Jawa Timur'
)

# Untuk menampilkan line plot day perc change dari Nikkei
c = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jateng2,
    color='yellow',
    legend_label='Jawa Tengah'
)

# Bokeh Library
tooltips = [
            ('Index','@Location'),
            ('Total Active Cases', '@{Total Active Cases}{0.2f}')
]

# Menambahkan HoverTool untuk membuat fig
fig3.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Menampilkan ke plot HTML
output_file('Level 3.html', title='Level 3')

fig1.legend.click_policy = 'hide'
fig2.legend.click_policy = 'hide'
fig3.legend.click_policy = 'hide'

# Membuat tiga panel yaitu Adj Close,Volume,Day Perc Change
New_Cases = Panel(
    child=fig1,
    title='New Cases'
)
New_Deaths = Panel(
    child=fig2,
    title='New Deaths'
)
Total_Active_Cases = Panel(
    child=fig3,
    title='Total Active Cases'
)

tabs = Tabs(tabs=[
                  New_Cases, New_Deaths, Total_Active_Cases
                ])

show(tabs)