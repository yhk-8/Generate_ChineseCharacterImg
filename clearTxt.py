# ecoding=utf-8

#去掉文本行里面的空格、\t、数字（其他有要去除的也可以放到' \t1234567890......'里面）
ifn = r"test.txt"
ofn = r"train_output.txt"
 
infile = open(ifn,'r',encoding="utf-8",errors='ignore')
outfile = open(ofn,'w',encoding="utf-8",errors='ignore')
 
for eachline in infile.readlines():
  lines = filter(lambda ch: ch not in ' \t1234567890\nqwertyuiopasdfghjklzxcvbnm ":', eachline)
  lines=list(lines)
  outfile.writelines(lines) # 写入train_output.txt(此处是一股脑的全写进去，并没有做任何的分行处理)
 
infile.close
outfile.close