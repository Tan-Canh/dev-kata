const { iterativeBinarySearch, recursiveBinarySearch } = require("../index");

describe("kata chop", () => {
  test("recursiveBinarySearch", () => {
    // recursiveBinarySearch
    expect(recursiveBinarySearch(3, [])).toBe(-1);
    expect(recursiveBinarySearch(3, [1])).toBe(-1);
    expect(recursiveBinarySearch(1, [1])).toBe(0);
    //
    expect(recursiveBinarySearch(1, [1, 3, 5])).toBe(0);
    expect(recursiveBinarySearch(3, [1, 3, 5])).toBe(1);
    expect(recursiveBinarySearch(5, [1, 3, 5])).toBe(2);
    expect(recursiveBinarySearch(0, [1, 3, 5])).toBe(-1);
    expect(recursiveBinarySearch(2, [1, 3, 5])).toBe(-1);
    expect(recursiveBinarySearch(4, [1, 3, 5])).toBe(-1);
    expect(recursiveBinarySearch(6, [1, 3, 5])).toBe(-1);
    //
    expect(recursiveBinarySearch(1, [1, 3, 5, 7])).toBe(0);
    expect(recursiveBinarySearch(5, [1, 3, 5, 7])).toBe(2);
    expect(recursiveBinarySearch(7, [1, 3, 5, 7])).toBe(3);
    expect(recursiveBinarySearch(0, [1, 3, 5, 7])).toBe(-1);
    expect(recursiveBinarySearch(2, [1, 3, 5, 7])).toBe(-1);
    expect(recursiveBinarySearch(4, [1, 3, 5, 7])).toBe(-1);
    expect(recursiveBinarySearch(6, [1, 3, 5, 7])).toBe(-1);
    expect(recursiveBinarySearch(8, [1, 3, 5, 7])).toBe(-1);
  });

  test("iterativeSearch", () => {
    // iterativeSearch
    expect(iterativeBinarySearch(3, [])).toBe(-1);
    expect(iterativeBinarySearch(3, [1])).toBe(-1);
    expect(iterativeBinarySearch(1, [1])).toBe(0);
    //
    expect(iterativeBinarySearch(1, [1, 3, 5])).toBe(0);
    expect(iterativeBinarySearch(3, [1, 3, 5])).toBe(1);
    expect(iterativeBinarySearch(5, [1, 3, 5])).toBe(2);
    expect(iterativeBinarySearch(0, [1, 3, 5])).toBe(-1);
    expect(iterativeBinarySearch(2, [1, 3, 5])).toBe(-1);
    expect(iterativeBinarySearch(4, [1, 3, 5])).toBe(-1);
    expect(iterativeBinarySearch(6, [1, 3, 5])).toBe(-1);
    //
    expect(iterativeBinarySearch(1, [1, 3, 5, 7])).toBe(0);
    expect(iterativeBinarySearch(3, [1, 3, 5, 7])).toBe(1);
    expect(iterativeBinarySearch(5, [1, 3, 5, 7])).toBe(2);
    expect(iterativeBinarySearch(7, [1, 3, 5, 7])).toBe(3);
    expect(iterativeBinarySearch(0, [1, 3, 5, 7])).toBe(-1);
    expect(iterativeBinarySearch(2, [1, 3, 5, 7])).toBe(-1);
    expect(iterativeBinarySearch(4, [1, 3, 5, 7])).toBe(-1);
    expect(iterativeBinarySearch(6, [1, 3, 5, 7])).toBe(-1);
    expect(iterativeBinarySearch(8, [1, 3, 5, 7])).toBe(-1);
  });
});
