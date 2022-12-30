#!python
# -*- coding:utf-8 -*-
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def opt(train, opt_rate=0.1, threshold=0.015):
    """Remove outliers

    Args:
        train : pandas.Datafram
        opt_rate : 
        threshold : 

    Returns:
        AQindex

    """
    AQindex = []
    train = train
    threshold_num = threshold * len(train)
    ind = [i for i in train.columns][1:-1]

    for inx in ind:
        max = train.loc[:, inx].max()
        min = train.loc[:, inx].min()
        diff = max - min
        diffmin = min + opt_rate * diff
        diffmax = min + (1 - opt_rate) * diff
        minlist = train[train[inx] < diffmin].index.values.tolist()
        maxlist = train[train[inx] > diffmax].index.values.tolist()

        if len(minlist) <= threshold_num:
            for minindex in train[train[inx] < diffmin].index.values.tolist():
                AQindex.append(minindex)

        if len(maxlist) <= threshold_num:
            for maxindex in train[train[inx] > diffmax].index.values.tolist():
                AQindex.append(maxindex)
    AQindex = list(set(AQindex))
    AQindex = sorted(AQindex)
    return AQindex


def add_datetime_feats(data):
    """Add time features

    Args:
        data : pandas.Datafram

    Returns:
        pandas.Datafram

    """
    data['time'] = pd.to_datetime(data['time'])
    data['hour'] = data['time'].dt.hour
    data['minute'] = data['time'].dt.minute
    data['weekday'] = data['time'].dt.weekday
    data['ts'] = data['hour'] * 60 + data['minute']  # 判断是一年的第几个季度
    return data


def remove_rate(data, difference_sequence):
    """Add removal rate

    Args:
        data : pandas.Datafram
        difference_sequence : Columns to be calculated, e.g., [('COD', 'WI_COD', 'WO_COD'),(...),('AR_AN', 'WI_AN', 'AR_AN')]

    Returns:
        pandas.Datafram

    """
    for (ans, l, r) in difference_sequence:
        data['Var_' + ans] = abs(data[l] - data[r])
        data['RM_' + ans] = abs(data[l] - data[r]) / data[l]
    return data


def slide_in_timeseries(data, slide_sequence, slide_value=[2, 3, 4, 5, 10, 15, 20, 30, 60, 120]):
    """Adding rolling features to the timing sequence

    Args:
        data : pandas.Datafram
        slide_sequence : Rolled Columns
        slide_value : Rolling steps list , e.g., [2, 3, 4, 5]

    Returns:
        pandas.Datafram

    """
    for i in slide_value:
        data[[ii + f'_mean_{i}' for ii in slide_sequence]] = data[slide_sequence].rolling(i, min_periods=1).mean()
    return data


def wwtp_data_opt(f_train, f_test, difference_sequence, d_train='./after_train.xlsx', d_test='./after_test.xlsx',save_rate=0.8):
    """Test envai

    Args:
        f_train : trainset filename, string
        f_test : testset filename, string
        difference_sequence : Rolling steps list , e.g., [2, 3, 4, 5]
        d_train, d_test : processed dataset saving address
        save_rate : 

    Returns:
        (trainset, test,set), e.g., (pandas.Datafram, pandas.Datafram)

    """
    train = pd.read_excel(f_train)
    test = pd.read_excel(f_test)
    # Get the column names except time and label
    train_org_col = train.columns.tolist()[1:-2]

    optindex = opt(train, 0.1, 0.015)
    train = train.drop(index=optindex).reset_index(drop=True)

    data = pd.concat([train, test]).reset_index(drop=True)
    data = add_datetime_feats(data)

    data = remove_rate(data, difference_sequence)

    data = slide_in_timeseries(data, train_org_col)

    # Retain features of save_rate according to the variance
    pd.set_option("display.max_columns", 100)
    data = data[data.describe().T.sort_values(by="std", ascending=False, inplace=False).iloc[
                : int(len(data.columns) * save_rate)].index.tolist()]

    train = data.iloc[:train.shape[0]].reset_index(drop=True)
    test = data.iloc[train.shape[0]:].reset_index(drop=True)

    train.to_excel(d_train)
    test.to_excel(d_test)
    return d_train, d_test
