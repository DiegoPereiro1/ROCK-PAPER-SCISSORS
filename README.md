# ROCK-PAPER-SCISSORS
Practice 1 // AI and Big Data course-IES de Teis

Diego Pereiro Martinez Sayanes

# Estrategia del Agente RPS
Se guardan los movimientos tanto del usuario como de la máquina en una lista.

Primer movimiento tiene que ser random

En el caso de que pierda el programa. El programa sacara lo que gane  al resultado con el que ha perdido:

Rondas posibles:
Papel>Piedra --->Programa sacara en la siguiente ronda Tijeras
Piedra>Tijeras -->Programa sacara en la siguiente ronda Papel
Tijeras>Papel --> Programa sacara en la siguiente ronda Piedra

En caso de perder dos o más veces seguidas. El programa deberá sacar el resultado con el que todavía no ha perdido.

En el caso de que gané el programa. En la siguiente ronda el programa sacará con lo que ha perdido el contrincante:

Rondas posibles:
Papel>Piedra ---> Programa sacara en la siguiente ronda Piedra
Piedra>Tijeras ---> Programa sacara en la siguiente ronda Tijeras
Tijeras>Papel --->  Programa sacara en la siguiente ronda Papel

En el caso de ganar 2 partidas seguidas deberá sacar el resultado con el que ha ganado la partida anterior.  

En caso de empate. El programa sacará un resultado random. Entre los dos resultados que quedan sin sacar.


# Estrategia del Agente RPSLS

Primer movimiento tiene que ser random
#1

En el caso de que pierda el programa. El programa sacara lo que gane  al resultado con el que ha perdido:

Rondas posibles:
Papel>Piedra--->Programa sacara en la siguiente ronda Tijeras o Lagarto
Spock>Piedra--->programa sacara en la siguiente ronda Papel o Lagarto

Spock>Tijeras--->Programa sacara en la siguiente ronda Papel o Papel

Piedra>Tijeras-->Programa sacara en la siguiente ronda Papel o Spock
Tijeras>Lagarto-->Programa sacara en la siguiente ronda Piedra o Spock

Lagarto>Spock-->Programa sacara en la siguiente ronda Piedra o Tijeras

Lagarto>Papel-->Programa sacara en la siguiente ronda Lagarto o Tijeras

Tijeras>Papel--> Programa sacara en la siguiente ronda Piedra o Spock

Piedra>Lagarto--->Programa sacara en la siguiente ronda Papel o Spock

Papel>Spock--->Programa sacara en la siguiente ronda Piedra o Lagarto``

En caso de perder dos veces seguidas. El programa deberá sacar un resultado random excluyendo con el que ha perdido durante 1,2 o 3 partidas seguidas.

Y si vuelve a perder volver al caso inicial de partida perdida.

En el caso de que gané el programa. En la siguiente ronda el programa sacará con lo que ha perdido el contrincante:

La primera evz que gana sacará el movimiento con el que ha perdido el usuario

En el caso de ganar 2 partidas seguidas deberá sacar el resultado con el que ha ganado la partida anterior.  

Resetear y volver a empezar en caso de volver a ganar


En caso de empate. El programa sacará un resultado random. Entre los dos resultados que quedan sin sacar.