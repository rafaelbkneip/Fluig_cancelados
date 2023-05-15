#Módulo para definir a primeira solicitação do intervalo / Module to define the first solicitation of the range

#Definir função / Define function
def intervalo(fluigs, conferencia):

    #Os números dos casos representam os dias da semana / The case numbers represent the weekdays
    match conferencia:
        
        case 1:
            #As solciitações serão lidas a partir daquela que se encontra na posição do meio do intervalo / The solicitations will be scrapped starting with the one located at the center position of the range
            primeiro_fluig = int(len(fluigs)/2)

            #A primeira solicitação lida será a primeira do intervalo / The first solicitation to be scrapped is the first one in the range
        case 2:
            primeiro_fluig = 1

        case 3:
            primeiro_fluig = int(len(fluigs)/2)

        case 4:
            primeiro_fluig = 1

        case 5:
            primeiro_fluig = int(len(fluigs)/2)

    return (primeiro_fluig)