import pandas as pd


def get_data_overview(data):
    df = pd.read_csv(data)

    shape = df.shape
    missing_values = df.isnull().sum()

    for idx, value in zip(missing_values.index, missing_values.values):
        if value == 0:
            missing_values.drop(idx, axis=0, inplace=True)

    if len(missing_values) > 0:
        missing_values = missing_values.to_string()
    else:
        missing_values = 'There are no missing values.'

    info = [
        shape,
        missing_values,
    ]

    return info