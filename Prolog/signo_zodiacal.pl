signo(aries, 21, marzo, 19, abril).
signo(tauro, 20, abril, 20, mayo).
signo(geminis, 21, mayo, 20, junio).
signo(cancer, 21, junio, 22, julio).
signo(leo, 23, julio, 22, agosto).
signo(virgo, 23, agosto, 22, septiembre).
signo(libra, 23,septiembre,22,octubre).
signo(escorpio,23,octubre, 21,noviembre).
signo(sagitario,22,noviembre,21,diciembre).
signo(capricornio, 22, diciembre, 19, enero).
signo(acuario, 20, enero, 18, febrero).
signo(piscis, 19, febrero, 20, marzo).


zodiac_sign(Day, Month, Sign) :-
    signo(Sign, StartDay, StartMonth, EndDay, EndMonth),
    ((Month = StartMonth, Day >= StartDay); (Month = EndMonth, Day =< EndDay)).