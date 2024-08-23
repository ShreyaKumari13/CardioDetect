from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from chat import get_response
import pickle

app = Flask(__name__)
CORS(app)

# Load the model for heart disease prediction
all_models = pickle.load(open('models.pkl', 'rb'))


@app.post("/predicted")
def predicted():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route('/', methods=['GET', 'POST'])
def hey():
    return render_template("signin.html")

@app.route('/index', methods=['GET', 'POST'])
def hello():
    return render_template("index.html")

@app.route('/heart', methods=['GET', 'POST'])
def heart():
    return render_template("heart.html")

@app.route('/chatu', methods=['GET', 'POST'])
def chatu():
    return render_template('chatu.html')

@app.route('/accordion__content', methods=['GET', 'POST'])
def accordion__content():
    return render_template("index.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email == email and password == password:
        return jsonify({'redirect': '/index'})
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/api', methods=['POST'])
def predict():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    fgender = request.form['gender']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']
    
    if trestbps == '':
        trestbps = 95
    if chol == '':
        chol = 150
    if thalach == '':
        thalach = 72
    if oldpeak == '':
        oldpeak = 2

    received_features = [age, fgender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    input_data = {
        "age": age,
        "Gender": fgender,
        "Chest Pain Types": cp,
        "Resting Blood Pressure(in mm/Hg)": trestbps,
        "Cholesterol Level": chol,
        "is Fasting Blood Pressure>120mg/Dl?": fbs,
        "Resting Electro Cardio Graphic Result": restecg,
        "Maximum Heart Rate Achieved": thalach,
        "Does Exercise Induced Angina?": exang,
        "Old Peak (ST Depression Induced by Exercise Relative to Rest)": oldpeak,
        "Slope of ST Segment": slope,
        "number of major vessels (0-3) colored by flourosopy": ca,
        "Thal Type": thal
    }

    if fgender == "Male":
        gender = 1
    else:
        gender = 0
    
    if thal == "Normal":
        thal = 0
    elif thal == "Fixed Defect":
        thal = 1
    else:
        thal = 2

    if restecg == "Normal":
        restecg = 0
    elif restecg == "STT Abnormality":
        restecg = 1
    else:
        restecg = 2
    if exang == "Yes":
        exang = 1
    else:
        exang = 0

    age = int(age)
    cp = int(cp)
    trestbps = int(trestbps)
    chol = int(chol)
    fbs = int(fbs)
    thalach = int(thalach)
    oldpeak = int(oldpeak)
    slope = int(slope)
    ca = int(ca)
    features = [age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    dict = {}
    avg = 0
    for model in all_models:
        res = model.predict([features])
        if res[0] == 1:
            dict[model] = "High Chance of Heart Disease"
        else:
            dict[model] = "Low Chance of Heart Disease"
        avg += res
    accuracy = round(avg[0] / 5, 2)
    
    personal_info = [name, email]
    responses = [input_data, dict, personal_info, accuracy]
    
    return render_template("result.html", result=responses)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
