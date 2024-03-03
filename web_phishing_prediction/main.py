from flask import Flask, render_template, request, redirect, url_for
from url_checker import url_validation


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def check():
        if request.method == 'POST':
                url = request.form['url']
                if url:
                        print(url)
                        danger = url_validation(str(url))
                        result = "URL looks like Phishing..." if danger else "URL doesn't look like dangerous..."
                        return render_template('index.html', result=result)
                else:
                        return render_template('index.html')

        return render_template('index.html')