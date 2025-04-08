-- Show Rider most recent Ride so they can rate it
SELECT *
FROM Ride
WHERE rider = 'mkp00'
ORDER BY rideID DESC
LIMIT 1;

-- Driver looking for their rating (replace Driver username with whoever logged in)
SELECT AVG(rating)
FROM Ride
WHERE driver = 'jdoe01';

-- Allow a Rider to rate a Ride after the fact if not most recent
-- ride (rating and rideID can be changed depending on user input)
-- Can be modified to just change rideID to one of most recent from above 
UPDATE Ride
SET rating = 3
WHERE rideID = 3;

-- Driver being able to see all of their rides (replace username in Python)
SELECT * FROM Ride WHERE driver = 'jdoe01';

-- Selecting first active Driver at top of table
SELECT * FROM driver WHERE active = TRUE LIMIT 1;

-- Changing Driver mode from (in)active (replace username and active, no need to check if they're already active
-- or inactive as SQL allows duplicate write over)
UPDATE Driver
SET active = TRUE
WHERE username = 'vzlow';

-- Adding a new Ride record to Ride table (replace rider, driver, pickUpLocation, dropOffLocation)
INSERT INTO Ride (rider, driver, pickUpLocation, dropOffLocation)
VALUES ('mkp00', 'jdoe01', '12345 QWERTY Street', '98765 YTREWQ Way')

-- BOTH below queries are for seeing all rides for a user
-- Can fstring this in python to just have one query depending
-- on if user is driver or rider and change rider/driver to other
SELECT *
FROM Ride
WHERE rider = 'mkp00';

SELECT *
FROM Ride
WHERE driver = 'jdoe01';
