(deftemplate pertsona 
    (slot izena (type SYMBOL))
    (slot hiria (type SYMBOL)) 
)

(deftemplate jarduera 
    (slot izena (type SYMBOL)) 
    (slot hiria (type SYMBOL)) 
    (slot iraupena (type INTEGER)) 
)

(defrule pertsonak_egonaldia 
    (declare (salience 10)) 
    ?p <- (pertsona (izena ?izena) (hiria ?hiria)) 
    ?j <- (jarduera (izena ?jarduera) (hiria ?hiria) (iraupena ?iraupena)) 
    => 
    (printout t "Pertsona: " ?izena " Hiria: " ?hiria " Jarduera: " ?jarduera " Iraupena: " ?iraupena crlf) 
    (retract ?p)
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