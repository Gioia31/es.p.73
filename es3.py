bustapaga = 0
ndipendente = 0
stipTOT = 0

stipTOT = 0
ndipendente = 0
bustapaga = 0 

while True: #ripeti finchè la cond nn è falsa
    bustapaga = float(input("Quando hai finito com l'inserimnto dei dati digita: -1. Qual'è il tuo stipendio? "))
    if bustapaga == -1:
        break
    else : 
        stipTOT = stipTOT + bustapaga
        ndipendente = ndipendente + 1 
        media= stipTOT / ndipendente

print("Lo stipendio medio è di ", media)