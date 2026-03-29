import pandas as pd
def prepare_inference(data):
    df = pd.DataFrame([data])
    df['YEAR_NORM'] = (df['year'] - 2011) / 15
    return df[['YEAR_NORM']].values