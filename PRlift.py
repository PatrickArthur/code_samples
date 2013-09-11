####################################################################################
## Weightlifting Personal Record Calculator - Import file or add in pr for the week#
## and how much percent you want to live each week#################################

#### Import functions to perform dates#####
import datetime
from datetime import date, timedelta

today=datetime.date.today()
Lastwk=date.today()-timedelta(days=7)


print "Welcome to the Weekly Fitness Tracker, please import this weeks exercises\n"


### Open text file and create a two dimensional list####

with open("Text2.txt") as f:
       lis=[list(map(str,x.split("/"))) for x in f]

### Open new text file that will be used to output results#####
fid=open("Pr"+str(today)+".txt","wb")


#### User adds in percent they want to go up and its turned into a percentage ####
print "Add in what percentage of your PR you want for goal\n"
wt_per=raw_input("Weight Percentage: \n")
wt_per2=(int(wt_per)*.01)


### Loop that is used when user adds in additional exercises not on import file####

excty=raw_input("Please add Extra Exercises Performed as of "+str(Lastwk)+"\n")
excty2=raw_input("Please add PR in lbs as of "+str(Lastwk)+"\n")
while (excty != ""):
    lis.append([excty,excty2])
    raw_input("Press <ENTER> to exit\n")
    excty=raw_input("Please add Exercise Performed as of "+str(Lastwk)+"\n")
    excty2=raw_input("Please add PR in lbs as of "+str(Lastwk)+"\n")
    


##### For loop used to output data

for i in lis:
    var3=float(i[1])
    var4 =float(i[1])*wt_per2+float(i[1])
    var5=i[0]
    print var5+" Personal Record as of "+str(Lastwk)+" is "+str(var3)+" lbs"
    print "Your "+var5+" goal for this week is to lift "+str(var4)+" lbs as of "+str(today)
    print ""
    fid.write(var5+" Personal Record as of "+str(Lastwk)+" is "+str(var3)+" lbs\n")
    fid.write("Your "+var5+" goal for this week is to lift "+str(var4)+" lbs as of "+str(today)+"\n")
    fid.write("  \n")
    

fid.close