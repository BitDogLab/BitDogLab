import os
from flask import Flask, render_template, redirect, request, flash
import json
import pandas as pd
app = Flask(__name__)
app.config['SECRET_KEY'] = 'PEDRO'

def CreateCsv(filename):
    d = {'temp_max': [], 'temp_min': [], 'select': []}
    df = pd.DataFrame(data=d)
    df.to_csv(filename, index=False)
    df = pd.read_csv(filename)
    return df

@app.route('/')
def home():
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    def check_key(key, data):
        if key in data:
            pass
        else:
            data[key] = 0

    check_key("temp", data)
    check_key("umidade", data)
    check_key("ruido", data)
    check_key("luminosidade", data)
    
    return render_template('index.html', 
                           temp_html=data['temp'], 
                           umidade_html=data['umidade'],
                           ruido_html=data['ruido'],
                           luminosidade_html=data['luminosidade']
                           )


@app.route('/set_current_temp', methods=['GET', 'POST'])

def current():   
    data = request.json
    with open('data.json', 'w') as f:
        json.dump(data, f)
    print(data['temp'])
    print(data['umidade'])
    print(data['ruido'])
    print(data['luminosidade'])

    return render_template('index.html')

@app.route('/set_temp', methods=['POST'])

def getform_temp():
    
    temp_max = request.form['temp_max']
    temp_min = request.form['temp_min']
    select = request.form['alerta_temp']
    new_row = {"temp_max": temp_max, "temp_min": temp_min, "select": select}
  
    if(os.path.isfile("temp_limiares.csv")):
        df = pd.read_csv("temp_limiares.csv")
        
    else:
        df = CreateCsv("temp_limiares.csv")
    
    df.loc[len(df)] = new_row
    df.to_csv("temp_limiares.csv", index=False)
    
    return render_template('index.html')

@app.route('/limiar_temp', methods=['GET'])
def limiar_temp():
    
    if(os.path.isfile("temp_limiares.csv")):
        df = pd.read_csv("temp_limiares.csv")
    else:
        return "nada"
    
    var = f"{str(df.iloc[-1]['temp_max'])}$$${str(df.iloc[-1]['temp_min'])}$$${str(df.iloc[-1]['select'])}"
    
    return var 

#######################

@app.route('/set_temp', methods=['POST'])

def getform_temp():
    
    temp_max = request.form['temp_max']
    temp_min = request.form['temp_min']
    select = request.form['alerta_temp']
    new_row = {"temp_max": temp_max, "temp_min": temp_min, "select": select}
  
    if(os.path.isfile("temp_limiares.csv")):
        df = pd.read_csv("temp_limiares.csv")
        
    else:
        df = CreateCsv("temp_limiares.csv")
    
    df.loc[len(df)] = new_row
    df.to_csv("temp_limiares.csv", index=False)
    
    return render_template('index.html')

@app.route('/limiar_temp', methods=['GET'])
def limiar_temp():
    
    if(os.path.isfile("temp_limiares.csv")):
        df = pd.read_csv("temp_limiares.csv")
    else:
        return "nada"
    
    var = f"{str(df.iloc[-1]['temp_max'])}$$${str(df.iloc[-1]['temp_min'])}$$${str(df.iloc[-1]['select'])}"
    
    return var
###############################
@app.route('/set_temp', methods=['POST'])

def getform_temp():
    
    temp_max = request.form['temp_max']
    temp_min = request.form['temp_min']
    select = request.form['alerta_temp']
    new_row = {"temp_max": temp_max, "temp_min": temp_min, "select": select}
  
    if(os.path.isfile("temp_limiares.csv")):
        df = pd.read_csv("temp_limiares.csv")
        
    else:
        df = CreateCsv("temp_limiares.csv")
    
    df.loc[len(df)] = new_row
    df.to_csv("temp_limiares.csv", index=False)
    
    return render_template('index.html')

@app.route('/limiar_temp', methods=['GET'])
def limiar_temp():
    
    if(os.path.isfile("temp_limiares.csv")):
        df = pd.read_csv("temp_limiares.csv")
    else:
        return "nada"
    
    var = f"{str(df.iloc[-1]['temp_max'])}$$${str(df.iloc[-1]['temp_min'])}$$${str(df.iloc[-1]['select'])}"
    
    return var
################################
@app.route('/set_temp', methods=['POST'])

def getform_temp():
    
    temp_max = request.form['temp_max']
    temp_min = request.form['temp_min']
    select = request.form['alerta_temp']
    new_row = {"temp_max": temp_max, "temp_min": temp_min, "select": select}
  
    if(os.path.isfile("temp_limiares.csv")):
        df = pd.read_csv("temp_limiares.csv")
        
    else:
        df = CreateCsv("temp_limiares.csv")
    
    df.loc[len(df)] = new_row
    df.to_csv("temp_limiares.csv", index=False)
    
    return render_template('index.html')

@app.route('/limiar_temp', methods=['GET'])
def limiar_temp():
    
    if(os.path.isfile("temp_limiares.csv")):
        df = pd.read_csv("temp_limiares.csv")
    else:
        return "nada"
    
    var = f"{str(df.iloc[-1]['temp_max'])}$$${str(df.iloc[-1]['temp_min'])}$$${str(df.iloc[-1]['select'])}"
    
    return var
####################


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")

# @app.route('/json_example', methods=['POST'])
# def handle_json():
#     data = request.json
#     print(data.get('name'))
#     print(data.get('age'))
#     return data