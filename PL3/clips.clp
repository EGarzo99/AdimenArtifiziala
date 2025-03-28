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
    (bind ?ordenatuta FALSE)
    (while (not ?ordenatuta)
        (bind ?ordenatuta TRUE)
        (loop-for-count (?i (- ?n 1))
            (if (> (nth$ ?i $?a) (nth$ (+ ?i 1) $?a)) then
                (bind ?tmp (nth$ ?i $?a))
                (bind $?a (replace$ $?a ?i ?i (nth$ (+ ?i 1) $?a)))
                (bind $?a (replace$ $?a (+ ?i 1) (+ ?i 1) ?tmp))
         
                (bind ?ordenatuta FALSE)
            )
        )
    )
    (return $?a)
)

;5. ARIKETA
(deffunction gorakorraBikoitia($?a)
    (bind ?n (length$ $?a))
    (bind $?a2 (create$))
    (loop-for-count (?i ?n)
        (if (evenp (nth$ ?i $?a)) then
            (bind $?a2 (insert$ $?a2 1 (nth$ ?i $?a)))
        )
    )
    (return (gorakorra $?a2))
)

;6. ARIKETA
(deffunction diferentzia(?a $?b)
    (bind $?dif (create$))
    (loop-for-count (?i (length$ ?a))
        (if (not (member$ (nth$ ?i ?a) $?b)) then
            (bind $?dif (insert$ $?dif (+ 1(length$ $?dif)) (nth$ ?i ?a)))
        )
    )
    (return $?dif)
)

;7. ARIKETA
(deffunction kateaketa(?a $?b)
    (bind ?katea $?a)
    (loop-for-count (?i (length$ ?b))
        (bind ?katea (insert$ ?katea (+ 1(length$ ?katea)) (nth$ ?i ?b)))
    )
    (return ?katea)
)

;8. ARIKETA
(deffunction kartesiarra (?a $?b)
    (bind $?emaitza (create$))
    (loop-for-count (?i (length$ ?a))
        (loop-for-count (?j (length$ $?b))
            (bind $?temp (create$ (nth$ ?i ?a) (nth$ ?j $?b)))
            (bind ?emaitza (insert$ ?emaitza (+ 1(length$ ?emaitza)) $?temp))
        )
    )
    (return ?emaitza)
)

;9. ARIKETA
(deffunction lehenaDa(?a)
    (if (<= ?a 1) then
        (return FALSE)
    else
        (loop-for-count (?i 2 (div ?a 2))
            (if (= (mod ?a ?i) 0) then
                (return FALSE)
            )
        )
    )
    (return TRUE)
)

(deffunction kapikuaDa(?a)
    (bind ?lag 10)
    (bind $?lista (create$))
    (while (< 0 (div ?a ?lag))
        (bind $?lista (insert$ $?lista (+ 1(length$ $?lista)) (mod ?a ?lag)))
        (bind ?a (div ?a ?lag))
        (printout t $?lista " " crlf)
    ) 
)   