from django.shortcuts import render, HttpResponse

import requests

# Create your views here.
def home(request):
    info = requests.get("https://valorant-api.com/v1/agents", params=None).json()

    for data in info['data']:
        if data['displayName'] == "Brimstone":
            context = {
                'uuid': data['uuid'],
                'displayName': data['displayName'],
                'desc': data['description'],
                'displayIcon': data['displayIcon'], 
                'bg': data['background'],
                'fullPortraitV2': data['fullPortraitV2'],
                'role': data['role']['displayName']
            }

    return render(request, 'index.html', context=context)
            
    # e370fa57-4757-3604-3648-499e1f642d3f