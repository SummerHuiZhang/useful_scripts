with open("result.txt", "r") as infile: 
  lines=infile.readlines() 
  with open("result.txt", "w") as outfile: 
    for l in lines: 
      if '4096 1 13' not in l: 
        outfile.write(l)
