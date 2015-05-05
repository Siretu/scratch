vartannat [] = []
vartannat (x:[]) = [x]
vartannat (x:y:xs) = x : vartannat xs
