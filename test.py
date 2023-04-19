text = 'Start'
indx = 1
for i in range(650):
    if indx % 150 == 0:
        text = 'Now 2'
        print(text)
    indx += 1
    text2 = f"#{indx} -1001492018811 65\n"
    text += text2
    indx +=1
    
print(text)
