(defrule R1 
    (declare (salience 15)) 
    ?a <- (zenbaki ?x ?u) 
    ?b <- (zenbaki ?y ?v) 
    (test (> ?u ?v)) 
=> 
    (assert (zenbaki (+ ?x ?y) (+ ?u 1))) 
    (retract ?b)
) 

(defrule R2 
    (declare (salience 5)) 
    ?b <-(totala ?x) 
    (test (> ?x 0)) 
=> 
    (assert (zenbaki 0 1))
) 

(defrule R3 
    (declare (salience 5))
    ?b <-(totala ?x) 
    (test (> ?x 1)) 
=> 
    (assert (zenbaki 1 2))
) 

(defrule R4 
    (declare (salience 20)) 
    (totala ?a) 
    (zenbaki ?x ?a) 
=> 
    (printout t "OK:" ?x crlf) 
    (halt)
) 

(defrule R5 
    (declare (salience 1)) 
=> 
    (printout t "ERROR" crlf)
) 