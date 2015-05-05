# Ruby version of sequence.py. 

def group(l)
  groups = []
  if l.length
    l = l.split("")
    current = [l[0]]
    l[1,l.length].each do |x|
      if x != current[0]
        groups.push(current)
        current = [x]
      else
        current.push(x)
      end
    end
    groups.push(current)
  end
  return groups
end

def compress(num)
  g = group(num.to_s)
  result = ""
  g.each { |x|
    result += (x.length.to_s + x[0])
  }
  return result.to_i
end

def seq(n)
  current = 1
  while n > 1
    current = compress(current)
    n -= 1
  end
  return current
end
