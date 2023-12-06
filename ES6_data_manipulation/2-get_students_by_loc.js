const getStudentsByLocation = (list, location) => {
  return list.filter((student) => student.location === location);
};

export default getStudentsByLocation;
