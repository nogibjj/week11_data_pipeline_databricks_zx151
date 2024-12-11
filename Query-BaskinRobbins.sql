CREATE OR REPLACE TABLE baskinrobbins_categorized AS
SELECT
  Flavour,
  Calories,
  Fat_without_Trans_g,
  CASE 
    WHEN Fat_without_Trans_g <= 5 THEN 'Low' -- Replace 5 with your actual low threshold
    WHEN Fat_without_Trans_g > 5 AND Fat_without_Trans_g <= 10 THEN 'Medium' -- Adjust these numbers
    ELSE 'High'
  END AS Fat_Category
FROM
  baskinrobbins_prepared;
