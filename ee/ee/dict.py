dict = {"name": "Ahamed", "age": 25, "courses": ["Math", "Physics"]}
print(dict["name"])
print(dict.get("age"))  # Output: 25

dict["grade"] = "A"
dict["age"] = 26
print("Updated :", dict)

del dict["courses"]
removed = dict.pop("grade")

print(dict.keys())
print(dict.values())
print(dict.items())

print('Maximum Key', max(dict))
print('Minimum Key', min(dict))
