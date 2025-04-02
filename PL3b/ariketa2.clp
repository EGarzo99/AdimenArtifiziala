(defrule elementuak-batu
    (declare (salience 10))
    (elementua ?x)
=>
    (assert (elementua (* 2 ?x)))
    (printout t (* 2 ?x) crlf)
)
    
(defrule gelditu
    (declare (salience 20))
    (elementua ?x)
    (test (> ?x 9))
=>
    (halt)
)

(deffacts hasierako_balioak
    (elementua 1)
)