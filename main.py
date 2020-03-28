from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime
import pandas

data = pandas.read_excel(r'C:\Users\mokko\Desktop\wine-master\wine.xlsx', na_values='', keep_default_na=False, usecols=['Название', 'Цена', 'Картинка', 'Сорт'], sheet_name='wines')
print(data)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('index.html')
first_year = datetime.datetime(year=1920, month=1, day=1, hour=0)
today = datetime.datetime.now()
delta = today.year - first_year.year

wines = [
    {
        "title": data['Название'].tolist()[0],
        "price": data['Цена'].tolist()[0],
        "image": data['Картинка'].tolist()[0],
        "type": data['Сорт'].tolist()[0]
    },
    {
        "title": data['Название'].tolist()[1],
        "price": data['Цена'].tolist()[1],
        "image": data['Картинка'].tolist()[1],
        "type": data['Сорт'].tolist()[1]
    },
    {
        "title": data['Название'].tolist()[2],
        "price": data['Цена'].tolist()[2],
        "image": data['Картинка'].tolist()[2],
        "type": data['Сорт'].tolist()[2]
    },
    {
        "title": data['Название'].tolist()[3],
        "price": data['Цена'].tolist()[3],
        "image": data['Картинка'].tolist()[3],
        "type": data['Сорт'].tolist()[3]
    },
    {
        "title": data['Название'].tolist()[4],
        "price": data['Цена'].tolist()[4],
        "image": data['Картинка'].tolist()[4],
        "type": data['Сорт'].tolist()[4]
    },
    {
        "title": data['Название'].tolist()[5],
        "price": data['Цена'].tolist()[5],
        "image": data['Картинка'].tolist()[5],
        "type": data['Сорт'].tolist()[5]
    },
]

rendered_page = template.render(
    age=delta,
    wines=wines,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
