const cleanSet = (set, startString) => {
  if (startString === '') return '';
  let result = '';
  let flag = 0;
  set.forEach((element) => {
    if (element.startsWith(startString)) {
      result +=
        flag === 0
          ? element.split(startString)[1]
          : '-' + element.split(startString)[1];
      flag++;
    }
  });
  return result;
};

export default cleanSet;
