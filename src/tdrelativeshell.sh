# find all the dup wav files
find ./ -name "*).wav" > dupWav.txt

# rm last charactor
sed 's:(.*$::g' dupWav.txt 

# rm fist cha
sed -i 's:./::g' dupWav.txt 

# un name
mv dupWav.txt ddupWav.txt

# find all the dup txt files
find ./ -name '*.txt' | grep -v 'dup'> dupTxt.txt

# replace first part
sed -i 's:././::g' dupTxt.txt 

# replace last part
sed -i 's:\.txt::g' dupTxt.txt 

# find txt dup parts
sort dupTxt.txt  | uniq -D > ddupTxt.txt

# merge two dup txt file
cat ddup* > dddup.txt

# statical final dup files
sort dddup.txt | uniq > finalDup.txt

# find abnormal coding
find ./ -name  "*.txt" |xargs -i file {} | grep -v 'ISO-8859' > abnormalTxt

# 文本文件格式转换
find ./ -name "*.txt" | xargs -i iconv {} -f gbk -t utf-8 -o /home/zhangjl/dataCenter/asr/td/vx/txt_u8/{}

# find utf coding
find ./ -name "*.txt" | xargs -i file {} | grep  'UTF'
