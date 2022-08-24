from copyreg import pickle
import pandas as pd
import pickle
def get_locations():
    df = pd.read_csv('server/static/data/clean_data.csv')
    locations = sorted( df['location'].unique() )
    return locations

def get_model():
    model = pickle.load(open('server/static/model/finalModel.pkl', 'rb'))
    return model