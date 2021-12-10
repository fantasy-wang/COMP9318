import pandas as pd

train_label = label = pd.read_csv("./data/COVID_train_labels.csv")
train_label_more_than_month = train_label[train_label['day'] > 40]


def mini(x):
    return int(x-40)
# train_label_more_than_month['day'] = train_label_more_than_month.apply(lambda x: mini(x['day']), axis=1).copy()
# print(train_label_more_than_month)
# print(type(train_label_more_than_month))



train_label_more_than_month.loc[:, 'day'] = train_label_more_than_month['day'] - 40

train_label_more_than_month.reset_index(drop=True, inplace=True)

train_label_more_than_month.to_csv("./label.csv", index=False)



