giorni = 0
veicoliTOT = 0
veicoli = 1 #non uguale a 0 perchè poi nn parte 

while veicoli != 0:
    veicoli= int(input("Quanti veicoli sono passati oggi dal casello ? ")) #cambiamo il valore variabile veicoli
    giorni = giorni +1
    veicoliTOT = veicoliTOT + veicoli #cambiamo valore alla veriabile mantenendo il numero del giorno precedente

    if veicoli == 0: #quando dobbaimo stoppare il prg
        giorni= giorni-1
        
print("In ", giorni," giorni, sono passati ", veicoliTOT, " veicoli")