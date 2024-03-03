from flask import Flask, render_template, request, redirect, url_for
from url_checker import url_validation

# data = [[38,  3,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
#         0]]

# scaled_data = load_scaler.transform(data)
# print(scaled_data)

# prediction = load_model.predict(scaled_data)
# prediction = load_model.predict_proba(scaled_data)

# print(prediction)



app = Flask(__name__)


# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')

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
        #     return redirect('index.html', result=result)
        return render_template('index.html')