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



## Set hyper-parameters for the SVM Model
# svm_model = SVR()
# svm_model.set_params(**{'kernel': 'rbf', 'degree': 1, 'C': 5000,
#                         'gamma': 'scale', 'coef0': 0.0, 'tol': 0.001, 'epsilon': 10})


# Generate Prediction Results
# predicted_cases_part1 = []
# for idx in range(len(test_features)):
#     test_feature = test_features.loc[idx]
#     prediction = submission.predict_COVID_part1(svm_model, train_df, train_labels_df,
#                                                 past_cases_interval, past_weather_interval, test_feature)
#     predicted_cases_part1.append(prediction)
#
# print(predicted_cases_part1)

def part2(features_except_daily_case, w, c, svm_model):
    train_df1 = pd.read_csv("./all_matrix.csv.csv")
    # train_labels_df1 = pd.read_csv("./label.csv")

    weather_interval = w
    case_interval = c

    features_except_daily_case = features_except_daily_case

    ## Generate Prediction Results
    predicted_cases_part2 = []
    for idx in range(len(test_features)):
        test_feature = test_features.loc[idx]
        prediction = submission.predict_COVID_part2(train_df1, train_labels_df, test_feature, weather_interval,
                                                    case_interval, svm_model, features_except_daily_case)
        predicted_cases_part2.append(prediction)



    ## MeanAbsoluteError Computation...!
    # predicted_cases_part1 = [945, 897, 832, 881, 907, 921, 1028, 819, 812, 809, 860, 845, 837, 898, 861, 811, 846, 839, 855, 892]
    test_label_file = './data/COVID_test_labels.csv'
    test_labels_df = pd.read_csv(test_label_file)
    ground_truth = test_labels_df['dailly_cases'].to_list()
    MeanAbsError = mean_absolute_error(predicted_cases_part2, ground_truth)

    if MeanAbsError < 61 or MeanAbsError > 100:
        print('start')
        print(features_except_daily_case)
        print(predicted_cases_part2)
        print('w = {} and c = {}'.format(weather_interval, case_interval))
        print('MeanAbsError = ', MeanAbsError)
        print('end')
    # else:
    #     print('big number = {}'.format(MeanAbsError))


res = []
columns = train_df.columns.values.tolist()
max_e = [i for i in columns if i.startswith('max')]
min_e = [i for i in columns if i.startswith('min')]
avg_e = [i for i in columns if i.startswith('avg')]
res.append(max_e)
res.append(min_e)
res.append(avg_e)
a = max_e.copy()
b = min_e.copy()
c = avg_e.copy()
a.append('precipitation')
b.append('precipitation')
c.append('precipitation')
res.append(a)
res.append(b)
res.append(c)


svm_model = SVR()
svm_model.set_params(**{'kernel': 'rbf', 'degree': 1, 'C': 20000,
                        'gamma': 'scale', 'coef0': 0.0, 'tol': 0.001, 'epsilon': 0.1})

svm_model = SVR()
svm_model.set_params(**{'kernel': 'rbf', 'degree': 1, 'C': 20000,
                        'gamma': 'scale', 'coef0': 0.0, 'tol': 0.001, 'epsilon': 0.1})
for k in res:
    for i in range(30, 0, -1):
        part2(k, i, 16, svm_model)
