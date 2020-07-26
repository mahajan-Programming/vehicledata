from bs4 import BeautifulSoup
import json
import requests
import pprint

with open("2wheeler.html") as html_file:
    soup = BeautifulSoup(html_file, 'html5lib')

vehicledata={
    "2wheeler":[
        {
            "hero":[
                
            ],
            "indus":[
                
            ],
            "avon":[
                
            ],
            "okinava":[
                
            ],
            "palatino":[
                
            ],
            "lohia":[
                
            ],
            "tork":[
                
            ],
            "ather":[
                
            ],
            "revolt":[
                
            ]
        }
    ]
}


dict={
    "src":"",
    "name":"",
    "range":"",
    "price":"",
    "speed":"",
    "engine power":"",
    "charging time":"",
    "button-link":""
}

for veicle in soup.find_all("div",class_="card ml-auto mr-auto"):
    src = veicle.find("img",class_="card-img-top")['src']
    name = veicle.h4.text
    range = veicle.find("div",class_="range")

    price = veicle.find("div",class_="price")
    speed= veicle.find("div",class_="speed")
    engine= veicle.find("div",class_="engine")
    time= veicle.find("div",class_="time")
    linkbutton= veicle.find("a",class_="btn btn-primary text-center")["href"]

    dict["src"]=src
    dict["name"]=name
    dict["range"]=range.text
    dict["price"]=price.txt
    dict["speed"]=speed.text
    dict["engine power"]=engine.text
    dict["charging time"]=time.text
    dict["button link"]=linkbutton
    if("Hero" in name):
        for a in vehicledata["2wheeler"]:
            a['hero'].append(dict)
    elif("Indus" in name):
        for a in vehicledata["2wheeler"]:
            a['indus'].append(dict)
    elif("Avon" in name):
        for a in vehicledata["2wheeler"]:
            a['avon'].append(dict)
    elif("Okinava" in name):
        for a in vehicledata["2wheeler"]:
            a['okinawa'].append(dict)
    elif("Palatino" in name):
        for a in vehicledata["2wheeler"]:
            a['palatino'].append(dict)
    elif("Lohia" in name):
        for a in vehicledata["2wheeler"]:
            a['lohia'].append(dict)
    elif("Tork" in name):
        for a in vehicledata["2wheeler"]:
            a['tork'].append(dict)
    elif("Ather" in name):
        for a in vehicledata["2wheeler"]:
            a['ather'].append(dict)
    else:
        for a in vehicledata["2wheeler"]:
            a['revolt'].append(dict)

pprint.pprint(vehicledata)
