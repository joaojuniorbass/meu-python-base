#!/usr/bin/python3

"""Hello World multi linguas.

Dependendo da lingua configurada  no ambiente o programa exibe a
 mensagem correspondente

Como usar: 

Tenha a variável LANG devidamente configurada. Ex:
	export LANG=pt_BR

Excecução:

	python3 hello.py
	ou
	./hello.py
"""
__version__ ="0.0.1"
__author__ = "João Carlos"
__licence__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
#também testei a variável como current_language = os.getenv("LANG").split(".")
#snake case -quando tudo é nomeado todo em minúsculo e separado por underline
#Pascal Case -> CurrentLanguage

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde"

print(current_language)   
print(msg)   






