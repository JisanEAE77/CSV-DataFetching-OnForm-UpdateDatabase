from django.http.response import JsonResponse
from django.shortcuts import render
import pandas as pd
import os
from pathlib import Path
import json
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.

def dashboard(request, *args, **kwargs):
    df1 = pd.read_csv(os.path.join(BASE_DIR, 'static/exampleFile.csv'))
    df1 = list(set(df1['Player Name'].tolist()))

    df2 = pd.read_csv(os.path.join(BASE_DIR, 'static/masterFile.csv'))
    df2 = sorted(list(set(df2['Name'].tolist())))

    context = {
        'df1': df1,
        'df2': df2,
    }
    return render(request, 'fuzzymatch/dashboard.html', context)

def getNames(request, url):
    url = str(url)
    url = url.replace('#', '\\')
    df1 = pd.read_csv(url)
    df1 = list(set(df1['Player Name'].tolist()))

    df2 = pd.read_csv(os.path.join(BASE_DIR, 'static/masterFile.csv'))
    df2 = sorted(list(set(df2['Name'].tolist())))

    context = {
        'df1': df1,
        'df2': df2,
    }

    return JsonResponse(context)


def update(request, filename, agegroup, datatype, values):
    filename = str(filename)
    filename = filename.replace('#', '/')
    agegroup = str(agegroup)
    datatype = str(datatype)
    values = values.split(',')
    print(filename, agegroup, datatype, values)
    ids = list()
    df = pd.read_csv(os.path.join(BASE_DIR, 'static/masterFile.csv'))
    df2 = list(set(df['Name'].tolist()))
    df3 = list(set(df['playerId'].tolist()))
    for e in values:
        index = df2.index(e)
        ids.append(df3[index])
    df= pd.read_csv(filename)
    tempdf = list(df['Player Name'].tolist())
    playerNames = list()
    playerIds = list()

    df1 = list(set(df['Player Name'].tolist()))
    for e in tempdf:
        index = df1.index(e)
        playerNames.append(values[index])
        playerIds.append(ids[index])
    df['ageGroup'] = agegroup
    df['dataType'] = datatype
    df['Full Name'] = playerNames
    df['playerId'] = playerIds

    print(df)

    context = {
        "update": "successful"
    }

    return JsonResponse(context)

    