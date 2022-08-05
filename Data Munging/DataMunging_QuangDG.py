import numpy as np
import pandas as pd


def weather_dat():
    df = pd.read_fwf("weather.dat")
    df_new = df[['Dy', 'MxT', 'MnT']].drop(30)
    df_new.replace('(\*)', '', regex=True, inplace=True)
    df_new = df_new.astype(int)
    df_new['diff_temp'] = pd.DataFrame(df_new['MxT'] - df_new['MnT'])
    print(df_new['diff_temp'].idxmin())
    return df_new['Dy'][df_new['diff_temp'].idxmin()]


def football_dat():
    football_data = open('football.dat', 'r')
    data = []
    for line in football_data:
        temp = line.rstrip().split()
        if '-' in temp:
            temp.pop(temp.index('-'))
        if len(temp) > 1:
            data.append(temp)

    for idx in range(1, len(data)):
        data[idx] = data[idx][1:]

    print(data[0])
    df_football = pd.DataFrame(data=data[1:], columns=[data[0]], index=range(0, len(data[1:])))
    diff = df_football['F'].astype(int).to_numpy() - df_football['A'].astype(int).to_numpy()
    df_football['diff'] = np.absolute(diff)
    return df_football.loc[df_football['diff'].idxmin()[0]].at['Team']

