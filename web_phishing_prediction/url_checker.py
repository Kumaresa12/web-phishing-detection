import joblib
import os

dir = os.getcwd()


load_model = joblib.load(dir + rf'\model\svm_modelV2.pkl')
load_scaler = joblib.load(dir + rf'\model\minmax_scaler.pkl')

def url_validation(url: str):
    url_data = {}

    url_data['url_length'] = len(url)
    url_data['n_dots'] = url.count('.')
    url_data['n_hypens'] = url.count('-')
    url_data['n_underline'] = url.count('_')
    url_data['n_slash'] = url.count('/')
    url_data['n_questionmark'] = url.count('?')
    url_data['n_equal'] = url.count('=')
    url_data['n_at'] = url.count('@')
    url_data['n_and'] = url.count('&')
    url_data['n_exclamation'] = url.count('!')
    url_data['n_space'] = url.count('%20')
    url_data['n_tilde'] = url.count('~')
    url_data['n_comma'] = url.count(',')
    url_data['n_plus'] = url.count('+')
    url_data['n_asterisk'] = url.count('*')
    url_data['n_hastag'] = url.count('#')
    url_data['n_dollar'] = url.count('$')
    url_data['n_percent'] = url.count('%')
    print(url_data)
    
    data = [[url_data['url_length'], url_data['n_dots'], url_data['n_hypens'], url_data['n_underline'], url_data['n_slash'], url_data['n_questionmark'], url_data['n_equal'], url_data['n_at'], url_data['n_and'], url_data['n_exclamation'], url_data['n_space'], url_data['n_tilde'], url_data['n_comma'], url_data['n_plus'], url_data['n_asterisk'], url_data['n_hastag'], url_data['n_dollar'], url_data['n_percent']]]
    print(data)

    scaled_data = load_scaler.transform(data)

    prediction = load_model.predict(scaled_data)
    prediction_proba = load_model.predict_proba(scaled_data)
    print(prediction_proba)
    print(type(prediction_proba))
    print(prediction_proba[0][1])

    print(prediction)

    return True


        