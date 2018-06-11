
import pickle


data = "\xe5\xbc\xa0\xe4\xb8\x89"
data_pick = pickle.dumps(data)
print(data_pick)
print(pickle.loads(data_pick))
