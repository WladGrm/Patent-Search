from sentence_transformers import SentenceTransformer
import pickle
import faiss
import numpy as np
import pandas as pd
from model_utils import *
#Loading params
config = get_config("model_config.yaml")

#Getting index
with open(config["path_to_pickle"], 'rb') as f:
    index = pickle.load(f)
index = faiss.deserialize_index(index)

utils = Utils()


class SemanticSearch:
    def __init__(self):
        self.model = utils.get_model_for_search(config['model_path_for_search'])
        self.df = pd.read_csv(config['path_to_csv'])
        self.index = index

    def indx(self, I):
        I = I.flatten().tolist()
        return [self.df.loc[self.df.numeric_value == idx].to_dict(orient='records') for idx in I]

    def s_v(self, query, index, num_results=10):
        vector = self.model.encode(list(query))
        D, I = index.search(np.array(vector).astype("float32"), k=num_results)
        return D, I
