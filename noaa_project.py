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
    'DC': 'Washington DC', # Added Washington DC
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
import re # This is how we're going to do a pattern text search.
from bs4 import BeautifulSoup
URL = 'https://www.weather.gov/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', id = (['wwaleft','wwaright','wwacenter_l','wwacenter_r']))
URLSlist = []
for result in results:
    # I added 'html.parser' here, to get rid of a warning in the console.
    soup_results = BeautifulSoup(str(result), 'html.parser').findAll('a', href=True)
    for a in soup_results:
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
        # You can use the library 're' to look for a regular expression
        # This just means you can look for a substring within a string
        #
        # https://www.w3schools.com/python/python_regex.asp
        #
        # Here's a fun tool to practice writing regular expressions to match
        # text. f"\s{state}\s" just creates a string with two whitespaces around
        # it to match on. So Indiana would be " IN " and you wouldn't find matches
        # for a word like "RINO"
        # https://rubular.com/

        # Convert pre to a string before you can do this
        pre_string = str(pre.text)

        # First loop through the abbreviations
        for state in us_state_abbrev.keys():
            matched_state = re.search(f"\s{state}\s", pre_string)
            if matched_state:
                # print(f"MATCHED STATE {state} for item {item}")
                states.append(matched_state.group(0).strip())
                singlestates = set(states)

        # Then loop through the state names, just in case.
        for state in us_state_abbrev.values():
            matched_state = re.search(f"\s{state}\s", pre_string)
            if matched_state:
                # print(f"MATCHED STATE {state} for item {item}")
                states.append(matched_state.group(0).strip())
                singlestates = set(states)

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
        # Now we have ot make sure the list is unique, since we looked for
        # both state names and abbreviations, and there could be duplicates.
        unique_tacos = set(tacos)
        unique_state_list = ", ".join(unique_tacos)

        # You can use a python "f string" to make strings a little easier than
        # using the plus sign +
        # https://realpython.com/python-f-strings/
        manytacos = f"A {alert} is in effect for parts of {unique_state_list}.\n Source: {item}\n\n"


    print(str(manytacos))
