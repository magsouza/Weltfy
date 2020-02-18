import wikipedia
import json

nations = json.loads(open('countries.json').read())


def get_summary(artist):
    summary = wikipedia.summary(artist)
    summary = summary.replace('\n', '').replace(
        '\'', '').replace(',', '').replace('.', '')
    return summary


def try_cases(artist):
    types_of_cases = ['singer', 'group', 'band']
    cases = []
    summaries = []

    for type in types_of_cases:
        aux = f'{artist} ({type})'
        cases.append(aux)

    for case in cases:
        try:
            summary = get_summary(case)
            summaries.append(summary)
        except:
            pass

    return summaries


def get_summaries(artist):
    summaries = []
    try:
        summary = get_summary(artist)
        summaries.append(summary)
    except:
        summs = try_cases(artist)
        summaries.extend(summs)
    return summaries


def get_nationalities(summaries):
    nationalities = []
    for summ in summaries:
        summ = summ.split()
        # gets index of the keywords singer/band/...
        idx = index_to_split(summ)
        summ = summ[:idx]               # and slice it up to this word
        # so it can filter words with nationalities suffix
        summ = filter_suffixes(summ)
        nationalities.extend(summ)
    return nationalities


def get_nation(artist):
    summaries = get_summaries(artist)
    nationalities = get_nationalities(summaries)

    country = []
    for nat in nationalities:
        try:
            for dct in nations:
                if dct['adj'] in nat:
                    country.append(dct['country'])
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
        elif word.endswith('an'):
            sfx.append(word)

    return sfx


def index_to_split(summary):
    if 'singer' in summary:
        return summary.index('singer')
    elif 'group' in summary:
        return summary.index('group')
    elif 'band' in summary:
        return summary.index('band')
    elif 'rapper' in summary:
        return summary.index('rapper')


def get_code(country):
    for dct in nations:
        if dct['country'] == country:
            return dct['alpha-2'].lower()
