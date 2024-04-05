# scp -P 2223 -r .\flask\ lsm@192.168.43.57:~/bitdoglab-iot/exemplos/
import os
from flask import Flask, render_template, redirect, request, flash
import json
import pandas as pd
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'PEDRO'

def CreateCsv(filename, col1, col2, col3, col4, col5):
    d = {col1: [], col2: [], col3: [], col4: [], col5: []}
    df = pd.DataFrame(data=d)
    df.to_csv(filename, index=False)
    df = pd.read_csv(filename)
    return df

def getform(date, sensor, max_field, min_field, alerta_field, col1 = 'data', col2 = 'sensor', col3 = 'max', col4 = 'min', col5 = 'alerta'):
    max = request.form[max_field]
    min = request.form[min_field]
    alerta = request.form[alerta_field]
    new_row = {col1: date, col2: sensor, col3: max, col4: min, col5: alerta}
    return new_row

def append_row(filename, new_row, col1 = 'data', col2 = 'sensor', col3 = 'max', col4 = 'min', col5 = 'alerta'):
    if(os.path.isfile(filename)):
        df = pd.read_csv(filename)
    else:
        df = CreateCsv(filename, col1, col2, col3, col4, col5)
    df.loc[len(df)] = new_row
    df.to_csv(filename, index=False)

    return df

def append_row2(filename, new_row, col1 = 'temperatura', col2 = 'umidade', col3 = 'luminosidade'):
    if(os.path.isfile(filename)):
        df = pd.read_csv(filename)
    else:
        df = CreateCsv2(filename, col1, col2, col3)
    df.loc[len(df)] = new_row
    df.to_csv(filename, index=False)

    return df

def CreateCsv2(filename, col1, col2, col3):
    d = {col1: [], col2: [], col3: []}
    df = pd.DataFrame(data=d)
    df.to_csv(filename, index=False)
    df = pd.read_csv(filename)
    return df

def limiar(filename, col1 = 'data', col2 = 'sensor', col3 = 'max', col4 = 'min', col5 = 'alerta'):
    if(os.path.isfile(filename)):
        df = pd.read_csv(filename)
    else:
        return "0$$$0$$$0$$$0$$$Led"
    
    var = f"{str(df.iloc[-1][col1])}$$${str(df.iloc[-1][col2])}$$${str(df.iloc[-1][col3])}$$${str(df.iloc[-1][col4])}$$${str(df.iloc[-1][col5])}"
    return var

def check_key(key, data):
        if key in data:
            pass
        else:
            data[key] = 0

@app.route('/')
def home():
    filename = 'dados.csv'
    if(os.path.isfile(filename)):
        df = pd.read_csv(filename)
    else:
        new_row = [0, 0, 0]
        df = append_row2(filename = filename, new_row=new_row, col1 = "temperatura", col2 = "umidade", col3 = "luminosidade")

    sensor = get_limiar().split('$$$')[1]
    if sensor == 'temperatura':
        max = get_limiar().split('$$$')[2]
        min = get_limiar().split('$$$')[3]
        disp = get_limiar().split('$$$')[4]
    
        return render_template('index.html', 
                            temp_html=df.iloc[-1]['temperatura'], 
                            umidade_html=df.iloc[-1]['umidade'],
                            luminosidade_html=df.iloc[-1]['luminosidade'],
                            max_temp = get_limiar().split('$$$')[2],
                            min_temp = get_limiar().split('$$$')[3],
                            disp_temp = get_limiar().split('$$$')[4],
                            max_lum = 0,
                            min_lum = 0,
                            disp_lum = "Desativado",
                            max_umid = 0,
                            min_umid = 0,
                            disp_umid = "Desativado",
                            
                            )
    
    if sensor == 'luminosidade':
        max = get_limiar().split('$$$')[2]
        min = get_limiar().split('$$$')[3]
        disp = get_limiar().split('$$$')[4]
    
        return render_template('index.html', 
                            temp_html=df.iloc[-1]['temperatura'], 
                            umidade_html=df.iloc[-1]['umidade'],
                            luminosidade_html=df.iloc[-1]['luminosidade'],
                            max_lum = get_limiar().split('$$$')[2],
                            min_lum = get_limiar().split('$$$')[3],
                            disp_lum = get_limiar().split('$$$')[4],
                            max_temp = 0,
                            min_temp = 0,
                            disp_temp = "Desativado",
                            max_umid = 0,
                            min_umid = 0,
                            disp_umid = "Desativado",
                            )
    
    if sensor == 'umidade':
        max = get_limiar().split('$$$')[2]
        min = get_limiar().split('$$$')[3]
        disp = get_limiar().split('$$$')[4]
    
        return render_template('index.html', 
                            temp_html=df.iloc[-1]['temperatura'], 
                            umidade_html=df.iloc[-1]['umidade'],
                            luminosidade_html=df.iloc[-1]['luminosidade'],
                            max_lum = 0,
                            min_lum = 0,
                            disp_lum = "Desativado",
                            max_temp = 0,
                            min_temp = 0,
                            disp_temp = "Desativado",
                            max_umid = get_limiar().split('$$$')[2],
                            min_umid = get_limiar().split('$$$')[3],
                            disp_umid = get_limiar().split('$$$')[4],
                            )
    else:
        return render_template('index.html', 
                            temp_html=df.iloc[-1]['temperatura'], 
                            umidade_html=df.iloc[-1]['umidade'],
                            luminosidade_html=df.iloc[-1]['luminosidade'],
                            max_lum = 0,
                            min_lum = 0,
                            disp_lum = "Desativado",
                            max_temp = 0,
                            min_temp = 0,
                            disp_temp = "Desativado",
                            max_umid = 0,
                            min_umid = 0,
                            disp_umid = "Desativado",
                            )

    # return render_template('index.html', 
    #                     temp_html=df.iloc[-1]['temperatura'], 
    #                     umidade_html=df.iloc[-1]['umidade'],
    #                     luminosidade_html=df.iloc[-1]['luminosidade'],
    #                     max_temp=limiar_temperatura().split('$$$')[0],
    #                     min_temp=limiar_temperatura().split('$$$')[1],
    #                     disp_temp=limiar_temperatura().split('$$$')[2],
    #                     max_umid=limiar_umidade().split('$$$')[0],
    #                     min_umid=limiar_umidade().split('$$$')[1],
    #                     disp_umid=limiar_umidade().split('$$$')[2],
    #                     max_lum=limiar_luminosidade().split('$$$')[0],
    #                     min_lum=limiar_luminosidade().split('$$$')[1],
    #                     disp_lum=limiar_luminosidade().split('$$$')[2]

    #                        )


@app.route('/send_data', methods=['POST'])

def current():   
    data = request.json
    new_row = [data['temperatura'], data['umidade'], data['luminosidade']]
    print(new_row)
    append_row2(filename = "dados.csv", new_row=new_row, col1 = "temperatura", col2 = "umidade", col3 = "luminosidade")

    return render_template('index.html')

@app.route('/get_limiar', methods=['GET'])
def get_limiar():

    filename = "limiares.csv"
    var = limiar(filename)
    
    return var
# ######### SENSOR ##############
# @app.route('/choose_sensor', methods=['POST'])

# def getform_sensor():

#     x = request.form['sensor']
#     # sensor_temp = request.form[sensor_temp]
#     # sensor_umid = request.form[sensor_umid]
#     # sensor_lum = request.form[sensor_lum]
#     # print(f"sensor temp {sensor_temp}")
#     # print(f"sensor umid {sensor_umid}")
#     # print(f"sensor lum {sensor_lum}")

#     return render_template('index.html')
######### TEMPERATURA #########
@app.route('/set_temperatura', methods=['POST'])
def getform_temperatura():
    
    filename = 'limiares.csv'
    sensor = 'temperatura'
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    new_row = getform(data,
                      sensor, 
                      max_field = "temp_max", 
                      min_field = "temp_min", 
                      alerta_field = "alerta_temp")
    append_row(filename, new_row)

    return render_template('index.html')




######### UMIDADE #########
@app.route('/set_umidade', methods=['POST'])
def getform_umidade():

    filename = 'limiares.csv'
    sensor = 'umidade'
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    new_row = getform(data,
                      sensor, 
                      max_field = "umid_max", 
                      min_field = "umid_min", 
                      alerta_field = "alerta_umid")
    append_row(filename, new_row)

    return render_template('index.html')

# @app.route('/get_umidade', methods=['GET'])
# def limiar_umidade():

#     filename = "umidade_limiares.csv"
#     var = limiar(filename)
    
#     return var

######### RUIDO #########
# @app.route('/set_ruido', methods=['POST'])

# def getform_ruido():
    
#     filename = 'limiares.csv'
#     sensor = 'ruido'
#     data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
#     new_row = getform(data,
#                       sensor, 
#                       max_field = "temp_max", 
#                       min_field = "temp_min", 
#                       alerta_field = "alerta_temp")
#     append_row(filename, new_row)

#     return render_template('index.html')

# @app.route('/get_ruido', methods=['GET'])
# def limiar_ruido():
#     filename = "ruido_limiares.csv"
#     var = limiar(filename)
    
#     return var

######### LUMINOSIDADE #########
@app.route('/set_luminosidade', methods=['POST'])

def getform_luminosidade():

    filename = 'limiares.csv'
    sensor = 'luminosidade'
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    new_row = getform(data,
                      sensor, 
                      max_field = "lum_max", 
                      min_field = "lum_min", 
                      alerta_field = "alerta_lum")
    append_row(filename, new_row)

    return render_template('index.html')

# @app.route('/get_luminosidade', methods=['GET'])
# def limiar_luminosidade():
#     filename = "luminosidade_limiares.csv"
#     var = limiar(filename)
    
#     return var



if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")

# @app.route('/json_example', methods=['POST'])
# def handle_json():
#     data = request.json
#     print(data.get('name'))
#     print(data.get('age'))
#     return data