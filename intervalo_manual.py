#Módulo para definir a primeira solicitação do intervalo / Module to define the first solicitation of the range

import definir_intervalo
import return_date

#Definir função / Define function
def intervalo(fluigs, fluig_inicial):

    
    cont = 0
    print('Contador', cont)

    for j in range(len(fluigs)):
        try:

            fluigs[j].index(fluig_inicial)
            print(fluigs[j])
            cont = cont + 1
            break

        except:
            pass

    if (cont == 0 ):
        print("Esse Fluig não consta na planilha. A definição do Fluig incial será dada pelo escopo definido em definir_intervalo.py")
        conferencia = return_date.today()
        #Determinar intervalo / Determine range
        j = definir_intervalo.intervalo(fluigs, conferencia)



    return (j)