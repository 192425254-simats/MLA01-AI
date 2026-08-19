% Best First Search

edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).
edge(e, h).
edge(f, h).

% Heuristic values
h(a, 6).
h(b, 4).
h(c, 3).
h(d, 5).
h(e, 2).
h(f, 1).
h(g, 4).
h(h, 0).

best_first(Start, Goal, Path) :-
    search([Start], Goal, [], Path).

search([Goal|_], Goal, _, [Goal]).

search([Current|Rest], Goal, Visited, [Current|Path]) :-
    findall(H-Node,
        (edge(Current, Node),
         \+ member(Node, Visited),
         h(Node, H)),
        Children),
    append(Rest, Children, NewList),
    sort(NewList, Sorted),
    remove_heuristic(Sorted, Nodes),
    search(Nodes, Goal, [Current|Visited], Path).

remove_heuristic([], []).

remove_heuristic([_-Node|T], [Node|R]) :-
    remove_heuristic(T, R).
