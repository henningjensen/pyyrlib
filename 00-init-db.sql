CREATE TABLE IF NOT EXISTS `locations` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `country` VARCHAR(100) NOT NULL,
  `xml` VARCHAR(200) NOT NULL,
  UNIQUE (name, country) ON CONFLICT REPLACE
);

CREATE INDEX locations_name ON locations ('name');
CREATE INDEX locations_country ON locations ('country');

