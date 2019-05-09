from flask import Flask, render_template 
app = Flask(__name__)
app.debug = True

#Articles = Articles()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cidadeverde')
def cidadeverde():
    return render_template('cidadeverde.html')

@app.route('/g1piaui')
def g1piaui():
    return render_template('g1piaui.html')

@app.route('/cidademodelo')
def cidademodelo():
    return render_template('cidademodelo.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

if __name__ == '__main__':
    app.run()

