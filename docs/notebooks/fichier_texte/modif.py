import json


with open("rep1.txt","rt",encoding="utf8") as rf:
    repertoire1 = json.load(rf)

rep3={}
for val in repertoire1:
    nom=val['first name']
    rep3[nom]={'nom':val['last name'],'telephone':val['phone'],'email':val['mail']}


print(rep3)