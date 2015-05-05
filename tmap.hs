data TMap a = Leaf a
            | Children [TMap a]
              deriving Show
                       
tmap :: (a -> b) -> TMap a -> TMap b
tmap func (Leaf x) = Leaf (func x)
tmap func (Children list) = Children (map (tmap func) list)