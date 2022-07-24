curDate = input("Please enter the current date: ").split("/")
dd, mm, yyyy = map(int, curDate)
days = int(input("Please enter number of days: "))

curDays = yyyy*360 + (mm-1)*30 + dd
furDays = curDays + days

yyyy = (furDays-1) // 360 
furDays = (furDays-1)%360 + 1
mm = (furDays-1) // 30 + 1
dd = (furDays-1) % 30 + 1

print("The future date is: ")
print(str(dd) + "/" + str(mm) + "/" + str(yyyy))
