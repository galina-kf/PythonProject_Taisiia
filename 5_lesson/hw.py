student = {
    "name": "John",
    "age": 20,
    "height": 180,
}
student.setdefault("city","Berlin")
student.update({"age":"23"})
del student["height"]
print(student)