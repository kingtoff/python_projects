MonthConversions = {
    "Jan" : "January",  #using key-pair value
    "Feb" : "February",
     "Mar" : "March",
     "Apr" : "April",
     "May" : "May",
     "Jun" : "June",
     "Oct" : "October"

}
print(MonthConversions.get("Oct"))
print(MonthConversions["Feb"])
print(MonthConversions.get("Nov", "does not exist"))
