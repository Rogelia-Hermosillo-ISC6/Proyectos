% Base de datos de vuelos
vuelo(gdl, cdmx, 2000).
vuelo(cdmx, gdl, 1000).
vuelo(cdmx, mty, 800).
vuelo(mty, cdmx, 800).
vuelo(gdl, zac, 900).
vuelo(zac, gdl, 900).

vuelo(X, Y, Precio) :-vuelo(X, Z, P1),vuelo(Z, Y, P2),
    Precio is P1 + P2.

idavuelta(X, Y, Precio) :-vuelo(X, Y, P1),vuelo(Y, X, P2),
    Precio is P1 + P2.