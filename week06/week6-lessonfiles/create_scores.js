use test
//db.grades.drop();
types = ['exam', 'quiz', 'homework', 'homework'];
for (i = 0; i < 1000000; i++) {
    scores = []
    for (j = 0; j < 4; j++) {
	scores.push({'type':types[j],'score':Math.random()*100});
    }
    record = {'student_id':i, 'scores':scores};
    db.grades.insert(record);

}
	    
