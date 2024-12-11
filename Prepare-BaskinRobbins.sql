%sql
CREATE OR REPLACE TABLE
  baskinrobbins_prepared (
    Flavour STRING,
    Calories LONG,
    Total_Fat_g DOUBLE,
    Trans_Fat_g DOUBLE,
    Carbohydrates_g LONG,
    Sugars_g LONG,
    Protein_g DOUBLE,
    Fat_without_Trans_g DOUBLE
  );

INSERT INTO
  baskinrobbins_prepared
SELECT
  Flavour,
  Calories,
  Total_Fat_g,
  Trans_Fat_g,
  Carbohydrates_g,
  Sugars_g,
  Protein_g,
  Fat_without_Trans_g
FROM
  baskin_robbins_prepared
