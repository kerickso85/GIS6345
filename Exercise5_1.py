import time
seconds_since_epoch = time.time() #declare variable for current time in reference to epoch
days_since_epoch =int(seconds_since_epoch/60/60/24) #convert current time to seconds, to min, and to days
print('Days since epoch:')
print(days_since_epoch)
current_hour = (seconds_since_epoch/(60*60))%24
#print('Current hour:') #debug hour statement
#print(int(current_hour)) #debug hour statement
current_minutes = (current_hour - int(current_hour))*60%60
#print('Current minutes:') #debug minutes statement
#print(int(current_minutes)) #debug minutes statement
current_seconds = (current_minutes - int(current_minutes))*60%60
#print('Current seconds:') #debug seconds statement
#print(int(current_seconds)) #debug seconds statement
current_time=str(int(current_hour))+':'+str(int(current_minutes))+':'+str(int(current_seconds))
print('The current time in GMT time zone is',current_time,'(hh:mm:ss)')


