 

(deftemplate elementua 
    (slot balio (type INTEGER))
) 


(defrule erregela1 
    (declare (salience 10)) 
    (elementua (balio ?x)) 
=> 
    (assert (balio ?x))
) 


(defrule erregela2 
    (declare (salience 5)) 
    ?a <- (balio ?x) 
    (balio ?y) 
    (test (< ?x ?y)) 
=> 
    (retract ?a)
) 

 

(defrule erregela3 
    (declare (salience 1)) 
    ?a <- (balio ?x) 
=> 
    (printout t "Emaitza: balio " ?x crlf) 
    (retract ?a)
) 

 

(deffacts hasierkoak 
    (elementua (balio 1)) 
    (elementua (balio 8)) 
    (elementua (balio 5))
) 