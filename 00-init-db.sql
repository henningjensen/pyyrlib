CREATE TABLE IF NOT EXISTS `countries` (
  `countryid` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `countrycode` VARCHAR(2) NOT NULL,
  `countryname` VARCHAR(20) NOT NULL,
  UNIQUE (`countrycode`)
);

CREATE TABLE IF NOT EXISTS `places` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `countryid` INTEGER NOT NULL,
  `placename` VARCHAR(20) NOT NULL,
  `xml` VARCHAR(200) NOT NULL
);

CREATE INDEX places_countryid ON places ('countryid');
CREATE INDEX places_placename ON places ('placename');
