from flask import Flask
import view as v
import controller as c
import literals as lit
app = Flask(__name__)

# @app.route('/')
# @app.route('/hello')
# def hello():
#     return "Hey there!"


@app.route('/')
@app.route('/view_list')
def view_list():
    purchases = []
    all_purchases = c.read_file(purchases)
    return v.display_purchases(all_purchases, lit.BY_NAME)

if __name__ == '__main__':
    app.run('localhost', 4449)
