from flask import Flask, render_template
import plotly
import plotly.graph_objects as go
import numpy as np
from flask import *

import io  # got moved to io in python3.
import pandas as pd
import requests
import json
r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5iMe4q7srLIAow58hokKe8Zv6z5u2hCVDk191Vbt-Mp8i7N2dq3oaIiSfQUFOAfH-Z1nvPwyh3G0r/pub?output=csv')
data = r.content
virar = pd.read_csv(io.BytesIO(data), index_col = 0)
r1 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTeERMAFxcU71iZiKV2pScY1rK8OaljkAZ7boH69021Ku63CyzDqevDgTNXS32IkNrI7pkMy4v8Q3Tp/pub?output=csv')
data1 = r1.content
dadar = pd.read_csv(io.BytesIO(data1), index_col = 0)
r2 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQVwRNyaJ0Q6bpI1y7LTjLUmquz48MTrt03Y-ZDxmt-ed2BLeplW7HpGpdz22efudSaVexW9ajUiwxv/pub?output=csv')
data2 = r2.content
borivali = pd.read_csv(io.BytesIO(data2), index_col = 0)
r3 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRUT8HL1XEe4EYAjKbuKivvIrrUMd-kkn5mlgGPXrq1AtATs7Y-cu_BrucTIYS6p_tRsQd8XTzfV5r9/pub?output=csv')
data3 = r3.content
palghar = pd.read_csv(io.BytesIO(data3), index_col = 0)
r4 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRTUOWGhlLILpC93KKe86qiZhkamJ8h-9CVWhCbtc1iz7lYU-EZYx6bjKrUjsjC-iatW1j57SzZOCYc/pub?output=csv')
data4 = r4.content
vasai = pd.read_csv(io.BytesIO(data4), index_col = 0)

 
app = Flask(__name__)

@app.route('/')
def index():
    

    #suggestions
    l=['virar','dadar','borivali','palghar','vasai']
    l1=[len(virar),len(dadar),len(borivali),len(palghar),len(vasai)]
    s=l[l1.index(max(l1))]
    l2=['Palghar','Borivali','Andheri','Dadar','Vasai','Churchgate','Boisar','Saphale','Malad','Santacruz','Virar']
    pal=len(virar[virar.Destination == 'palghar'])+len(vasai[vasai.Destination == 'palghar'])+len(borivali[borivali.Destination == 'palghar'])+len(dadar[dadar.Destination == 'palghar'])
    bor=len(virar[virar.Destination == 'borivali'])+len(vasai[vasai.Destination == 'borivali'])+len(palghar[palghar.Destination == 'borivali'])+len(dadar[dadar.Destination == 'borivali'])
    andh=len(virar[virar.Destination == 'andheri'])+len(vasai[vasai.Destination == 'andheri'])+len(palghar[palghar.Destination == 'andheri'])+len(borivali[borivali.Destination == 'andheri'])+len(dadar[dadar.Destination == 'andheri'])
    dad=len(virar[virar.Destination == 'dadar'])+len(vasai[vasai.Destination == 'dadar'])+len(palghar[palghar.Destination == 'dadar'])+len(borivali[borivali.Destination == 'dadar'])
    vas=len(virar[virar.Destination == 'vasai'])+len(palghar[palghar.Destination == 'vasai'])+len(borivali[borivali.Destination == 'vasai'])+len(dadar[dadar.Destination == 'vasai'])
    chu=len(virar[virar.Destination == 'churchgate'])+len(vasai[vasai.Destination == 'churchgate'])+len(palghar[palghar.Destination == 'churchgate'])+len(borivali[borivali.Destination == 'churchgate'])+len(dadar[dadar.Destination == 'churchgate'])
    boi=len(virar[virar.Destination == 'boisar'])+len(vasai[vasai.Destination == 'boisar'])+len(palghar[palghar.Destination == 'boisar'])+len(borivali[borivali.Destination == 'boisar'])+len(dadar[dadar.Destination == 'boisar'])
    sap=len(virar[virar.Destination == 'saphale'])+len(vasai[vasai.Destination == 'saphale'])+len(palghar[palghar.Destination == 'saphale'])+len(borivali[borivali.Destination == 'saphale'])+len(dadar[dadar.Destination == 'saphale'])
    mal=len(virar[virar.Destination == 'malad'])+len(vasai[vasai.Destination == 'malad'])+len(palghar[palghar.Destination == 'malad'])+len(borivali[borivali.Destination == 'malad'])+len(dadar[dadar.Destination == 'malad'])
    san=len(virar[virar.Destination == 'santacruz'])+len(vasai[vasai.Destination == 'santacruz'])+len(palghar[palghar.Destination == 'santacruz'])+len(borivali[borivali.Destination == 'santacruz'])+len(dadar[dadar.Destination == 'santacruz'])
    vir=len(vasai[vasai.Destination == 'virar'])+len(palghar[palghar.Destination == 'virar'])+len(borivali[borivali.Destination == 'virar'])+len(dadar[dadar.Destination == 'virar'])
    l3=[pal,bor,andh,dad,vas,chu,boi,sap,mal,san,vir]
    s1=l2[l3.index(max(l3))]
    s2=l2[l3.index(min(l3))]
    a=list(virar['Date'].unique())
    b=len(a)//7
    w=len(a)
    e=w//5

    #for virar
    #number of people going from virar to outstation
    y=[len(virar[virar.Destination == 'palghar']),len(virar[virar.Destination == 'borivali']),len(virar[virar.Destination == 'andheri']),len(virar[virar.Destination == 'dadar']),len(virar[virar.Destination == 'vasai']),len(virar[virar.Destination == 'churchgate']),len(virar[virar.Destination == 'boisar']),len(virar[virar.Destination == 'saphale']),len(virar[virar.Destination == 'malad']),len(virar[virar.Destination == 'santacruz'])]
    #cost collected from people going out from virar
    y1=[len(virar[virar.Destination == 'palghar'])*15,len(virar[virar.Destination == 'borivali'])*15,len(virar[virar.Destination == 'andheri'])*20,len(virar[virar.Destination == 'dadar'])*20,len(virar[virar.Destination == 'vasai'])*5,len(virar[virar.Destination == 'churchgate'])*30,len(virar[virar.Destination == 'boisar'])*20,len(virar[virar.Destination == 'saphale'])*15,len(virar[virar.Destination == 'malad'])*25,len(virar[virar.Destination == 'santacruz'])*25]        
    #crowd based on days
    vf=virar.groupby(['Day']).count()
    y2=list(vf['Cost'])
    x=['Palghar','Borivali','Andheri','Dadar','Vasai','Churchgate','Boisar','Saphale','Malad','Santacruz']
    x1=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    stack0 =go.Pie(labels=x, values=y, name='Minimum',text=x)
    stack1 = go.Figure(go.Scatter(x=x1, y=y2,line = dict(color='royalblue', width=4, dash='solid')))
    stack1.update_layout(xaxis_title="Week Days",yaxis_title="Number of Passengers travelled",)
    stack2 =go.Figure(go.Bar(x=x,y=y1,text=y1, textposition='inside',marker=dict(color='rgb(231,107,243)', opacity=1)))
    stack2.update_layout(xaxis_title="Stations Name",yaxis_title="Amount")
    data=[stack0]
    data1=stack1
    data2=stack2
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)
    #predict_virar
    lvi=[]
    for i in range(1,8):
    	c=virar[virar["Day"]==i].Day.count()
    	c=c//b
    	lvi.append(c)
    time=['7:00','8:00','9:00','10:00','12:00','13:00','14:00','18:00','19:00','20:00']
    t=['07','08','09','10','12','13','14','18','19','20']
    time_value_virar=[]
    crowd_virar=[]
    station_virar=['palghar','borivali','andheri','dadar','vasai','churchgate','boisar','saphale','malad','santacruz']
    qvi=virar["Time"]
    qvi=qvi.str.slice(stop=2)
    qvi=np.array(qvi)
    qvi=list(qvi)
    for i in range(len(t)):
    	time_value_virar.append(qvi.count(t[i])//b)
    for i in range(len(station_virar)):
    	crowd_virar.append(virar[virar["Destination"]==station_virar[i]].Destination.count()//b)
    stack19 =go.Pie(labels=x1, values=lvi, name='Minimum',text=x1)
    stack20=go.Figure(go.Scatter(x=x, y=crowd_virar,line = dict(color='royalblue', width=4, dash='solid')))
    stack21 =go.Figure(go.Bar(x=time,y=time_value_virar, text=time_value_virar,textposition='inside', marker=dict(color='rgb(5, 245, 217)', opacity=1)))
    stack20.update_layout(yaxis_title="Number of Passengers to be Arrived",xaxis_title="Stations Name")
    stack21.update_layout(xaxis_title="Time Zone",yaxis_title="Number of Passengers to be Present")
    data19=[stack19]
    data20=stack20
    data21=stack21
    graphJSON19 = json.dumps(data19, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON20 = json.dumps(data20, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON21 = json.dumps(data21, cls=plotly.utils.PlotlyJSONEncoder)

    #for vasai road
    #number of people going from vasai to outstation
    y3=[len(vasai[vasai
    	.Destination == 'palghar']),len(vasai[vasai.Destination == 'borivali']),len(vasai[vasai.Destination == 'andheri']),len(vasai[vasai.Destination == 'dadar']),len(vasai[vasai.Destination == 'virar']),len(vasai[vasai.Destination == 'churchgate']),len(vasai[vasai.Destination == 'boisar']),len(vasai[vasai.Destination == 'saphale']),len(vasai[vasai.Destination == 'malad']),len(vasai[vasai.Destination == 'santacruz'])]
    #cost collected from people going out from vasai
    y4=[len(vasai[vasai.Destination == 'palghar'])*15,len(vasai[vasai.Destination == 'borivali'])*10,len(vasai[vasai.Destination == 'andheri'])*15,len(vasai[vasai.Destination == 'dadar'])*15,len(vasai[vasai.Destination == 'virar'])*5,len(vasai[vasai.Destination == 'churchgate'])*20,len(vasai[vasai.Destination == 'boisar'])*15,len(vasai[vasai.Destination == 'saphale'])*10,len(vasai[vasai.Destination == 'malad'])*15,len(vasai[vasai.Destination == 'santacruz'])*15]        
    #crowd based on days
    vaf=vasai.groupby(['Day']).count()
    y5=list(vaf['Cost'])
    x2=['Palghar','Borivali','Andheri','Dadar','Virar','Churchgate','Boisar','Saphale','Malad','Santacruz']
    x3=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    stack3 =go.Pie(labels=x2, values=y3, name='Minimum',text=x)
    stack4=go.Figure(go.Scatter(x=x3, y=y5,line = dict(color='#3477eb', width=4, dash='solid')))
    stack5 =go.Figure(go.Bar(x=x2,y=y4,text=y4,textposition='inside', marker=dict(color='rgb(52, 119, 235)', opacity=1)))
    stack4.update_layout(xaxis_title="Week Days",yaxis_title="Number of Passengers travelled",)
    stack5.update_layout(xaxis_title="Stations Name",yaxis_title="Amount")
    data3=[stack3]
    data4=stack4
    data5=stack5
    graphJSON3 = json.dumps(data3, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(data4, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(data5, cls=plotly.utils.PlotlyJSONEncoder)
    #predict_vasai
    lva=[]
    for i in range(1,8):
    	c=vasai[vasai["Day"]==i].Day.count()
    	c=c//b
    	lva.append(c)
    time_value_vasai=[]
    crowd_vasai=[]
    station_vasai=['palghar','borivali','andheri','dadar','virar','churchgate','boisar','saphale','malad','santacruz']
    qva=vasai["Time"]
    qva=qva.str.slice(stop=2)
    qva=np.array(qva)
    qva=list(qva)
    for i in range(len(t)):
    	time_value_vasai.append(qva.count(t[i])//b)
    for i in range(len(station_vasai)):
    	crowd_vasai.append(vasai[vasai["Destination"]==station_vasai[i]].Destination.count()//b)
    stack22 =go.Pie(labels=x1, values=lva, name='Minimum',text=x1)
    stack23=go.Figure(go.Scatter(x=station_vasai, y=crowd_vasai,line = dict(color='royalblue', width=4, dash='solid')))
    stack24 =go.Figure(go.Bar(x=time,y=time_value_vasai, text=time_value_vasai,textposition='inside', marker=dict(color='rgb(7, 242, 121)', opacity=1)))
    stack23.update_layout(yaxis_title="Number of Passengers to be Arrived",xaxis_title="Stations Name")
    stack24.update_layout(xaxis_title="Time Zone",yaxis_title="Number of Passengers to be Present")
    data22=[stack22]
    data23=stack23
    data24=stack24
    graphJSON22 = json.dumps(data22, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON23 = json.dumps(data23, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON24 = json.dumps(data24, cls=plotly.utils.PlotlyJSONEncoder)


    # for palghar
    #number of people going from palghar to outstation
    y6=[len(palghar[palghar.Destination == 'vasai']),len(palghar[palghar.Destination == 'borivali']),len(palghar[palghar.Destination == 'andheri']),len(palghar[palghar.Destination == 'dadar']),len(palghar[palghar.Destination == 'virar']),len(palghar[palghar.Destination == 'churchgate']),len(palghar[palghar.Destination == 'boisar']),len(palghar[palghar.Destination == 'saphale']),len(palghar[palghar.Destination == 'malad']),len(palghar[palghar.Destination == 'santacruz'])]
    #cost collected from people going out from palghar
    y7=[len(palghar[palghar.Destination == 'vasai'])*15,len(palghar[palghar.Destination == 'borivali'])*10,len(palghar[palghar.Destination == 'andheri'])*15,len(palghar[palghar.Destination == 'dadar'])*15,len(palghar[palghar.Destination == 'virar'])*5,len(palghar[palghar.Destination == 'churchgate'])*20,len(palghar[palghar.Destination == 'boisar'])*15,len(palghar[palghar.Destination == 'saphale'])*10,len(palghar[palghar.Destination == 'malad'])*15,len(palghar[palghar.Destination == 'santacruz'])*15]        
    #crowd based on days
    pf=palghar.groupby(['Day']).count()
    y8=list(pf['Cost'])
    x4=['Vasai','Borivali','Andheri','Dadar','Virar','Churchgate','Boisar','Saphale','Malad','Santacruz']
    x5=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    stack6 =go.Pie(labels=x4, values=y6, name='Minimum',text=x)
    stack7=go.Figure(go.Scatter(x=x5, y=y8,line = dict(color='#107a0b', width=4, dash='solid')))
    stack8 =go.Figure(go.Bar(x=x4,y=y7, text=y7,textposition='inside', marker=dict(color='rgb(28, 222, 18)', opacity=1)))
    stack7.update_layout(xaxis_title="Week Days",yaxis_title="Number of Passengers travelled",)
    stack8.update_layout(xaxis_title="Stations Name",yaxis_title="Amount")
    data6=[stack6]
    data7=stack7
    data8=stack8
    graphJSON6 = json.dumps(data6, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON7 = json.dumps(data7, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON8 = json.dumps(data8, cls=plotly.utils.PlotlyJSONEncoder)
    #predict_palghar
    lp=[]
    for i in range(1,8):
    	c=palghar[palghar["Day"]==i].Day.count()
    	c=c//b
    	lp.append(c)
    time_value_palghar=[]
    crowd_palghar=[]
    station_palghar=['vasai','borivali','andheri','dadar','virar','churchgate','boisar','saphale','malad','santacruz']
    qp=palghar["Time"]
    qp=qp.str.slice(stop=2)
    qp=np.array(qp)
    qp=list(qp)
    for i in range(len(t)):
    	time_value_palghar.append(qp.count(t[i])//b)
    for i in range(len(station_palghar)):
    	crowd_palghar.append(palghar[palghar["Destination"]==station_palghar[i]].Destination.count()//b)
    stack25 =go.Pie(labels=x1, values=lp, name='Minimum',text=x1)
    stack26=go.Figure(go.Scatter(x=station_palghar, y=crowd_palghar,line = dict(color='royalblue', width=4, dash='solid')))
    stack27 =go.Figure(go.Bar(x=time,y=time_value_palghar,text=time_value_palghar,textposition='inside', marker=dict(color='rgb(150, 7, 245)', opacity=1)))
    stack26.update_layout(yaxis_title="Number of Passengers to be Arrived",xaxis_title="Stations Name")
    stack27.update_layout(xaxis_title="Time Zone",yaxis_title="Number of Passengers to be Present")
    data25=[stack25]
    data26=stack26
    data27=stack27
    graphJSON25 = json.dumps(data25, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON26 = json.dumps(data26, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON27 = json.dumps(data27, cls=plotly.utils.PlotlyJSONEncoder)


    #for borivali stn
    #number of people going from borivali to outstation
    y9=[len(borivali[borivali.Destination == 'vasai']),len(borivali[borivali.Destination == 'palghar']),len(borivali[borivali.Destination == 'andheri']),len(borivali[borivali.Destination == 'dadar']),len(borivali[borivali.Destination == 'virar']),len(borivali[borivali.Destination == 'churchgate']),len(borivali[borivali.Destination == 'boisar']),len(borivali[borivali.Destination == 'saphale']),len(borivali[borivali.Destination == 'malad']),len(borivali[borivali.Destination == 'santacruz'])]
    #cost collected from people going out from borivali
    y10=[len(borivali[borivali.Destination == 'vasai'])*15,len(borivali[borivali.Destination == 'palghar'])*20,len(borivali[borivali.Destination == 'andheri'])*10,len(borivali[borivali.Destination == 'dadar'])*10,len(borivali[borivali.Destination == 'virar'])*10,len(borivali[borivali.Destination == 'churchgate'])*10,len(borivali[borivali.Destination == 'boisar'])*25,len(borivali[borivali.Destination == 'saphale'])*20,len(borivali[borivali.Destination == 'malad'])*10,len(borivali[borivali.Destination == 'santacruz'])*5]        
    #crowd based on days
    bf=borivali.groupby(['Day']).count()
    y11=list(bf['Cost'])
    x6=['Vasai','Palghar','Andheri','Dadar','Virar','Churchgate','Boisar','Saphale','Malad','Santacruz']
    x7=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    stack9 =go.Pie(labels=x6, values=y9, name='Minimum',text=x)
    stack10=go.Figure(go.Scatter(x=x7, y=y11,line = dict(color='#90a808', width=4, dash='solid')))
    stack11 =go.Figure(go.Bar(x=x6,y=y10, text=y10,textposition='inside', marker=dict(color='rgb(236, 240, 12)', opacity=1)))
    stack10.update_layout(xaxis_title="Week Days",yaxis_title="Number of Passengers travelled",)
    stack11.update_layout(xaxis_title="Stations Name",yaxis_title="Amount")
    data9=[stack9]
    data10=stack10
    data11=stack11
    graphJSON9 = json.dumps(data9, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON10 = json.dumps(data10, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON11 = json.dumps(data11, cls=plotly.utils.PlotlyJSONEncoder)
    #predict_borivali
    lb=[]
    for i in range(1,8):
    	c=borivali[borivali["Day"]==i].Day.count()
    	c=c//b
    	lb.append(c)
    time_value_borivali=[]
    crowd_borivali=[]
    station_borivali=['vasai','palghar','andheri','dadar','virar','churchgate','boisar','saphale','malad','santacruz']
    qb=borivali["Time"]
    qb=qb.str.slice(stop=2)
    qb=np.array(qb)
    qb=list(qb)
    for i in range(len(t)):
    	time_value_borivali.append(qb.count(t[i])//b)
    for i in range(len(station_borivali)):
    	crowd_borivali.append(borivali[borivali["Destination"]==station_borivali[i]].Destination.count()//b)
    stack28 =go.Pie(labels=x1, values=lb, name='Minimum',text=x1)
    stack29=go.Figure(go.Scatter(x=station_borivali, y=crowd_borivali,line = dict(color='royalblue', width=4, dash='solid')))
    stack30 =go.Figure(go.Bar(x=time,y=time_value_borivali, text=time_value_borivali,textposition='inside', marker=dict(color='rgb(252, 252, 8)', opacity=1)))
    stack29.update_layout(yaxis_title="Number of Passengers to be Arrived",xaxis_title="Stations Name")
    stack30.update_layout(xaxis_title="Time Zone",yaxis_title="Number of Passengers to be Present")
    data28=[stack28]
    data29=stack29
    data30=stack30
    graphJSON28 = json.dumps(data28, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON29 = json.dumps(data29, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON30 = json.dumps(data30, cls=plotly.utils.PlotlyJSONEncoder)


    #for dadar
    #number of people going from dadar to outstation
    y12=[len(dadar[dadar.Destination == 'vasai']),len(dadar[dadar.Destination == 'borivali']),len(dadar[dadar.Destination == 'andheri']),len(dadar[dadar.Destination == 'palghar']),len(dadar[dadar.Destination == 'virar']),len(dadar[dadar.Destination == 'churchgate']),len(dadar[dadar.Destination == 'boisar']),len(dadar[dadar.Destination == 'saphale']),len(dadar[dadar.Destination == 'malad']),len(dadar[dadar.Destination == 'santacruz'])]
    #cost collected from people going out from dadar
    y13=[len(dadar[dadar.Destination == 'vasai'])*15,len(dadar[dadar.Destination == 'borivali'])*10,len(dadar[dadar.Destination == 'andheri'])*10,len(dadar[dadar.Destination == 'palghar'])*20,len(dadar[dadar.Destination == 'virar'])*15,len(dadar[dadar.Destination == 'churchgate'])*10,len(dadar[dadar.Destination == 'boisar'])*25,len(dadar[dadar.Destination == 'saphale'])*25,len(dadar[dadar.Destination == 'malad'])*10,len(dadar[dadar.Destination == 'santacruz'])*5]        
    #crowd based on days
    df=dadar.groupby(['Day']).count()
    y14=list(df['Cost'])
    x8=['Vasai','Borivali','Andheri','Palghar','Virar','Churchgate','Boisar','Saphale','Malad','Santacruz']
    x9=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    stack12 =go.Pie(labels=x8, values=y12, name='Minimum',text=x)
    stack13=go.Figure(go.Scatter(x=x9, y=y14, line = dict(color='#400e10', width=4, dash='solid')))
    stack14 =go.Figure(go.Bar(x=x8,y=y13, text=y13,textposition='inside', marker=dict(color='rgb(214, 11, 21)', opacity=1)))
    stack13.update_layout(xaxis_title="Week Days",yaxis_title="Number of Passengers travelled",)
    stack14.update_layout(xaxis_title="Stations Name",yaxis_title="Amount")
    data12=[stack12]
    data13=stack13
    data14=stack14
    graphJSON12 = json.dumps(data12, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON13 = json.dumps(data13, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON14 = json.dumps(data14, cls=plotly.utils.PlotlyJSONEncoder)
    #predict_dadar
    ld=[]
    for i in range(1,8):
    	c=dadar[dadar["Day"]==i].Day.count()
    	c=c//b
    	ld.append(c)
    time_value_dadar=[]
    crowd_dadar=[]
    station_dadar=['vasai','palghar','andheri','borivali','virar','churchgate','boisar','saphale','malad','santacruz']
    qd=dadar["Time"]
    qd=qd.str.slice(stop=2)
    qd=np.array(qd)
    qd=list(qd)
    for i in range(len(t)):
    	time_value_dadar.append(qd.count(t[i])//b)
    for i in range(len(station_dadar)):
    	crowd_dadar.append(dadar[dadar["Destination"]==station_dadar[i]].Destination.count()//b)
    stack31 =go.Pie(labels=x1, values=ld, name='Minimum',text=x1)
    stack32=go.Figure(go.Scatter(x=station_dadar, y=crowd_dadar,line = dict(color='royalblue', width=4, dash='solid')))
    stack33 =go.Figure(go.Bar(x=time,y=time_value_dadar, text=time_value_dadar,textposition='inside', marker=dict(color='rgb(104, 7, 250)', opacity=1)))
    stack32.update_layout(yaxis_title="Number of Passengers to be Arrived",xaxis_title="Stations Name")
    stack33.update_layout(xaxis_title="Time Zone",yaxis_title="Number of Passengers to be Present")
    data31=[stack31]
    data32=stack32
    data33=stack33
    graphJSON31 = json.dumps(data31, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON32 = json.dumps(data32, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON33 = json.dumps(data33, cls=plotly.utils.PlotlyJSONEncoder)

    #dashboard function
    Total_virar = virar['Cost'].sum()
    Total_dadar = dadar['Cost'].sum()
    Total_borivali=borivali['Cost'].sum()
    Total_palghar=palghar['Cost'].sum()
    Total_vasai=vasai['Cost'].sum()
    y15=[Total_virar,Total_dadar,Total_vasai,Total_borivali,Total_palghar]
    date_list=virar['Date'].unique()
    date_list_count=[]
    for i in range(len(date_list)):
    	date_list_count.append(virar[virar["Date"]==date_list[i]].Date.count()+dadar[dadar["Date"]==date_list[i]].Date.count()+palghar[palghar["Date"]==date_list[i]].Date.count()+vasai[vasai["Date"]==date_list[i]].Date.count()+borivali[borivali["Date"]==date_list[i]].Date.count())
    #revenue collected by each station
    stack15 =go.Pie(labels=l, values=y15, name='Minimum',text=x)
    #total passengers travelled from particular station
    stack16=go.Figure(go.Scatter(x=l, y=l1,line = dict(color='#f58d05', width=4, dash='solid')))
    #total passengers travelled to a particular station
    stack17 =go.Figure(go.Bar(x=l2,y=l3,text=l3, textposition='inside', marker=dict(color='#f58d05', opacity=1)))
    stack18 =go.Figure(go.Bar(x=date_list,y=date_list_count,text=date_list_count, textposition='inside', marker=dict(color='rgb(245, 5, 21)', opacity=1)))
    stack16.update_layout(yaxis_title="Number of Passengers travelled from this Station",xaxis_title="Stations Name")
    stack17.update_layout(xaxis_title="Stations Name",yaxis_title="Number of Passengers travelled to this Station")
    stack18.update_layout(xaxis_title="Dates",yaxis_title="Number of Passengers travelled at this Date")
    data15=[stack15]
    data16=stack16
    data17=stack17
    data18=stack18
    graphJSON15 = json.dumps(data15, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON16 = json.dumps(data16, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON17 = json.dumps(data17, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON18 = json.dumps(data18, cls=plotly.utils.PlotlyJSONEncoder)
    #predict_dashboard
    next_day=[len(virar)//w,len(dadar)//w,len(borivali)//w,len(palghar)//w,len(vasai)//w]
    time_value_dashboard=[]
    for i in range(len(t)):
    	time_value_dashboard.append((time_value_virar[i]+time_value_dadar[i]+time_value_borivali[i]+time_value_palghar[i]+time_value_vasai[i])//5)
    lda=[]
    for i in range(len(lvi)):
    	c=lvi[i]+lva[i]+lp[i]+lb[i]+ld[i]
    	lda.append(c)
    station_dashboard=[]
    for i in l3:
    	station_dashboard.append(i//e)
    #next day prediction
    stack34 =go.Pie(labels=l, values=next_day, name='Minimum',text=l)
    #weekdays prediction
    stack35=go.Figure(go.Scatter(x=x1, y=lda, name='Low 2007',line = dict(color='#f58d05', width=4, dash='solid')))
    #time series graph prediction
    stack36 =go.Figure(go.Bar(x=time,y=time_value_dashboard,text=time_value_dashboard, textposition='inside', marker=dict(color='#f58d05', opacity=1)))
    stack37 =go.Figure(go.Bar(x=l2,y=station_dashboard,text=station_dashboard, textposition='inside', marker=dict(color='rgb(245, 5, 21)', opacity=1)))
    stack35.update_layout(yaxis_title="Number of Passengers Will be Travelling Next Week",xaxis_title="Week Days")
    stack36.update_layout(xaxis_title="Time Zone",yaxis_title="Number of Passengers will be present at this time.")
    stack37.update_layout(xaxis_title="Station Name",yaxis_title="Number of Passengers will Arrived.")
    data34=[stack34]
    data35=stack35
    data36=stack36
    data37=stack37
    graphJSON34 = json.dumps(data34, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON35 = json.dumps(data35, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON36 = json.dumps(data36, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON37 = json.dumps(data37, cls=plotly.utils.PlotlyJSONEncoder)


    o=time_value_dashboard.index(max(time_value_dashboard))
    o=time[o]
    p=time_value_dashboard.index(min(time_value_dashboard))
    p=time[p]


    return render_template('index.html', plot=graphJSON,plot1=graphJSON1,plot2=graphJSON2,plot3=graphJSON3,plot4=graphJSON4,plot5=graphJSON5,plot6=graphJSON6,plot7=graphJSON7,plot8=graphJSON8,plot9=graphJSON9,plot10=graphJSON10,plot11=graphJSON11,plot12=graphJSON12,plot13=graphJSON13,plot14=graphJSON14,s=s,s1=s1,s2=s2,plot15=graphJSON15,plot16=graphJSON16,plot17=graphJSON17,plot18=graphJSON18,plot19=graphJSON19,plot20=graphJSON20,plot21=graphJSON21,plot22=graphJSON22,plot23=graphJSON23,plot24=graphJSON24,plot25=graphJSON25,plot26=graphJSON26,plot27=graphJSON27,plot28=graphJSON28,plot29=graphJSON29,plot30=graphJSON30,plot31=graphJSON31,plot32=graphJSON32,plot33=graphJSON33,plot34=graphJSON34,plot35=graphJSON35,plot36=graphJSON36,plot37=graphJSON37,o=o,p=p)

#main function
if __name__ == '__main__':
    app.run()