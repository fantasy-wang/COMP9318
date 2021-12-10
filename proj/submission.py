import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
import math


def make_N_days_data(df, choose_features):
    elements = choose_features
    more_than_month_day = df[df['day'] > 30]['day']
    day_list = more_than_month_day.tolist()
    res = []
    for d in day_list:
        d_dict = {'day': d}
        for e in elements:
            df_e = df[list(map(lambda x: d - 30 <= x < d, df['day']))].loc[:, ['day', e]]
            for less_d in range(len(df_e['day']) - 1, -1, -1):
                print(less_d)
                e_value = int(df_e[e].iloc[29 - less_d])
                d_dict[e + '-' + str(less_d + 1)] = [e_value]
        res.append(d_dict)

    df_res = pd.DataFrame.from_dict(res[0])
    for i in range(1, len(res)):
        df_temp = pd.DataFrame.from_dict(res[i])
        df_res = df_res.append(df_temp, ignore_index=True)
    return df_res


def get_interval_data(df, weather_interval, cases_interval, choose_feature_except_daily_case):
    subset_weather = choose_feature_except_daily_case
    weather_column = [i + '-' + str(j) for i in subset_weather for j in range(weather_interval, 0, -1)]
    case_column = ['dailly_cases-' + str(i) for i in range(cases_interval, 0, -1)]
    column = [*weather_column, *case_column]
    return df[column]


## Project-Part1
def predict_COVID_part1(svm_model, train_df, train_labels_df, past_cases_interval, past_weather_interval, test_feature):
    features = ['max_temp', 'max_dew', 'max_humid', 'dailly_cases']
    feature_except_daily_cases = features[:3]
    train_df_interval = get_interval_data(make_N_days_data(train_df, features), past_weather_interval,
                                          past_cases_interval, feature_except_daily_cases)
    train_labels_df_thirty = train_labels_df[train_labels_df['day'] > 30]['dailly_cases']
    test_feature_interval = get_interval_data(test_feature, past_weather_interval, past_cases_interval,
                                              feature_except_daily_cases)
    fit = svm_model.fit(train_df_interval, train_labels_df_thirty)
    pre = fit.predict(test_feature_interval.values.reshape(1, -1))
    return math.floor(pre)


## Project-Part2
def predict_COVID_part2(train_df, train_labels_df, test_feature, weather_interval, case_interval, svm_model, features_except_daily_case):
    # features = []
    # features_except_daily_case = []
    # columns_name = train_df.columns.values.tolist()
    # if columns_name[0] == 'day':
    #     features = columns_name[1:]
    # if features[-1] == 'dailly_cases':
    #     features_except_daily_case = features[:-1]
    weather_interval = weather_interval
    case_interval = case_interval
    train_df_interval = get_interval_data(train_df, weather_interval, case_interval,
                                          features_except_daily_case)
    train_labels_df_thirty = train_labels_df[train_labels_df['day'] > 30]['dailly_cases']
    test_feature_interval = get_interval_data(test_feature, weather_interval, case_interval, features_except_daily_case)
    fit = svm_model.fit(train_df_interval, train_labels_df_thirty)
    pre = fit.predict(test_feature_interval.values.reshape(1, -1))
    return math.floor(pre)
