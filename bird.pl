% ---------- Animal Classification ----------

bird(sparrow).
bird(parrot).
bird(eagle).
bird(pigeon).
bird(penguin).
bird(ostrich).

animal(dog).
animal(cat).

% ---------- Birds that cannot fly ----------

cannot_fly(penguin).
cannot_fly(ostrich).

% ---------- Inheritance Rule ----------

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).

% ---------- Animal Check ----------

is_bird(X) :-
    bird(X).
