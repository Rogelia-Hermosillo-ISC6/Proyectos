:- discontiguous padre/2.

padre(rogelio, luis).
padre(martha, luis).

padre(rogelio, lupe).
padre(martha, lupe).

padre(agustin, marisela).
padre(lidia, marisela).

padre(agustin, rita).
padre(lidia, rita).

esposo(luis, marisela).
esposo(luism, rita).
esposo(raul, lupe).

padre(luis, eduardo).
padre(marisela, eduardo).

padre(luis, yazmin).
padre(marisela, yazmin).

padre(luism, mili).
padre(rita, mili).

padre(luism, enrique).
padre(rita, enrique).

padre(raul, lorena).
padre(lupe, lorena).

padre(raul, junior).
padre(lupe, junior).

hijo(Hijo, Padre) :-
    padre(Padre, Hijo).

hermano(A,B) :-
    padre(X,A),
    padre(X,B),
    A \== B.

nieto(Nieto, Abuelo) :-
    padre(Abuelo, Padre),
    padre(Padre, Nieto).

tio(Tio, Sobrino) :-
    hermano(Tio, Padre),
    padre(Padre, Sobrino).

primo(A,B) :-
    padre(P1,A),
    padre(P2,B),
    hermano(P1,P2),
    A \== B.

esposos(A,B) :-
    esposo(A,B).

esposos(A,B) :-
    esposo(B,A).

abuelo(Abuelo, Nieto) :-
    padre(Abuelo, Padre),
    padre(Padre, Nieto).
