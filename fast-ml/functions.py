import pandas as pd


def get_missing_values(df: pd.core.frame.DataFrame) -> str:
    missing_values = df.isnull().sum()

    for idx, value in zip(missing_values.index, missing_values.values):
        if value == 0:
            missing_values.drop(idx, axis=0, inplace=True)

    if len(missing_values) > 0:
        missing_values = missing_values.to_string()
    else:
        missing_values = 'There are no missing values.'

    return missing_values


def get_columns(data: str) -> list:
    df = pd.read_csv(data)
    columns = list(df.columns)

    return columns


def get_data_overview(data: str) -> dict:
    df = pd.read_csv(data)

    shape = df.shape
    data_types = df.dtypes.to_string()
    missing_values = get_missing_values(df)
    duplicated_rows = df.duplicated().sum()

    info = {
        'shape': shape,
        'types': data_types,
        'missing': missing_values,
        'duplicated': duplicated_rows,
    }

    return info
