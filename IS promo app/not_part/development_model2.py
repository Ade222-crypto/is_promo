import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import not_part.promotional_platform as promotional_platform,network_base.production_perspective as production_perspective
from sklearn.metrics.pairwise import cosine_similarity
from not_part.promotional_platform import access,con_len
import numpy as np
system2=[]
system2=(dir(promotional_platform))
query=[]
location_app=[]
if system2:
    query.append(system2)
elif production_perspective():
    obj = getattr(promotional_platform, access)
    obj=pd.DataFrame(obj)
    location =  obj[obj].isin(query)
    location_app.append(location)
influence = TfidfVectorizer()
net_formation = influence.fit_transform( system2)
similarity_scores = cosine_similarity(net_formation)
loc_query = pd.Series(system2).isin(influence.get_feature_names_out())
data={}
df1 = iter(pd.DataFrame({},axis=1))
for i in df1:
    if loc_query.isin(location).any():
        if loc_query.ndim==0:
            array_perspective = np.array([loc_query.item()])
    data[i]=next(array_perspective)
refactored_net = pd.Series(data)[loc_query].tolist()
understood_data0 = df1[df1['system1'].isin(refactored_net)]
for art,names in enumerate(data):
    data[art]=isinstance(con_len,type(con_len)) and isinstance(refactored_net,list)
#to create AME, a reccomender system is needed
#perspective connection will acknowlegde AME
#net algorithm will serve a behavioural purpose to AME

#the algo of ai + net will serve promotion then need to be strategic about accepting AME
def perpective_recommend(n_input):
    global con_len,array_perspective
    find=refactored_net.index(net_formation)#Location lookup
    change=similarity_scores[find]#Embedding change
    relatable_idx = np.argsort(change)[::-1] # ordering
    data=relatable_idx[1:n_input+1]
    data_storage=data.tolist()
    for math_recognize in range(len(data_storage)):
        index=data_storage[math_recognize]
        vec = np.array(index, dtype=float)
        norm_vec = vec / np.linalg.norm(vec)
        relationship= np.corrcoef(norm_vec.reshape(-1, 1))#relationship
    math_recognize=relationship[n_input]#there has to be an intake informing relationship
    AI_recognition= pd.Series(data_storage)[math_recognize]
    ai_filter = pd.Series(AI_recognition)[con_len]
    behaviour=list(ai_filter)
    index=similarity_scores[ai_filter]
    position=list(zip(data_storage,index))
    AME_ordering=relatable_idx[position]
    m_sim_score=sorted(AME_ordering,key=lambda x:x[1],reverse=True)
    reccomendations=[]
    activation = np.zeros(len(similarity_scores))
    weight = similarity_scores
    for movie_id,_ in m_sim_score[:n_input+1]:
        sorting=m_sim_score.index(np.absolute(movie_id))[ai_filter][0]
        if np.where(sorting != array_perspective):
            neighbors = np.nonzero(weight[ai_filter])[0].itemsize
            for neighbor in neighbors:
               activation[neighbor] += m_sim_score * weight[ai_filter, neighbor]
            reccomendations.append(sorting)
            location_app.extend(reccomendations)
    return reccomendations
