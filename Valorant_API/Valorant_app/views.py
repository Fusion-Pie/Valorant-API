from django.shortcuts import render, HttpResponse

import requests


# Hitting the API to get agents information
agent_endpoint = requests.get("https://valorant-api.com/v1/agents", params=None).json()


# Create your views here.
def home(request):
    if request.method == "POST":
        agent_name = request.POST.get('btn_name')
        
        context = getAgentInfo(agent_name)
        
        context['agentList'] = getAgentsName()

        return render(request, 'index.html', context=context)

    else:
        # It is for the first time when the page gets loaded
        context = getAgentInfo("Brimstone")
        
        context['agentList'] = getAgentsName()

        return render(request, 'index.html', context=context)
        

# Function to get agent information
def getAgentInfo(agentName):
    for data in agent_endpoint['data']:
        # isPlayableCharacter is used as the api has two sova's one is playable and another is not
        if (data['displayName'] == agentName and data['isPlayableCharacter']):
            context = {
                'uuid': data['uuid'],
                'displayName': data['displayName'],
                'desc': data['description'],
                'displayIcon': data['displayIcon'], 
                'bg': data['background'],
                'fullPortraitV2': data['fullPortraitV2'],
                'role': data['role']['displayName']
            }

    return context


# Function to get all agents name
def getAgentsName():
    agentList = []
    for agent in agent_endpoint['data']:
        if agent['isPlayableCharacter']:
            agentList.append(agent['displayName'])

    return agentList