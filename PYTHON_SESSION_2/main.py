time_in = input("What time is it? (e.g. 7:30 AM or 19:30): ")


time_parts = time_in.split(" ") # makes the time and the "am or pm" separate
time_in = time_parts[0].split(":") #cuts into 2 parts where there is colon

hour = int(time_in[0]) #gets hour
minute = int(time_in[1]) #gets min

if len(time_parts) == 2: #checks if theres 2 parts
    am_pm = time_parts[1].upper() #makes big 

    if am_pm == "PM" and hour != 12: #adds 12 if not 12
        hour += 12
    elif am_pm == "AM" and hour == 12: #if 12 it makes it 0
        hour = 0
#make into float 
#ex: 7+30/100 = 7.3
time = hour + minute / 100


if time >= 7.00 and time < 8.00: print("It is Breakfast time!")

elif time >= 12.00 and time < 13.00: print("It is Lunch time!")

elif time >= 18.00 and time < 19.00: print("It is Dinner time!")

