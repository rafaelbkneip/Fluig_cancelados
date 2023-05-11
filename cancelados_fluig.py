from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from time import sleep

def scraper(navegador, inicio, fluigs):

  sleep(20)

  situacao=[]
  situacao_aux=[]

  for j in range(inicio,inicio+50): 

    sleep(5)

    print(fluigs[j][0])

    navegador.get("http://fluig.raizeducacao.com.br/portal/p/01/pageworkflowview?app_ecm_workflowview_detailsProcessInstanceID=" + str(fluigs[j][0]))

    WebDriverWait(navegador,20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="workflowView-cardViewer"]')))
    site_lancamento = navegador.find_element(By.XPATH, '//*[@id="workflowView-cardViewer"]')
    navegador.switch_to.frame(site_lancamento)

    cancelado_str =[]
    escondidos_str =[]

    cancelado = (navegador.find_elements(By.CLASS_NAME, 'ativ-cancelado'))
    escondidos = (navegador.find_elements(By.CLASS_NAME, 'hide'))

    for i in range(len(cancelado)):
      cancelado_str.append(str(cancelado[i]))

    for i in range(len(escondidos)):
      escondidos_str.append(str(escondidos[i]))

    contagem = (escondidos_str.count(cancelado_str[0]))

    if (contagem==0):
      situacao_aux.append('CANCELADO')

    else:
      situacao_aux.append('ATIVO')

    situacao.append(situacao_aux)
    situacao_aux = []

  return situacao