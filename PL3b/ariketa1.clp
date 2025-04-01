 

(defrule batura 
    (declare (salience 10)) 
    ?a <- (balio ?x) => (assert (balio (+ 1 ?x)))
) 
 

(defrule gelditu 
    (declare (salience 20)) 
    (balio ?x) 
    (test (> ?x 9)) => (halt)
) 

(deffacts hasierako_balioak (balio 1)) 
