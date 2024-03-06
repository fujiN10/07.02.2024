from flask import Flask, url_for, request, render_template
from data import db_session

app = Flask(__name__)


@app.route('/')
def slash():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    a = ['Человечество вырастает из детства.',

         'Человечеству мала одна планета.',

         'Мы сделаем обитаемыми безжизненные пока планеты.',

         'И начнем с Марса!',

         'Присоединяйся!']
    return '</br>'.join(a)


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Жди нас, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                    <h2>Вот она какая, красная планета.<h2>
                    <div class="alert alert-primary" role="alert">
                    </div>
                  </body>
                </html>'''


@app.route('/index1')
def index1():
    return render_template('index.html')


@app.route('/training/<prof>')
def training(prof):
    return render_template('train.html', prof=prof)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')
