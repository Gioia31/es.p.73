bustapaga = 0
ndipendente = 0
stipTOT = 0

while bustapaga != -1: #ripeti finchè bustapaga != -1
    bustapaga = float(input("Quando hai finito com l'inserimnto dei dati digita: -1. Qual'è il tuo stipendio? "))
    stipTOT = bustapaga + stipTOT
    ndipendente = ndipendente +1
    media = stipTOT / ndipendente

    if bustapaga == -1:
        stipTOT = stipTOT +1  #annullo il -1
        ndipendente = ndipendente -1 #elimino il ndipendente con bustapaga -1
        media= stipTOT / ndipendente

print("Lo stipendio medio è di ", media)