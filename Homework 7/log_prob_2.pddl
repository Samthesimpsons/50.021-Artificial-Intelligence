(define (problem log-problem-2)
  (:domain log-problem)
  (:objects truck package1 package2 tampinese changi bedok)
  (:init (truck truck)
    (package package1) (package package2)
    (location tampinese) (location changi) (location bedok)
    (at-truck truck tampinese)
    (at-package package1 bedok) (at-package package2 changi)
    (path tampinese changi) (path changi tampinese) (path changi bedok)
    (path bedok changi) (path tampinese bedok) (path bedok tampinese))

  (:goal (and (at-package package1 changi) (at-package package2 bedok))))