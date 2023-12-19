# to create methodology behind understanding subsections during reading
from pydictionary import PyDictionary

pydic = PyDictionary()

def construct(strings):
    meanings = [pydic.meaning(x) for x in strings.split(' ')]

    