MonthConversion ={
    "Jan" : "January",
    "Feb": "Febuary",
    "Mar" : "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(MonthConversion["Jan"])
print(MonthConversion.get("Jan"))
print(MonthConversion["Feb"])
print(MonthConversion["Mar"])
print(MonthConversion["Jun"])
print(MonthConversion["Sept"])
print(MonthConversion["Oct"])
##Manual Initialize     
print(MonthConversion.get("Swa","Love you bro"))
##if you want to get the file name is in dictionary you have to find using the get or index if you use get of unknown word ypu used to get None 