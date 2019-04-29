from app import db, Student, Hod, Teacher


# create Student(name)

sunny = Student("sunny")
arpit = Student("arpit")
db.session.add_all([sunny, arpit])
db.session.commit()

# fetch DATABASE

print(Student.query.all())

sunny = Student.query.filter_by(name='sunny').all()[0]
# create hod
hod1 = Hod("saurin", sunny.id)
# create teachers
teacher1 = Teacher("mihir", sunny.id)
teacher2 = Teacher("yash", sunny.id)
db.session.add_all([hod1, teacher1, teacher2])
db.session.commit()

# Let's now grab rufus again after these additions
sunny = Student.query.filter_by(name='sunny').first()
print(sunny)

# Show toys
sunny.report_Teachers()
