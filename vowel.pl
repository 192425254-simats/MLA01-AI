% Vowel Identification

vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

check_vowel(X) :-
    vowel(X),
    write(X),
    write(' is a vowel.').

check_vowel(X) :-
    \+ vowel(X),
    write(X),
    write(' is not a vowel.').
