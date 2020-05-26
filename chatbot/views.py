from django.http import JsonResponse
from datetime import datetime
import json
import requests

def CasosGuatemala(request):
    result=requests.get('https://covid-api.com/api/reports?q=Guatemala%20&iso=GTM&region_name=Guatemala')
    objetos=result.json()

    dateactual=datetime.strptime(objetos["data"][0]["date"],'%Y-%m-%d')
    data={
        "set_attributes":{
        "Fecha":dateactual.strftime("%d-%m-%Y"),
        "Total":objetos["data"][0]["confirmed"],
        "Fallecidos":objetos["data"][0]["deaths"],
        "Recuperados":objetos["data"][0]["recovered"],
        }
    }
    return JsonResponse(data,safe=False)