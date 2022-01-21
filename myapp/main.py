import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc

#Membaca dataset dari Covid_19.csv
df = pd.read_csv('data/Covid_19.csv', parse_dates=['Date'])

#Menyimpan baris-baris tiap index di variabel kalbar, kaltim dan kalteng
kalbar = df[df.Location == 'Kalimantan Barat']
kaltim = df[df.Location == 'Kalimantan Timur']
kalteng = df[df.Location == 'Kalimantan Tengah']

#Menampilkan source data kalbar, kaltim, kalteng
source_kalbar = ColumnDataSource(data=kalbar)
source_kaltim = ColumnDataSource(data=kaltim)
source_kalteng = ColumnDataSource(data=kalteng)

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

#Menampilkan line plot New Cases dari kalbar
a = fig1.line(
    x='Date',
    y='New Cases',
    source=source_kalbar,
    color='blue',
    legend_label='Kalimantan Barat'
)

#Menampilkan line plot New Cases dari kaltim
b = fig1.line(
    x='Date',
    y='New Cases',
    source=source_kaltim,
    color='red',
    legend_label='Kalimantan Timur'
)

#Menampilkan line plot New Cases dari kalteng
c = fig1.line(
    x='Date',
    y='New Cases',
    source=source_kalteng,
    color='yellow',
    legend_label='Kalimantan Tengah'
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

#Menampilkan line plot New Deaths dari kalbar
a = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_kalbar,
    color='blue',
    legend_label='Kalimantan Barat'
)

#Menampilkan line plot New Deaths dari kaltim
b = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_kaltim,
    color='red',
    legend_label='Kalimantan Timur'
)

#Menampilkan line plot New Deaths dari kalteng
c = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_kalteng,
    color='yellow',
    legend_label='Kalimantan Tengah'
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

#Menampilkan line plot Total Active Cases dari kalbar
a = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_kalbar,
    color='blue',
    legend_label='Kalimantan Barat'
)

#Menampilkan line plot Total Active Cases dari kaltim
b = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_kaltim,
    color='red',
    legend_label='Kalimantan Timur'
)

#Menampilkan line plot Total Active Cases dari kalteng
c = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_kalteng,
    color='yellow',
    legend_label='Kalimantan Tengah'
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
