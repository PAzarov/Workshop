import json
from itertools import groupby
from operator import itemgetter

with open('data.json', 'r') as f:
    data = json.load(f)
    client_events = groupby(data['events_data'], key=itemgetter('client_id'))
    clients_dict = {k: len(list(v)) for k, v in client_events}
    most_active_clients = sorted(clients_dict.items(), key=itemgetter(1), reverse=True)
    print(most_active_clients[0])