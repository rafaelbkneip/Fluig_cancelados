#Importações / Imports
from __future__ import print_function
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path

#Importar módulos / Import modules
import cancelados_fluig
import return_date
import definir_intervalo
import login
import intervalo_manual

#Definir escopo da autorização / Define authorization scope
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#Definir planilha pelo seu ID e intervalo de células / Define spreadsheet by its ID and cell intervall
SAMPLE_SPREADSHEET_ID = ''
SAMPLE_RANGE_NAME = 'Fluigs!A:N'

#Acessar token de autorização / Access authorization token
creds = None
if os.path.exists('token.json'):
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('sheets', 'v4', credentials=creds)

#Acessar planilha e extrair valores / Access spreasheet and get values
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()    
fluigs = result['values']
print("A planilha consta com " + str(len(fluigs)) + " lançamentos.")

#Determinar dia da semana / Determine day of the week
conferencia = return_date.today()

#Para determinar o incío do intervalo, selecionar o método desejado: baseado em uma regra com os dias da semana ou baseada em uma solciitação0 especificada pelo usuário/
#Select the desired method to determine the range start: based on a weekday's logic or on a specific user-entered solicitation

#Determinar intervalo / Determine range
#Comentar caso o método escolhida seja o próximo / Comment the line if the selected method is the next one
inicio = definir_intervalo.intervalo(fluigs, conferencia)

#Determinar intervalo a partir de uma solicitação informada pelo usuário / Determine range starting from a user-entered solicitation
#Comentar caso o método escolhida seja o anterior / Comment the line if the selected method is the previous one
inicio = intervalo_manual.intervalo(fluigs, str(137925))

print("A leitura será iniciada pelo Fluig " + str(fluigs[inicio][0]))

#Logar / Log in
navegador = login.login()

#Determinar loop / Determine loop
#Escrever os resultados na planilha após a leitura de 50 chamados a partir do incial, definido anteriormente / Write the results after reading 50 solicitations, starting with the initial one, previously defined
while (inicio + 10 < len(fluigs)):

  #Obter os status das solicitações / Get the solicitation status
  respostas = cancelados_fluig.scraper(navegador, inicio, fluigs)

  print(respostas)

  #Escrever os resultados na planilha / Write the results on the spreadsheet
  result = sheet.values().update(spreadsheetId = SAMPLE_SPREADSHEET_ID, range ='Fluigs!N' + str(inicio + 1) + ':N' + str(inicio + 1 + len(respostas)), valueInputOption = 'USER_ENTERED', body = {'values': respostas}).execute()
  
  #Definir uma nova solicitação inicial / Define a new initial solicitation
  inicio = inicio + 10

  print('Loop concluído. Informações na planilha')