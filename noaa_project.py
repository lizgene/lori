#!/usr/bin/env python
# coding: utf-8

# In[1]:


us_state_abbrev = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    'IA/IL': 'Iowa, Illinois',}
import requests
from bs4 import BeautifulSoup
URL = 'https://www.weather.gov/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', id = (['wwaleft','wwaright','wwacenter_l','wwacenter_r']))
URLSlist = []
for result in results:
    for a in BeautifulSoup(str(result)).findAll('a', href=True):
        URLS = a
        URLSfixed = "https:" + str(a).replace(' ', '%20').replace('amp;', '').replace('<a%20href="', '').replace('</a>', '')
        URLSfixedgood= str(URLSfixed).split('"',1)
        URLgood= URLSfixedgood[0]
        URLSlist.append(URLgood)
        #print(URLgood)
        #print('---')
     #print("------------------------------------------------")
#print(URLSlist)

for item in URLSlist:

    page = requests.get(item)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    states = []
    for pre in soup.find_all('pre'):

        lines = BeautifulSoup(str(pre)).prettify().split('\n')
        liness= lines[3].split(' ')[-1]
        states.append(liness)
        singlestates = set(states)
    #print(singlestates)

    for h3 in soup.find('h3'):
        alert = str(h3)
        #print(alert)
    '''Convert abbreviation to State name'''

    tacos = []

    for state in singlestates:
        #print(state)
        if state in us_state_abbrev.keys():
            #print(state)
            #print(us_state_abbrev[state])
            #print("---")
            tacos.append(us_state_abbrev[state])
        elif state in us_state_abbrev.values():
            #print(state)
            tacos.append(state)
        else:
            #print("No State")
            tacos.append('No State')
        #print("---")



    #print(commas_added)
    for taco in tacos:

        manytacos = "A " + alert + " is in effect for parts of " + ", ".join((tacos)) + "."


    print(str(manytacos))
