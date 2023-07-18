from django.shortcuts import render, HttpResponse

import requests


# Hitting the API to get agents information
info = requests.get("https://valorant-api.com/v1/agents", params=None).json()




# Create your views here.
def home(request):
    if request.method == "POST":
        agent_name = request.POST.get('btn_name')
        
        for data in info['data']:
            if (data['displayName'] == agent_name.capitalize() and data['isPlayableCharacter']) or data['displayName'] == agent_name:
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

    else:
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
        