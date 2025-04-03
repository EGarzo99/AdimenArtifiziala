(deftemplate pertsona 
    (slot izena (type SYMBOL))
    (slot hiria (type SYMBOL)) 
)

(deftemplate jarduera 
    (slot izena (type SYMBOL)) 
    (slot hiria (type SYMBOL)) 
    (slot iraupena (type INTEGER)) 
    
)

(deftemplate batezbestekoak 
    (slot izena (type SYMBOL)) 
    (slot hiria (type SYMBOL)) 
    (slot iraupena (type INTEGER)) 
    (slot ekintzaKop (type INTEGER))
)

(defrule batezbestekoak
    (declare (salience 20))
    ?a <- (pertsona (izena ?izena) (hiria ?hiria))
    =>
    (assert(batezbestekoak (izena ?izena) (hiria ?hiria) (iraupena 0) (ekintzaKop 0)))
    (retract ?a)
)

(defrule pertsonak_egonaldia 
    (declare (salience 10)) 
    ?p <- (batezbestekoak (izena ?izena) (hiria ?hiria) (iraupena ?batezbestekoa) (ekintzaKop ?ekintzaKop)) 
    ?j <- (jarduera (izena ?jarduera) (hiria ?hiria) (iraupena ?iraupena&:(> ?iraupena 1))) 
    => 
    (modify ?p (iraupena (+ ?batezbestekoa ?iraupena) ) (ekintzaKop (+ 1 ?ekintzaKop))) 
    (retract ?j)
)

(defrule batezbestekoa
    (declare (salience 5))
    ?p <- (batezbestekoak (izena ?izena) (iraupena ?iraupena) (ekintzaKop ?ekintzaKop&:(> ?ekintzaKop 0)))
    =>
    (printout t ?izena "(r)en jardueren batez besteko iraupena: " 
        (if (> ?ekintzaKop 0) then (/ ?iraupena ?ekintzaKop) else 0) crlf)
)


(deffacts pertsonak 
    (pertsona (izena Juan) (hiria Paris)) 
    (pertsona (izena Ana) (hiria Edimburgo))
) 
 
(deffacts jarduerak 
    (jarduera (izena Eiffel_Dorrea) (hiria Paris) (iraupena 2)) 
    (jarduera (izena Edimburgoko_Gaztelua) (hiria Edimburgo) (iraupena 5)) 
    (jarduera (izena Louvre) (hiria Paris) (iraupena 6)) 
    (jarduera (izena Montmartre) (hiria Paris) (iraupena 1)) 
    (jarduera (izena Royal_Mile) (hiria Edimburgo) (iraupena 3))
)