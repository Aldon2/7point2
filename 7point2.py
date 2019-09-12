fname = input("Enter file name: ")
fh = open(fname)
count=(0)
total=(0)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"): #continue
        count=(count+1)
        num=line[20:]
        num=float(num)
        total=(total+num)
    #count=(count+1)
        final=(total/count)
        #print(num)
#print(total)
print(final)
#print("Average spam confidence: ",final)
#print(fh)
#print(count)
#print(num)
