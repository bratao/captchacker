import pickle

#Chargement des scores sauvegardés
f=open('scores.pck')
liste_scores = pickle.load(f)
f.close()

liste_scores.sort()

#Max scores at ending point
d = {}
for (pos, size, score, prediction) in liste_scores:
    d[pos] = [0, []]
d[0] = [0, []]

for (pos, size, score, prediction) in liste_scores:
    #Pour mettre à jour le plus haut score, il faut que:
    #- le score de l'intervalle considéré soit plus grand que le score courant (LE PLUS HAUT SCORE)
    #- il y ait une entrée dans le dico correspondant au début de l'intervalle considéré (LES INTERVALLES SE TOUCHENT)
    #- l'intervalle considéré
    
    if d.has_key(pos-size):
        cand = d[pos-size][0] + score

        if cand > d[pos][0]:
            if len(d[pos-size][1]) < 6:
                d[pos][0] = cand
                d[pos][1] = d[pos-size][1]+[prediction]
        


