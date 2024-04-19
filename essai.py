

# import json
# import datetime

# # Define a custom function to serialize datetime objects


# def serialize_datetime(obj):
#     if isinstance(obj, datetime.datetime):
#         return obj.isoformat()
#     raise TypeError("Type not serializable")


# # Create a datetime object
# dt = datetime.datetime.now()

# # Serialize the object using the custom function
# json_data = json.dumps(dt, default=serialize_datetime)
# print(json_data)


# # Importing required modules

# # Create a datetime object
# dt = datetime.datetime.now()

# # Convert the datetime object to a string in a specific format
# dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")

# # Serialize the string using the json module
# json_data = json.dumps(dt_str)
# print(json_data)


# from datetime import datetime

# now = datetime.now()  # current date and time

# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:", date_time)


# my_file = open("hello.txt", "r", encoding="utf8")
# print(my_file.read())
# my_file.close()


# with open("hello.txt", "r", encoding="utf8") as my_file:
#     print(my_file.read())


# with open("hello.txt", "w", encoding="utf8") as my_file:
#     my_file.write("Hello world \n")
#     my_file.write("I hope you're doing well today \n")
#     my_file.write("This is a text file \n")
#     my_file.write("Have a nice time \n")


# with open("hello.txt") as my_file:
#     for line in my_file:
#         print(line)


dictionnaire = {"Mimi": 1960, "William": 1962, "Nelly": 1964}
liste = []
print(liste)
liste.append(dictionnaire)
print(liste)
