padre(juan, alberto).
padre(luis, alberto).
padre(alberto, leoncio).
padre(geronimo, leoncio).
padre(luisa, geronimo).

hermano(A,B) :- padre(X,A), padre(X,B), A \== B.
nieto(A,B):-padre(A,P), padre(B,P).

