ans={}
#needed to seperate based on comma and : and | so in the entire string split correctly seperates based on the seperator we gave
for s in data:
    #now it splits by comma 
    values=s.split(",")
    #inner ones gets splitted for id number and second one becomes the number
    value1=values[0].split(":")[1]
    #name gets splitted here the second one being the name
    value2=values[1].split(":")[1]
    #all the three skills will have | here in the second part 
    value3=values[2].split(":")[1]
    #so we split them by | symbol
    value4=value3.split("|")
    #changing to int as mentioned and the values which are lists are sent in this dictionary as mentioned in the output
    ans[int(value1)]={"name":value2,"skills":value4}
print(ans)