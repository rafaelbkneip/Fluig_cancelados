#Módulo para retornar o dia da semana / Module to get the weekday
#0 é domingo / 0 is Sunday

#Importações / Imports
from datetime import date
from datetime import datetime

#Definir função / Define function
def today():
    today = (datetime.now())
    return(today.weekday())