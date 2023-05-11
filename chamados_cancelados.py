from __future__ import print_function

import os.path
import cancelados_fluig
import return_date
import definir_intervalo

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import selenium.webdriver.support.expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = ''
SAMPLE_RANGE_NAME = ''

creds = None

if os.path.exists('token.json'):
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
        
fluigs = result['values']

print(len(fluigs))

navegador = webdriver.Chrome(ChromeDriverManager().install(), options = options)
navegador.get("http://fluig.raizeducacao.com.br/portal/home")

username = navegador.find_element(By.ID, "username")
username.send_keys("")

password = navegador.find_elements(By.ID, "password")[-1]
password.send_keys("")

botao=navegador.find_element(By.ID, "submitLogin")
botao.click()

conferencia = return_date.today()

inicio = definir_intervalo.intervalo(fluigs, conferencia)

print(inicio)

while (inicio + 50 < len(fluigs)):

  respostas = cancelados_fluig.scraper(navegador, inicio, fluigs)

  print(respostas)

  result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Fluigs!P' + str(inicio + 1) + ':P' + str( inicio + 1 + len(respostas)), valueInputOption = 'USER_ENTERED', body={'values': respostas}).execute()
  
  inicio = inicio + 50

  print('Loop concluído. Informações na planilha')