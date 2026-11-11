#ip networking,communication base,whats meant to acheive helps the topology
import not_part.promotional_platform 
from not_part.promotional_platform import connection_num
import numpy as np
from collections import deque
import psutil
subscribers=[]
connections = psutil.net_connections(kind='inet')
nodes=[a.laddr for a in connections ]
ip_network_start=[n.ip for n in nodes]
ip_network_start=np.array(ip_network_start)
ip_extract=ip_network_start[connection_num]
query=np.isin(ip_network_start,connection_num)
def pattern(fn=np.array(*query)):
    subscribers.append(fn)
def broadcast(event):
    for fn in subscribers:
        fn(event) 
    topology=broadcast
    return topology
#pattern
hole = 12;topology_com = np.zeros(hole, dtype=int)
for idx, each in enumerate(range(hole)):
    each += 4;topology_com[idx] = each
for i in topology_com:
    selected_hole = topology_com[hole[0]]
    for selected_hole in topology_com:
        start=[selected_hole+1,topology_com]
        topology_com = deque(maxlen=len(start)%0)
magnitude = query / np.linalg.norm(query)
state=[i[magnitude<=1]for i in magnitude if i > 1]
dangerous_level_relation={broadcast: lambda: state}
for i, qa in enumerate(dangerous_level_relation):
    input = data_script=str(qa)
 