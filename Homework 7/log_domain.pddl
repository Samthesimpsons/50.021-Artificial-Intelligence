(define (domain log-problem)
  (:predicates  (package ?p)
                (truck ?t)
                (location ?l)
                (path ?l ?l)
                (at-package ?p ?l)
                (at-truck ?t ?l)
                (in-truck ?p ?t))
(:action move
  :parameters (?truck ?from ?to)
  :precondition (and (truck ?truck) (location ?from) (location ?to) 
                (at-truck ?truck ?from) (path ?from ?to))
  :effect (and (at-truck ?truck ?to) 
          (not (at-truck ?truck ?from))))

(:action load
  :parameters (?pack ?truck ?location)
  :precondition (and (truck ?truck) (package ?pack) (location ?location)
                (at-truck ?truck ?location) (at-package ?pack ?location))
  :effect (and (in-truck ?pack ?truck) 
          (not (at-package ?pack ?location))))

(:action unload
  :parameters (?pack ?truck ?location)
  :precondition (and (truck ?truck) (package ?pack) (location ?location)
                (at-truck ?truck ?location) (in-truck ?pack ?truck))
  :effect (and (at-package ?pack ?location) 
          (not (in-truck ?pack ?truck)))))