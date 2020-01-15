import wikipedia, json

nations = json.loads(open('api/countries.json').read())

def get_summary(artist):
    summary = wikipedia.WikipediaPage(artist).summary
    summary = summary.replace('\n','').replace('\'','').replace(',', '').replace('.', '')
    return summary

def get_nation(artist):
    types_of_cases = ['singer', 'group', 'band']
    cases = []
    summaries = []

    try:
        summary = get_summary(artist)
        summaries.append(summary)
    except:
        for case in types_of_cases:
            aux = f'{artist} ({case})'
            cases.append(aux)

        for case in cases:
            try:
                summary = get_summary(case)
                summaries.append(summary)
            except:
                pass

    nationalities = []

    for summ in summaries:
        summ = summ.split()
        idx = index_to_split(summ)
        summ = summ[:idx]
        summ = filter_suffixes(summ)
        nationalities.append(summ)

    country = []
    
    for nat in nationalities:
        try:
            for dct in nations:
                if dct['adj'] in nat:
                    country.append(dct['country'])
                    break
        except:
            pass

    country = list(set(country))
    
    return country

def filter_suffixes(summary):
    sfx = []
    for word in summary:
        if not word[0].isupper():
            continue
        
        if word.endswith('ish'):
            sfx.append(word)
        elif word.endswith('ic'):
            sfx.append(word)
        elif word.endswith('ese'):
            sfx.append(word)
        elif word.endswith('ian'):
            sfx.append(word)
        elif word.endswith('ean'):
            sfx.append(word)
        elif word.endswith('ch'):
            sfx.append(word)
        elif word.endswith('i'):
            sfx.append(word)
        
    return sfx

def index_to_split(summary):
    if 'singer' in summary:
        return summary.index('singer')
    elif 'group' in summary:
        return summary.index('group')
    elif 'band' in summary:
        return summary.index('band')

def get_code(country):
    for dct in nations:
        if dct['country'] == country:
            return dct['alpha-2'].lower()