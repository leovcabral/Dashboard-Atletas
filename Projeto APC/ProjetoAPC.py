import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

df=pd.read_csv('DadosBase.csv')
aux_data=df.values.tolist()

nome=[]
ganhos=[]
coluna_ano= 6
coluna_nome = 1
coluna_ganhos = 7

ano = int(input('Qual ano você quer visualizar?'))
for x in list(range(len(aux_data))):
    if aux_data[x][coluna_ano] == ano:
        nome.append(aux_data[x][coluna_nome])
        ganhos.append(aux_data[x][coluna_ganhos])

data = [go.Bar(x=nome, y=ganhos, marker ={'color' : 'darkgreen', 'line': {'color':'black', 'width':2}},opacity = 0.8)]

layout = go.Layout(title = 'Ganhos por atleta no ano')
fig = go.Figure(data=data, layout=layout)
fig.show()

