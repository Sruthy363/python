course_python = {'alice','bob','simon','george','binny'}
course_datascience = {'tim','binny','ali','simon','abhijith'}
course_python.add('adil')
course_datascience.discard('tim')
course_combined = course_python.union(course_datascience)
print(course_python & course_datascience)
print(course_python - course_datascience)
print(course_combined)
courses = {
    "python" : 5,
    "datascience" : 4
}
for x,y in courses.items():
    print('Course:',x,',','Students:',y)

expected_growth = {key: value * 2 for key, value in courses.items()}
print(expected_growth)