#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  more_Hours = int(input("Enter more hours : "))
  #Ask user for minutes
  more_Minute = int(input("Enter more minutes : "))
  #Calculate the time after the user-supplied time has passed.
  Total_minutes = (currentMinute + more_Minute)
  Extra_Hours = Total_minutes // 60
  future_minutes = Total_minutes % 60
  Total_Hours = currentHour + more_Hours + Extra_Hours
  future_hours = Total_Hours % 24
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print ( future_hours, future_minutes)


if __name__ == '__main__':
  main()
