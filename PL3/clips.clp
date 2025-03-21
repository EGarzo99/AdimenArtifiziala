;1. ARIKETA
(deffunction mugaTartean (?a ?b)
    (printout t "Sartu zenbaki bat " crlf)
    (bind ?c (read))
    (while (or (< ?c ?a) (> ?c ?b))
        (printout t "Mugatik kanpo, sartu beste zenbaki bat" crlf)
        (bind ?c (read))
    )
)

;2. ARIKETA
(deffunction zkh(?a ?b)
    (if (= ?a ?b) then 
        (return ?a)
    else (if (> ?a ?b) then
        (return (zkh (- ?a ?b) ?b))
    else
        (return (zkh ?a (- ?b ?a)))
    ))
)

;3. ARIKETA
(deffunction mkt(?a ?b)
    (bind ?c (* ?a ?b))
    (return (div ?c (zkh ?a ?b)))
)

;4. ARIKETA
(deffunction gorakorra($?a)
    (bind ?n (length$ $?a))
    (loop-for-count (?i 1 ?n)
        (loop-for-count (?j 1 (- ?n ?i))
            (if (> (nth$ ?j $?a) (nth$ (+ ?j 1) $?a))
                then
                    (bind ?tmp (nth$ ?j $?a))
                    (bind (nth$ ?j $?a) (nth$ (+ ?j 1) $?a))
                    (bind (nth$ (+ ?j 1) $?a) ?tmp)
            )
        )
    )
    (return $?a)
)
