import re
import random
import string
import json
import os

#Code for managing our json file:
###########################################################################
def load_json():
    """Load JSON data from a file."""
    filename = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(filename, "keywords_and_builtins.json")
    try:
        with open(filename, 'r') as file:
            return set(json.load(file))
    except FileNotFoundError:
        return set()

def save_json(data):
    """Save JSON data to a file."""
    filename = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(filename, "keywords_and_builtins.json")
    with open(filename, 'w') as file:
        json.dump(list(data), file, indent=4)

def add_to_json(new_items):
    """Add new items to the JSON file ensuring uniqueness."""
    filename = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(filename, "keywords_and_builtins.json")
    existing_data = load_json()
    updated_data = existing_data.union(new_items)
    save_json(updated_data)
###########################################################################    
    
#Code for decreasing the readability:      
######################################################      
def nakljucni_string(dolzina=8):
    dolzina = random.randint(dolzina, 5*dolzina)
    k1 = random.choice(string.ascii_letters + '_')
    k2 = ''.join(random.choices(string.ascii_letters + string.digits + '_', k=dolzina-1))
    return k1 + k2

def sifrirana_koda(koda, list_datotek=[]):
    vzorec = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b') 
    slovar = {}
    keywords_and_builtins = load_json()
    def zamenjaj(match):
        original = match.group(0)
        if original in keywords_and_builtins or original in list_datotek:
            return original
        if original not in slovar:
            slovar[original] = nakljucni_string()
        return slovar[original]
    vrstice = koda.splitlines()
    nove_vrstice = []
    for vrstica in vrstice:
        if not vrstica.isspace() and not vrstica == "":
            nova_vrstica = vzorec.sub(zamenjaj, vrstica)
            nove_vrstice.append(nova_vrstica)
    
    nova_koda = '\n'.join(nove_vrstice)
    nova_koda = re.sub(r'\s*([{}(;,+\-*/=<>])\s*', r'\1', nova_koda)
    return nova_koda

def spremeni_kodo(pot, ignoriraj=[], save_to_python=True):
    with open(pot, "r") as o:
        koda = o.read()
        
    pot = os.path.dirname(os.path.realpath(__file__))
    pot1 = os.path.join(pot, "code.txt")
    koda = sifrirana_koda(koda, ignoriraj)
    
    with open(pot1, "w") as o:
        o.write(koda)
        
    if save_to_python:
        pot2 = os.path.join(pot, "code.py")
        with open(pot2, "w") as o:
            o.write(koda)
    return "Finished"
            
######################################################
######################################################
######################################################
######################################################

#HOW TO USE:
#HOW TO USE:
#HOW TO USE:

###################################################
#If you are facing problems, you might need to add some keywords and builtins 
#(words which will remain unchanged after decreasing readability) to the json file:
#For instance, you might want to add support for math module (already included).
things_to_add = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'copysign', 'cos', 'cosh', 'degrees',
'exp', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gcd', 'hypot',
'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'log', 'log10', 'log1p',
'log2', 'modf', 'nextafter', 'pow', 'radians', 'remainder', 'sin', 'sinh',
'sqrt', 'tan', 'tanh', 'trunc'
]
#In this case remove # in the line below:
#add_to_json(things_to_add)
####################################################

#Otherwise:
####################################################
#Specify path to the code you want to edit:
path = r"Paste the path here"

#Specify the names of the variables you don't want to change, 
#for instance, you might want to include file names if you used them in the code:
ignore = ["myfile1", "myfile2", "myfavouritevariable", "specificmethod"]

#Run the code after removing the # below:     
#print(spremeni_kodo(path, ignore))
#####################################################
