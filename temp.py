import datetime 
    
current_time = datetime.datetime.now() 

date = current_time.strftime("%d/%m/%Y")
hour = current_time.hour
minutes = current_time.minute

string = date + " " + str(hour) + ":" + str(minutes)

print(string)