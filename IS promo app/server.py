#The Flask script injects events into shared module state, which directly
#  reshapes how associative propagation spreads influence.
from flask import Flask, render_template, url_for, request, jsonify, redirect, session,g
import pandas as pd
import numpy as np
import os, csv, sqlite3, time, json, threading,ssl,subprocess,copy,sys
import communication_base as communication_base, ID_customisation as ID_customisation, deployment_model, not_part.serveradminfix as serveradminfix,not_part.promotional_platform as promotional_platform
from deployment_model import query
# System Modules
# Rent a server.
# Get a public IP.
# Point a domain name to that IP.
# Install an SSL certificate.
# Serve your application over HTTPS
# ssl.get_default_verify_paths()
# context = ssl.create_default_context()
# hosting_service = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# hosting_service.load_cert_chain(certfile="server.crt",keyfile="server.key")
# print('starttttttttttttttttttttttt')
# surpport_sys = communication_base
# data_deployment = ID_customisation

# interface_design = serveradminfix
# highest=serveradminfix.rec_test
# operation=promotional_platform
print('doneeeeeeeeeeeeeeeeee')
ever_running=subprocess.Popen(["python", "event_routing"],stdout=open("app.log", "w"),
                        stderr=subprocess.STDOUT,start_new_session=True)
information = []#memory
def data_info():
    for mod in [query()]:
        state = getattr(sys.modules[__name__], mod)()
        state = mod.export_state()
        if state is not None:
            information.append(state)
    return information

app = Flask(__name__)
app.secret_key = "your_secret_key"

#admin, UI block
class shared_module_propagation:
    def __init__(self):
        self.phonebook = {}
    def route(self, app, path, **options):
        def decorator(func):
            app.route(path, **options)(func)
            self.phonebook[path] = func
            return func
        return decorator
    def smp(self,*routes):
        route_creation = any(filter(None, routes))
        route_creation_access = [g for i in [route_creation] if i]
        return route_creation_access
propagation = shared_module_propagation()
smp=propagation.smp
@app.before_request
def lookups():
    g.smp = propagation.smp
    route_availability={g.smp:lambda:request.path}
    g.paths=route_availability[g.smp]()
data_pattern={}    
def send_to_admin( data_id):
    global data_pattern
    if data_id in data_pattern:
        return data_pattern[data_id]
    data_pattern = copy.deepcopy(propagation)
    query.receive(data_pattern)
@app.before_request
def sync_state():#beginning state
    g.system_state = data_info()
@propagation.route(app,"/url_navigation/<memory>", methods=['GET', 'POST'])
def user(memory):
    try:
        users = pd.DataFrame()
        if request.method == "POST":
            username = request.form.get('username')
            password = request.form.get('password')
            if username and password:
                users[username] = [password]
                if users[username].notna().any():
                    page = request.form.get("memory")
                    if page:
                        information[memory] = { "network": page.strip()}
                        return redirect(url_for({ "user",query.user_memory(information[memory])}))

    except Exception as e:
        print(e)    

    return render_template("UI2.html", memory=memory)
# @propagation.route(app,'/communication', methods=['GET', 'POST'])
# def coms():
#     #if request.method == 'GET':
#     if information[0] not in session:
#         session[information[0]] = []
#     if request.method == 'POST':
#         user_text = request.json.get('chat','')
#         if user_text :
#             stored = session[information[0]]
#             stored.append(user_text)
#             session[information[0]] = stored
#     user_data_storage = session[information[0]]
#     data_info(user_data_storage).append({"key": serveradminfix.rec_test(),
#                                   "message": information})=information
#     if serveradminfix.rec_test(user_data_storage):
#         print(user_data_storage)
#     return render_template('UI.html', messages=user_data_storage)
# session.modified = True
# @propagation.route(app,'/networking',methods=['GET','POST'])
# def connection():
#     get_network=[]
#     g.system_state = data_info()
#     query=np.isin(information,user)
#     get_network[query]
#     net = data.copy()
#     net["users"].append(get_network)
#     receive(net)
#     Behaviour={net:lambda:query}    
#     return jsonify({"status": "connection done"})
# #create server through url and wrap it with navigation and store the data
# @propagation.route(app,'/server/<data>',methods=['GET','POST'])
# def control(data_center=user):
#     info=user(data_center)
#     server = data.copy()
#     server["users"].append(info)
#     receive(server)
#     return jsonify({"status": "connection done"})
# #using py to crud query in csv from github

# @propagation.route(app,'/positionings')
# def productivity(i):
#     data=f"/url_navigation?message={i}"
#     if user==True:
#         which={user:lambda:data}
#     data_id=[list(which.values()).index(loc) for loc in which.values()]
#     data_for_admin = data.copy()
#     data_for_admin["users"].append(data_id)
#     receive(data_for_admin)
#     return jsonify({"status": "connection done"})
# #server recieves data from admin reflects it here
# @propagation.route(app,'/data_center')
# def data_to_service():
#     payload = request.json
#     state=propagation.deep_copy
#     data_center(state)
#     return
# #this potentially runs the affairs

 
if __name__=='__main__':
    app.run(debug=True)



    #make the routes more of trriger panels like controllables 