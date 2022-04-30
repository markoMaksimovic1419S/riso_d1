from email.headerregistry import ContentTypeHeader
import requests
import json

list_of_requests = [
    {"ime": "Nikola","prezime": "Nikolic","username": "nikolic_nikola","smer": "RI","predmeti":[{"ime": "ri1", "espb": "5"},{"ime": "r2", "espb": "1"},{"ime": "r3", "espb": "1"}]},
    {"ime": "Marko","prezime": "Markovic","username": "markovic_marko","smer": "IT","predmeti":[{"ime": "it1", "espb": "4"}]},
    {"ime": "Ilija","prezime": "Ilic","username": "ilic_ilija","smer": "RN","predmeti":[{"ime": "rn1", "espb": "6"},{"ime": "rn2", "espb": "4"}]},
]
endpoint = "http://192.168.1.5:8081/users"

print("Sending")
for one_request in list_of_requests:
    requests.post(endpoint, json=one_request)

print("Done, sent %s requests"%len(list_of_requests))


