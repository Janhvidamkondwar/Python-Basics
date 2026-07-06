student = {
    "Janhvi": 100,
    "Gaurav": 90,
    "Harry": 80,
    "Demo": 70,
    0: "Jani"
}

print("Keys:", student.keys())
print("Values:", student.values())

student.update({"Harry": 20})
print("After Update:", student)

student.pop("Janhvi")
print("After Pop:", student)

student.update({"Renuka": 60})
print("After Adding Renuka:", student)

print("Janhvi:", student.get("Janhvi"))
print("Harry:", student.get("Harry"))
print("Demo:", student.get("Demo"))
