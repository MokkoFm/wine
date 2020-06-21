from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import xlrd
import pprint
from collections import defaultdict

file_with_wines = pandas.read_excel('offer.xlsx', sheet_name='wines', usecols=['category', 'title', 'type', 'price', 'image', 'discount'])
wines_nomenclature = file_with_wines.to_dict(orient='record')
wines_catalog = defaultdict(list)

for wine in wines_nomenclature:
  wines_catalog[wine['category']].append(wine)


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
first_year = datetime.datetime(year=1920, month=1, day=1, hour=0)
today = datetime.datetime.now()
delta = today.year - first_year.year

rendered_page = template.render(
    age=delta,
    wines_catalog=wines_catalog
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()