votiprimocandidato = int(input("Quanti voti ha ricevuto il primo candidato? "))
votisecondocandidato = int(input("Quanti voti ha ricevuto il secondo candidato? "))
punteggio = []
candidati = ["primo candidato", "secdondo candidato"]
punteggio.append(votiprimocandidato)
punteggio.append(votisecondocandidato)
candidati.sort()
print("Elenco candidati in ordine alfabetico: ", candidati)
if votiprimocandidato > votisecondocandidato:
    print("Elenco in base al punteggio in ordine decrescente", punteggio)
elif votisecondocandidato > votiprimocandidato:
    punteggio.reverse()
    print("Elenco in base al punteggio in ordine decrescente", punteggio)

