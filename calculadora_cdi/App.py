from flask import Flask, render_template, request, jsonify
from datetime import datetime, date
from matplotlib import pyplot as plot
import numpy as np
from bcb import sgs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    capital = float(input("Digite o capital investido: "))
    frequencia = input("Digite a frequência do periodo(Y,m,D): ")
    inicio = input("Digite a data inicial maior do que 1995/01/01 no formato YYYY/MM/DD: ")
    final = input("Digite a data final no seguinte formato YYYY/MM/DD: ")

    data_inicial = datetime.strptime(inicio, "%Y/%m/%d").date()
    data_final = datetime.strptime(final, "%Y/%m/%d").date()

    taxaselic = sgs.get({"selic":11}, start = data_inicial,
    end = data_final)
    taxaselic = taxaselic*100


    #calcular retorno do periodo

    capital_acumulado = capital = (1 + taxaselic["selic"]).cumprod() -1
    capital_com_frequencia = capital_acumulado.resample(frequencia).last()

    resultado = capital_com_frequencia.tolist()

    return jsonify({"capital_com_frequencia": resultado})

if __name__ == '__main__':
    app.run(debug = True)
    


