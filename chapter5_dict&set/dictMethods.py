marks = {
    "harsh": 100,
    "john": 56,
    "Rohan": 23,
    0: "harsh"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Renuka": 100})
print(marks)

# print(marks.get("harsh2")) # Prints None
# print(marks["harsh2"]) # Returns an error