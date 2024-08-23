# Cardio Detect: Heart Disease Detection and Prediction Web Application
This is a web application which uses multiple ML models, Python(Flask and NLTK) in the backend for predicting heart attack percentage of a person, Front-End is designed through HTML/CSS &amp; JS, also integrated a chatbot for seamless user experience which replies with common diseases treatment recommendations.



## installation

Make sure you have brew installed on your system. If not, follow the steps [here](https://brew.sh) to do so.

- Install Python 2.7 on your system.

  ```
    brew install python@2
  ```

- Update your path variables accordingly

  ```
    export PATH="/usr/local/opt/python@2/libexec/bin:$PATH"
  ```

- Install flask on your system. This is essential for our libraries to work later.

```
 pip install Flask
```

- Install Visual Studio Code by following the steps given in flask.

- Clone the project (or copy the folder to your local)

  ```
    git clone https://github.com/YasinMakandar/Heart-Care
  ```

Now, the project is ready to run.

## Run Locally

After following the above steps for installation, type the command below to run the project.

```bash
  flask run
```

The project is running now.

## Tech Stack

**Language:** Python,Javascript,CSS,HTML
**Algorithms:** Logistic Regression,SVM,Decision Tree,Random Forest,KNN
**Framework:** Flask
**Tools:** VSCode,jupyter notebook
**Libraries:** NumPy,Pandas,Matplotlib

# Chatbot Deployment with Flask and JavaScript


This gives 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial Setup:
This repo currently contains the starter files.

Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```
# firebase-contact-form

a simple contact form using firebase database.

## How to link your firebase:

Go to https://console.firebase.google.com and add a project and a database. In the "rules" tab of the database, set the ".write" key to true
and copy the code to initialize your firebase to the file "main.js"

