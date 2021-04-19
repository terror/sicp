; a procedure that takes three numbers as input
; and returns the square of the two largest numbers

(define (sum-squared-two-largest x y z)
  (+ (* (max x y z) (max x y z)) (* (- (+ x y z) (max x y z) (min x y z)) (- (+ x y z) (max x y z) (min x y z))))
)

(display (sum-squared-two-largest 2 3 4)) (newline)
