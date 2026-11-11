
# import numpy as np
# import pandas as pd
# import importlib
# from sklearn.linear_model import SGDRegressor
# import network_buildup.communication_base as communication_base, network_buildup.ID_customisation as ID_customisation, deployment_model,serveradminfix
# import sqlite3,json
# from difflib import SequenceMatcher
# def circular(ref):
#     return ref
# def complacency(productivity):
#     return productivity
# def refrencence(adapt):
#     return adapt
# stored_reactions = {}
# def application(reactions):
#     global stored_reactions
#     stored_reactions = reactions
#     return reactions
# def data_arr(data_script):
#     return data_script
# def placeholder(datas=None,datas1=None):
#     json.dump(datas,datas1)
#     datas=pd.json_normalize()
#     datas1=pd.json_normalize()
#     return pd.DataFrame(datas,datas1)
# def UI(page_counts):
#     pd.DataFrame(dir(page_counts))
# check1 =[]
# comparation=[]
# similarity_score=[]
# def server_network():
#     module_name = "communication_base"
#     network = importlib.import_module(module_name)
#     attr = dir(network)   
#     array_attr = np.array(attr)
#     X = np.array([[len(name)] for name in array_attr])
#     y = np.arange(len(array_attr))
#     pattern = SGDRegressor()
#     pattern.partial_fit(X, y)
#     predictions = pattern.predict(X)
#     reactions = {}
#     for coms, connection in zip(array_attr, predictions):
#         reactions[coms] = float(connection)
#     module2_name = "ID_customisation"
#     network2 = importlib.import_module(module2_name)
#     br_attr = dir(network2)
#     check1 = np.array(list(reactions.items()), dtype=object)
#     br_attr_array = [item for item in check1[:,0] if item in br_attr]
#     for a in check1[:,0]:
#         for b in br_attr_array:
#             similarity_score = SequenceMatcher(None, a, b).ratio()
#     for ID_cst, connection1 in zip(check1, br_attr_array):
#         reactions[tuple(ID_cst)] = connection1
#     storage = pd.DataFrame({"module": ["relation_sys", "similarity_sys"],"reaction": [reactions[coms], reactions[tuple(ID_cst)]]})
#     # 1. Connect to SQLite database (creates file if not exists)
#     conn = sqlite3.connect("networks.db")
#     # 2. Save dataframe into table
#     storage.to_sql("reactions", conn, if_exists="replace", index=False)
#     # 3. Read it back
#     df_back = pd.read_sql("SELECT * FROM reactions", conn)
#     #print(df_back)
#     learning=dir(df_back)
#     module3_name = "deployment_model"
#     network3 = importlib.import_module(module3_name)
#     credit=dir(network3)
#     learning_array = df_back.columns.to_numpy()
#     comparation = [item for item in learning_array if item in credit]
#     for ID_dev, connection3 in zip(learning_array, comparation):
#         reactions[ID_dev] = connection3
#     #Build a learning routine that compares new concepts with the
#     #network’s self-detected state, read behaviour to expands knowledge, and refines it
#     #  by context (location) compareing network to ref, serving as a push to understand behaviour
#         looks=dir(serveradminfix.refrencence)
#         concept = pd.DataFrame({"looks": looks})
#         page= {
#         "lagos": "lagos.html",
#         "abuja": "abuja.html",
#         "kano": "kano.html"
#     }
#         def learn(con_structure,location):
#             conceptual=[]
#             if con_structure not in concept.columns:
#                 t=concept.loc[:,looks]#recommend location
#                 conceptual.extend(t.tolist())
#                 idx = t[t == location]
#                 if len(idx) > 0:
#                     conceptual.sort()
#                     print(location)
#                     for s,e in enumerate(idx):
#                         print(s, sum(e.values()))
#                         pattern=e/idx
                    
#                     start = 0
#                     stop = min(int(pattern * len(idx)), len(idx)) 
#                     selected_learns = idx[start:stop]
#                     highest_prob = max(selected_learns)
#                     if location not in page:
#                     # return render_template(page[location]) 
                
#                     #print("Location:", location, "| Best so far:", page[location])
#     #The values the network produces.
#     #How those values change over time.
#     #And how they relate to the stimulus (input).

#     #Your addition allows the network to selectively read behavior in chunks, 
#     #which makes it possible to detect phases, shifts, or local anomalies 
#     # instead of treating behavior as one long stream.
#                         return highest_prob
#         if isinstance(comparation, list) and isinstance(serveradminfix.learning, (list, np.ndarray)):
#             affected = [k for k, v in serveradminfix.reactions.items() if v == serveradminfix.complacency]

#         if len(affected)>=2:
#             # last two references
#             init, old = affected[-1], affected[-2]
#             pattern_check = (init, old)

#             problem = None
#             if init != old:
#                 problem = "faulty"

#             security = list(ID_customisation.connect.values())[-1]
#             state = f"{security}_{problem}"  # combined state

#             broken_parts = []
#             secure_links = []

#             for reference in affected:
#                 # check falsy state
#                 if not state or state.endswith("None"):
#                     broken_parts.append((security, reference, "falsy_state"))
#                     print(f"⚠️ Test failed: {security} has falsy state at {reference}")
#                     continue

#                 # equality test
#                 if security == reference:
#                     secure_links.append((security, reference))
#                     print(f"✅ Secure link: {security} equals {reference} (truthy)")
#                 else:
#                     broken_parts.append((security, reference, "not_equal"))
#                     print(f"❌ Broken link: {security} does not equal {reference}")

#                 print(f"{security} references {reference} like this {state}")

#             print("Broken parts:", broken_parts)
#             print("Secure links:", secure_links)
# server_network()
# module_df=pd.DataFrame({'a':dir(communication_base),'b':dir(ID_customisation),'c':dir(deployment_model)})
# attribute=pd.DataFrame()
# def controllable(control, target="communication"):
#     global attribute
#     if target == "communication":
#         attribute=module_df['a'].apply(control).tolist()
#         return attribute
#     elif target == "customisation":
#         attribute=module_df['b'].apply(control).tolist()
#         return attribute
#     elif target == "deployment":
#         attribute=module_df['c'].apply(control).tolist()
#         return attribute
#     else:
#         return f"No matching module for target={target}"
# values = {name: getattr(attribute, name) for name in dir(attribute)}
# print(values)
# looks=dir(serveradminfix.refrencence)
# transfered_learning=[]
# def rec_test(query,rec):
#     global values,attribute,transfered_learning
#     # filter the values of the attributes of this module using rec
#     results={}
#     columns = [attr for attr in values if rec(attr)]
#     coms=module_df[looks] == columns
#     #Compares each value in Series/DataFrame to columns,creating coms
#     if columns:
#         matches = pd.concat([
#             module_df['a'][module_df['a'].isin(columns)],
#             module_df['b'][module_df['b'].isin(columns)],
#             module_df['c'][module_df['c'].isin(columns)]
#         ])
#         top_attr = matches.value_counts().idxmax()
#         if not coms.empty:
#                     print(columns)
#                     for s,e in coms.iterrows():
#                         print(s, sum(e.sum()))
#                         pattern=e/e.sum()#rec patterns
#         row = module_df[
#             (module_df['a'] == top_attr) |
#             (module_df['b'] == top_attr) |
#             (module_df['c'] == top_attr)
#         ].iloc[0]
#         results[query] = row.to_dict()
#         start = 0
#         stop = min(int(pattern * len(coms)), len(coms)) 
#         selected_learns = coms[start:stop]
#         highest_prob = max(selected_learns)
#         data_management = {
#         "collected": module_df[pattern],          # actual data subset
#         "organized": sorted(module_df[pattern]),  # optional organization step
#         "quality_checked": [v for v in module_df[pattern] if v is not None],
#         "storage_count": len(pattern),    # lifecycle/statistics
#         "access_rules": "restricted",             # governance/security placeholder
#         }
#         print(transfered_learning[coms])
#         print(transfered_learning[pattern])
#         print(transfered_learning[data_management])
#         return highest_prob
# def admin_validate(new_data):
#         if not isinstance(new_data, (list, np.ndarray, dict)):
#             return False
#         if len(new_data) == 0:
#             return False
#         return True
# def admin_drift_control(old_value, new_value, tolerance=5):
#     return abs(new_value - old_value) <= tolerance
# def admin_normalize(count_dict):
#     total = sum(count_dict.values())
#     if total == 0:
#         return count_dict
#     return {k: v / total for k, v in count_dict.items()}
# def admin_log(previous, updated):
#     return {
#         "previous": previous,
#         "updated": updated
#     }
# def admin_governance(*ref):
#     return  pd.read_json('values.json',orient='index')

#     #create under standin thr data managment 
#     #a setup to behaviour of data
#     # check the changes
