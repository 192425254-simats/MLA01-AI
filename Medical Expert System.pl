% Medical Expert System

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain).

disease(cold) :-
    symptom(cough),
    symptom(sneezing),
    symptom(runny_nose).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating).

% Patient symptoms
symptom(fever).
symptom(cough).
symptom(body_pain).

% Diagnosis
diagnose :-
    disease(Disease),
    write('Possible Disease: '),
    write(Disease),
    nl.
