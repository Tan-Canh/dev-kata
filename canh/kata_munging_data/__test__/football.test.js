const soccerReader = require("../football");
require("jasmine-co").install();

describe("SoccerReader class ", () => {
  it("matches objects with the expect key/value pairs", async () => {
    // arrange
    // act
    const data = await soccerReader.parseSoccerData();

    // assert
    expect(data[0]).toEqual({
      team: "Arsenal",
      goalsFor: 79,
      goalsAgainst: 36,
    });
  });

  it("matches objects with the expect key/value pairs", async () => {
    // arrange
    // act
    const data = await soccerReader.teamWithSmallestDifference;

    // assert
    expect(data).toEqual({
      team: "Aston_Villa",
      goalsFor: 46,
      goalsAgainst: 47,
    });
  });
});
