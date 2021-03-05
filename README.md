GIOCO: SpeedHighway
Lo scopo del gioco è quello di allenare l'equilibrio di una persona.
Rimanendo fermi sul posto bisogna infatti spostare il busto a destra e a sinistra per schivare degli ostacoli che compaiono sullo schermo
Il giocatore deve essere munito di un marker di colore rosso da attacare sul petto.
Il gioco sfrutta due librerie: opencv e PyGame.
Tramite opencv, sfruttando la fotocamera, si rilevano gli oggetti di colore rosso e si ricavano le coordinate di questi ultimi.
![schermateVideocamera](https://user-images.githubusercontent.com/61046970/110084299-15d56000-7d90-11eb-862b-fb1c1ce6e60a.png)
Sfruttando le coordinate rilevate si sposta una macchina sull'asse delle ascisse sfruttando la libreria PyGame.
![download](https://user-images.githubusercontent.com/61046970/110084612-749ad980-7d90-11eb-8e1d-173b9369cf5b.png)
Gli ostacoli da evitare sono file di macchine che vengono spawnate sullo schermo in ordine e posizione randomici.
![immagineGioco](https://user-images.githubusercontent.com/61046970/110098006-fc3c1480-7d9f-11eb-8cb9-7a05affd1378.png)
Ogni volta che il giocatore supera un ostacolo viene incrementato il punteggio ma ATTENZIONE, la velocità degli ostacoli aumenta!!!
Ti conviene non schieantari contro le altre auto se non vuoi perdere.
![gameOver](https://user-images.githubusercontent.com/61046970/110098261-43c2a080-7da0-11eb-8826-6707e607a8ef.png)

