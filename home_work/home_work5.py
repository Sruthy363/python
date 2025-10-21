frontend_course = {'Alice', 'Brian', 'Catherine', 'David', 'Emma'}
backend_course = {'Frank', 'George', 'Catherine', 'Helen', 'Brian'}
backend_course.add('adil')
frontend_course.remove('David')
print(backend_course)
print(frontend_course)
print(frontend_course & backend_course)
print(backend_course - frontend_course)
unique_students = frontend_course.union(backend_course)
print(unique_students)
courses = {
    'frontend' : 4,
    'backend'  : 6
}
for x,y in courses.items():
    print('course:',x,',','students:',y)
    
courses = {
    'Frontend': len(frontend_course),
    'Backend': len(backend_course)
}

full_courses = {course: count for course, count in courses.items()}
full_courses['Fullstack'] = len(frontend_course | backend_course)  

for course, count in full_courses.items():
    print(course, ":", count)