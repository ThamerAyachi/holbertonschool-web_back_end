const getStudentsByLocation = (list, location) => {
  // eslint-disable-next-line arrow-body-style
  return list.filter((student) => student.location === location);
};

export default getStudentsByLocation;
