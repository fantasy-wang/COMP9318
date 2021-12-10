import submission
import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
import submission

## Parameters settings
past_cases_interval = 10
past_weather_interval = 10


## Read training data
train_file = './data/COVID_train_data.csv'
train_df = pd.read_csv(train_file)

## Read Training labels
train_label_file = './data/COVID_train_labels.csv'
train_labels_df = pd.read_csv(train_label_file)


## Read testing Features
test_fea_file = './data/test_features.csv'
test_features = pd.read_csv(test_fea_file)


def make_N_days_data(df, choose_features):
    elements = choose_features
    more_than_month_day = df[df['day'] > 30]['day']
    day_list = more_than_month_day.tolist()
    res = []
    for d in day_list:
        d_dict = {'day': d}
        for e in elements:
            df_e = df[list(map(lambda x: d - 30 <= x < d, df['day']))].loc[:, ['day', e]]
            print(df_e)
            for less_d in range(len(df_e['day']) - 1, -1, -1):

                e_value = int(df_e[e].iloc[29 - less_d])
                d_dict[e + '-' + str(less_d + 1)] = [e_value]
        res.append(d_dict)

    df_res = pd.DataFrame.from_dict(res[0])
    for i in range(1, len(res)):
        df_temp = pd.DataFrame.from_dict(res[i])
        df_res = df_res.append(df_temp, ignore_index=True)
    return df_res

def mini(x):
    return int(x-40)

df_dailly_case = train_df[train_df['day'] > 40]
df_dailly_case['day'] = df_dailly_case.apply(lambda x: mini(x['day']), axis=1)
features = []
columns_name = train_df.columns.values.tolist()
if columns_name[0] == 'day':
    features = columns_name[1:]
a = make_N_days_data(df_dailly_case, features)
a.to_csv('./case_more_m.csv', index=False)



