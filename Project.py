from flask import Flask
from flask.templating import render_template
# from flask.ext.codemirror import CodeMirror

from myform import MyForm
#
# SECRET_KEY = 'secret!'
# # mandatory
# CODEMIRROR_LANGUAGES = ['python', 'html']
# # optional
# CODEMIRROR_THEME = '3024-day'
# CODEMIRROR_ADDONS = (
#             ('display','placeholder'),
# )


app = Flask(__name__)
# app.config.from_object(__name__)
# codemirror = CodeMirror(app)


# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     form = MyForm()
#     if form.validate_on_submit():
#         text = form.source_code.data
#     return render_template("index.html", form=form)
#

@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
