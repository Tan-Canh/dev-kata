const weather = require("../weather");
require("jasmine-co").install();

describe("WeatherReader class ", () => {
  it("matches objects with the expect key/value pairs", async () => {
    // arrange
    // act
    const data = await weather.parseWeatherData();

    // assert
    expect(data[0]).toEqual({
      day: 1,
      maximum: 88,
      minimum: 59,
    });
  });

  it("matches objects with the expect key/value pairs", async () => {
    // arrange
    // act
    const data = await weather.dayWithSmallestSpread;

    // assert
    expect(data).toEqual({
      day: 14,
      maximum: 61,
      minimum: 59,
    });
  });
});
