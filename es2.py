primocandidato = str(input("Nome del primo candidato: "))
secondocandidato = str(input("Nome del secondo candidato: "))

votiprimocandidato = int(input("Quanti voti ha ricevuto " + primocandidato + " ? "))
votisecondocandidato = int(input("Quanti voti ha ricevuto " + secondocandidato + " ? "))

punteggio = []
candidati = []
candidati.append(primocandidato)
candidati.append(secondocandidato)
punteggio.append(votiprimocandidato)
punteggio.append(votisecondocandidato)
candidati.sort()
print("Elenco candidati in ordine alfabetico: ", candidati)

if votiprimocandidato > votisecondocandidato:
    print("Elenco in base al punteggio in ordine decrescente", punteggio)
elif votisecondocandidato > votiprimocandidato:
    punteggio.reverse()
    print("Elenco in base al punteggio in ordine decrescente", punteggio)

