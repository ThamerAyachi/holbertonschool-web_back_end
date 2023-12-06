export default function updateStudentGradeByCity(listStudent, city, newGrades) {
  return listStudent.find(student, student.location === city).map((student) => {
    const grade = newGrades.find((grade) => grade.studentId === student.id);
    return { ...student, grade: grade ? grade : 'N/A' };
  });
}
