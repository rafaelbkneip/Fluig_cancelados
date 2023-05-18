#Módulo para que o usuário defina a primeira solicitação do intervalo / Module for the user to define the first solicitation of the range

#Imporatações / Imports
import definir_intervalo
import return_date


#Definir função / Define function
def intervalo(fluigs, fluig_inicial):

    #Contador de controle / Control counter
    cont = 0

    for j in range(len(fluigs)):
        try:

            #Retornar com o índice da lista em que a solicitação informada se encontra / Return the index of the informed solicitation on the list
            fluigs[j].index(fluig_inicial)
            cont = cont + 1
            break
        
        except:
            pass
    
    #Caso não existir a solicitação na lista, selecionar a solicitação incial baseado na regra para os dias da semana / In case the solicitation cannot be found on the list, select the initial solicitation based on the weekdays
    if (cont == 0 ):
        print("Essa solicitação não consta na planilha. A definição da solicitação inicial será dada pelo escopo definido em definir_intervalo.py.")
        conferencia = return_date.today()
        j = definir_intervalo.intervalo(fluigs, conferencia)

    #Retornar a posição da solicitação / Return the index position of the solicitation
    return (j)