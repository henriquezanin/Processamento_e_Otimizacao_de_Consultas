from time import sleep
import psycopg2
import matplotlib.pyplot as plt
import subprocess
import numpy as np
from statistics import mean
    
con = psycopg2.connect(host='10.11.16.116', database='bd1',
user='postgres', password='postgres')
cur = con.cursor()
pre_warm25 = "SELECT pg_prewarm('exercicio25.clube'),pg_prewarm('exercicio25.jogador'), pg_prewarm('exercicio25.joga');"
cur.execute(pre_warm25)
pre_warm50 = "SELECT pg_prewarm('exercicio50.clube'),pg_prewarm('exercicio50.jogador'), pg_prewarm('exercicio50.joga');"
cur.execute(pre_warm50)
pre_warm100 = "SELECT pg_prewarm('exercicio100.clube'),pg_prewarm('exercicio100.jogador'), pg_prewarm('exercicio100.joga');"
cur.execute(pre_warm100)
pre_warm200 = "SELECT pg_prewarm('exercicio200.clube'),pg_prewarm('exercicio200.jogador'), pg_prewarm('exercicio200.joga');"
cur.execute(pre_warm200)

clear_stats = "SELECT pg_stat_reset();"

time_list = list()
sql = "explain (analyse true, timing true) select clube.nomeclube,  jogador.nomejogador, joga.datainiciojoga, joga.datafimjoga, joga.salario from exercicio25.jogador jogador join exercicio25.joga joga on jogador.idjogador = joga.idjogador join exercicio25.clube clube on clube.idclube = joga.idclube;"
for a in range(5):
    cur.execute(clear_stats)
    cur.execute(sql)
    recset = cur.fetchall()
    time_list.append(float(recset[-1][0].split(':')[-1].rstrip('ms')))

exercicio25 = mean(time_list)

time_list = list()
sql = "explain (analyse true, timing true) select clube.nomeclube,  jogador.nomejogador, joga.datainiciojoga, joga.datafimjoga, joga.salario from exercicio50.jogador jogador join exercicio50.joga joga on jogador.idjogador = joga.idjogador join exercicio50.clube clube on clube.idclube = joga.idclube;"
for a in range(5):
    cur.execute(clear_stats)
    cur.execute(sql)
    recset = cur.fetchall()
    time_list.append(float(recset[-1][0].split(':')[-1].rstrip('ms')))

exercicio50 = mean(time_list)

time_list = list()
sql = "explain (analyse true, timing true) select clube.nomeclube,  jogador.nomejogador, joga.datainiciojoga, joga.datafimjoga, joga.salario from exercicio100.jogador jogador join exercicio100.joga joga on jogador.idjogador = joga.idjogador join exercicio100.clube clube on clube.idclube = joga.idclube;"
for a in range(5):
    cur.execute(clear_stats)
    cur.execute(sql)
    recset = cur.fetchall()
    time_list.append(float(recset[-1][0].split(':')[-1].rstrip('ms')))

exercicio100 = mean(time_list)

time_list = list()
sql = "explain (analyse true, timing true) select clube.nomeclube,  jogador.nomejogador, joga.datainiciojoga, joga.datafimjoga, joga.salario from exercicio200.jogador jogador join exercicio200.joga joga on jogador.idjogador = joga.idjogador join exercicio200.clube clube on clube.idclube = joga.idclube;"
for a in range(5):
    cur.execute(clear_stats)
    cur.execute(sql)
    recset = cur.fetchall()
    time_list.append(float(recset[-1][0].split(':')[-1].rstrip('ms')))

exercicio200 = mean(time_list)

resultados = [exercicio25, exercicio50, exercicio100, exercicio200]
labels = ('25.000 ~ 19Mb', '50.000 ~ 21Mb', '100.000 ~ 24,67', '200.000 ~ 33Mb')
y_pos = np.arange(len(resultados))
fig, ax = plt.subplots()
bar_container = ax.bar(labels, resultados)
ax.set(ylabel='ms', title='Testes Pre-Warm de cache com estatisticas limpas')
ax.bar_label(bar_container, fmt='{%.2f}')

plt.show()