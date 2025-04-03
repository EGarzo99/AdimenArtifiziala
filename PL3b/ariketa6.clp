(deftemplate elementua
    (slot balio (type INTEGER)))

(defrule R1
    (declare (salience 40))
    (elementua (balio ?x))
    (not (hasiera ?))
    (test (>= ?x 0))
=>
    (assert (hasiera ?x)))

(defrule R2
    (declare (salience 20))
    (elementua (balio ?x))
    (not (elementua (balio 2)))
    (not (ezabatzen))
    (test (> ?x 2))
=>
    (assert (elementua (balio (- ?x 1)))))

(defrule R3
    (declare (salience 15))
    ?a <- (elementua (balio ?x))
    ?b <- (elementua (balio ?y))
    (test (> ?x ?y))
=>
    (assert (ezabatzen))
    (assert (elementua (balio (* ?x ?y))))
    (retract ?a)
    (retract ?b))

(defrule R4
    (declare (salience 30))
    ?a <- (elementua (balio 0))
=>
    (retract ?a)
    (assert (elementua (balio 1))))

(defrule R5
    (declare (salience 10))
    (hasiera ?x)
    (elementua (balio ?y))
    (test (>= ?y 0))
=>
    (printout t "OK:" "(" ?x "," ?y ")" crlf)
    (halt))

(defrule R6
    (declare (salience 1))
=>
    (printout t "ERROR" crlf))