-- Some random old Haskell I/O test

import System.Environment (getArgs)
import System.IO
main = do { args <- getArgs;
--            let a = "hell";
            if args == [] then
              putStrLn "Empty!"
            else 
              do {
                ih <- openFile (head args) ReadMode;
                input <- hGetContents ih;
                ws <- return (lines input);
                putStrLn(show ws);
                hClose(ih)
}
          }
       
       
cleanInput str@(c:rest)
  | c == ">" = head (words rest)
  | otherwise = str