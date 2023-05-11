def intervalo(fluigs, conferencia):

    match conferencia:

        case 1:
            primeiro_fluig = int(len(fluigs)/2)

        case 2:
            primeiro_fluig = 1

        case 3:
            primeiro_fluig = int(len(fluigs)/2)

        case 4:
            primeiro_fluig = 1

        case 5:
            primeiro_fluig = int(len(fluigs)/2)

    return (primeiro_fluig)