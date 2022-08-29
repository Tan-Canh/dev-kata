const recursiveBinarySearch = (num, arr, left, right) => {
  const l = left === undefined ? 0 : left;
  const r = right === undefined ? arr.length : right;
  const mid = Math.floor(l / 2 + r / 2);

  if (l > r || arr.length === 0) {
    return -1;
  } else if (arr.length === 1 || l === r) {
    return arr[0] === num ? 0 : -1;
  } else if (arr[mid] === num) {
    return mid;
  } else if (arr[mid] > num) {
    return recursiveBinarySearch(num, arr, l, mid - 1);
  } else if (arr[mid] < num) {
    return recursiveBinarySearch(num, arr, mid + 1, r);
  }

  return -1;
};

const iterativeBinarySearch = (num, arr) => {
  let left = 0;
  let right = arr.length;
  let mid = 0;

  while (left < right) {
    mid = Math.floor((left + right) / 2);
    if (arr[mid] === num) {
      return mid;
    } else if (arr[mid] > num) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  if (arr[left] === num) {
    return left;
  }

  return -1;
};

module.exports = {
  recursiveBinarySearch,
  iterativeBinarySearch,
};
