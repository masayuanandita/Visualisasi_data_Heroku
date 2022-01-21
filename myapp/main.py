import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc

#Membaca dataset dari Covid_19.csv
df = pd.read_csv('data/Covid_19.csv', parse_dates=['Date'])

#Menyimpan baris-baris tiap index di variabel jabar, jatim dan jateng
jabar = df[df.Location == 'Jawa Barat']
jatim = df[df.Location == 'Jawa Timur']
jateng = df[df.Location == 'Jawa Tengah']

#Menampilkan source data kalbar, kaltim, kalteng
source_jabar = ColumnDataSource(data=jabar)
source_jatim = ColumnDataSource(data=jatim)
source_jateng = ColumnDataSource(data=jateng)

#Membuat Figure untuk menampilkan New Cases
fig1 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='New Cases',
    title='New Cases',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

#Menampilkan line plot New Cases dari jabar
a = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jabar,
    color='blue',
    legend_label='Jawa Barat'
)

#Menampilkan line plot New Cases dari jatim
b = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jatim,
    color='red',
    legend_label='Jawa Timur'
)

#Menampilkan line plot New Cases dari jateng
c = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jateng,
    color='yellow',
    legend_label='Jawa Tengah'
)

#BokehLibrary
tooltips = [
            ('Index','@Location'), # ini index isinya nama lokasi
            ('New Cases', '@{New Cases}{f}') 
]

#Menambahkan HoverTool untuk membuat fig
fig1.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

#Membuat Figure untuk menampilkan New Deaths
fig2 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='New Deaths',
    title='New Deaths',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

#Menampilkan line plot New Deaths dari jabar
a = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jabar,
    color='blue',
    legend_label='Jawa Barat'
)

#Menampilkan line plot New Deaths dari jatim
b = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jatim,
    color='red',
    legend_label='Jawa Timur'
)

#Menampilkan line plot New Deaths dari jateng
c = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jateng,
    color='yellow',
    legend_label='Jawa Tengah'
)

# Bokeh Library
tooltips = [
            ('Index','@Location'),
            ('New Deaths', '@{New Deaths}{f}')
]

#Menambahkan HoverTool untuk membuat fig
fig2.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

#Membuat Figure untuk menampilkan Total Active Cases
fig3 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Total Active Cases',
    title='Total Active Cases',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

#Menampilkan line plot Total Active Cases dari jabar
a = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jabar,
    color='blue',
    legend_label='Jawa Barat'
)

#Menampilkan line plot Total Active Cases dari jatim
b = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jatim,
    color='red',
    legend_label='Jawa Timur'
)

#Menampilkan line plot Total Active Cases dari jateng
c = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jateng,
    color='yellow',
    legend_label='Jawa Tengah'
)

#BokehLibrary
tooltips = [
            ('Index','@Location'), 
            ('Total Active Cases', '@{Total Active Cases}{f}')
]

#Menambahkan HoverTool untuk membuat fig
fig3.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Menampilkan ke plot HTML
output_file('templates/index.html', title='index')

#Menambahkan aspek interaktif yang memungkinkan user untuk menyembunyikan data untuk indeks tertentu
fig1.legend.click_policy = 'hide'
fig2.legend.click_policy = 'hide'
fig3.legend.click_policy = 'hide'

#Membuat tiga panel yaitu New Cases, New Deaths, Total Active Cases
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

curdoc().add_root(tabs)
curdoc().title = "Covid-19 Statistic"
