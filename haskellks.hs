import GHC.Float

vartannat [] = []
vartannat [a] = [a]
vartannat (head:_:rest) = head : vartannat rest


data TMap a = Leaf a
            | Children [TMap a]
            deriving Show
                     
tmap :: (a -> b) -> TMap a -> TMap b
tmap f (Leaf a) = Leaf (f a)
tmap f (Children a) = Children (map (tmap f) a)

both f1 f2 lis = [x | x <- lis, (f1 x) == True, (f2 x) == True]

data HElem = IE Int
           | FE Float
           | RE Rational
             deriving Show
                      
baraheltal :: [HElem] -> [Int]
baraheltal [] = []
baraheltal (IE x:rest) = x:(baraheltal rest)
baraheltal (x:rest) = (baraheltal rest)

replace :: String -> String
replace "" = ""
replace (head:rest)
  | head == '%' = '#':(replace rest)
  | otherwise = head:(replace rest)

--makePolynom :: [Int] -> Int -> Int
--makePolynom koeff x = foldl (+) 0 [koeff!!n * (x**n)| n <- [0..(length koeff) - 1]]


makePolynom :: [Double] -> Double -> Double
makePolynom [c] _ = c
makePolynom (c:cs) x = c + x*(makePolynom cs x)


myPolynom koeff = makePolynom koeff


yValues x0 xn h = map (\x -> myPolynom [3,4,5] x) [x0,x0+h..xn]


myRev xs = foldr swap [] xs
swap x xs = xs ++ [x]

square x = x*x

anvVarje list x = map (\func -> func x) list