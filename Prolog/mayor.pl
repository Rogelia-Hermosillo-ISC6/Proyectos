lista([X], X).

lista([X|Todos], X) :-lista(Todos, MayorResto),X >= MayorResto.

lista([X|Todos], MayorResto) :-lista(Todos, MayorResto),X < MayorResto.





max(A,B,A) :- A >= B.
max(A,B,B) :- A < B.
maxl([H],H). 
maxl([H|T],M):- maxl(T,M1), max(M1,H,M). % Maximo de una lista