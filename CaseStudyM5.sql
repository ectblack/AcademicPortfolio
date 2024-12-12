-- query 1 

Use `droneportation`;

update passenger 
	Set lastname = "pearson", 
		address = "7358 elementum st.",
        city = "New Auburn", 
        state = "wi", 
        regioncode = "54747", 
        locationlat = "45.204902",
        locationlong = "-91.562678"
Where passid = 114;



-- query 2 

Replace Into `passenger` (`passid`, `firstname`, `lastname`, `address`, `city`, `state`, `country`, `regioncode`, `locationlat`, `locationlong`)
		Values (114, "Christine", "Pearson", "7358 Elementum St.",  "New Auburn", "WI", "USA", "54747", "45.204902", "-91.562678");


-- Query 3

Delete from passgroup
Where groupid = 2;

Delete from passgroup
Where groupid = 89;

Select * from passgroup;


-- Query 4

Update drone
Inner join flightreservation as fr using (droneid) 
set fr.droneid = 5
where modelid = 3 AND statusid != 5;

-- Query 5

Delete from p, mp
using manifestpackage as mp Inner join package as p using (packageid)
Where packageid >= 1;


-- Query 6

Truncate table package;
truncate table manifestpackage;