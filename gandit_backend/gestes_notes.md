# notes / justifications
on considère qu'on n'a qu'une seule chanson qu'on récupère (on sait toujours pas si on peut récupérer toute une playlist) et donc on va définir 4 gestes pour les deux capteurs qu'on a:
- STOP_MUSIC
- START_MUSIC
- UP_VOLUME
- DOWN_VOLUME

On considère aussi que l'on a que deux capteurs: un capteur P1 de pression et un capteur F2 de fléxion.


## START_MUSIC
- Les conditions sont: gesteP1 == 'PRESSED' and gesteF2 == 'TOOBENT'
+ Il faut donc bien fléchir son doit (un mouvement qui n'est pas naturel et donc on va pas avoir des réactions parasites à un geste) en cliquant avec son pouce (il faut bien appuyer).

## STOP_MUSIC
- Les conditions sont: gesteP1 == 'PRESSED' and gesteF2 == 'IDLE'
+ Il faut avoir un doigt comlpètement droit (un mouvement qui n'est pas naturel et donc on va pas avoir des réactions parasites à un geste) en cliquant avec son pouce (il faut bien appuyer).

## UP_VOLUME
- Les conditions sont: gesteP1 == 'IDLE' and gesteF2 == 'IDLE'
+ Il faut avoir un doigt comlpètement droit en évitant de faire un contact avec le capteur de pression qui est sur le pouce.

## DOWN_VOLUME
- Les conditions sont: gesteP1 == 'IDLE' and gesteF2 == 'TOOBENT'
+ Il faut donc bien fléchir son doit en évitant de faire un contact avec le capteur de pression qui est sur le pouce.



