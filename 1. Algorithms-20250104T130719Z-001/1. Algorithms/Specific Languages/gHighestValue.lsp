;; 1. g) Given a list of treasures with varying weights and values, determine the highest value possible within a given total summed weight limit.
;;       Objects are given in the format (x, y) where x is the size and y is the value.
;;       You may freely modify everything except the name of solution function and its parameters.

;; 1. g) Adonné une liste de trésors de valeurs et de poids différents, déterminez la plus grande valeur possible selon une limite de poids totale.
;;       Les trésors dans treasures sont du format (x, y) où x est le poids et y est la valeur.
;;       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.

;; CommonLisp

(defclass treasure()
    ((weight :reader treasure-weight
             :initarg :weight
             :type integer)

    (value   :reader treasure-weight
             :initarg :value
             :type integer))
)

;; treasures is a list of treasure objects
;; treasures est une liste d'objets de type treasure
(defun solution (treasures weightLimit)
 (if (< (treasure-weight (first treasures)) weightLimit)
    (return (treasure-value (first treasures)))
    (return 0))
)