def restock_check():
    count = 0
    infile = open("current_stock.txt", "r")
    outfile = open("restock_list.txt", "w")
    for line in infile:
       parts = line.split()
       name = parts[0]
       num = int(parts[1])
       if num < 15:
              outfile.write(name  + "\n")
              count += 1
    infile.close()
    outfile.close()


restock_check()


