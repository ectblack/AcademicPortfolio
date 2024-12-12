-- Query 1
SELECT OrderID, CustomerID, OrderDate, RequiredDate
FROM `Order`
WHERE shippeddate IS null
ORDER BY orderdate, requireddate

-- Query 2
SELECT orderid, ROUND(SUM(saleprice * quantity * (1-discount)), 2) AS Subtotal
FROM orderdetail
WHERE orderid = 10433 OR orderid = 10436 OR orderid = 10449
GROUP BY orderid
ORDER BY orderid

-- Query 3
SELECT productid, Productname, quantityperunit, supplierid, categoryid, listprice, unitcost, unitsinstock, unitsonreorder, reorderlevel, discontinued
FROM product
WHERE quantityperunit LIKE "%500 g%"

-- Query 4
SELECT country, COUNT(customerid) AS NumCustomers
FROM Customer
GROUP BY country
ORDER BY NumCustomers desc

-- Query 5
SELECT CustomerID, COUNT(DISTINCT(orderid)) AS NumOrders 
FROM `order`
GROUP BY customerid
ORDER BY NumOrders desc

-- Query 6 
SELECT orderid, employeeid
FROM `order`
WHERE orderid = 10433 OR orderid = 10436 OR orderid = 10449
ORDER BY orderid

-- Query 7
SELECT TimeStampDiff(DAY,Requireddate,shippeddate) AS DaysLate, COUNT(orderid) AS NumOrders
FROM `Order`
WHERE TimeStampDiff(DAY,Requireddate,shippeddate) > 0 AND shippeddate IS NOT null
GROUP BY DaysLate
ORDER BY DaysLate desc

-- Query 8
SELECT categoryID, ROUND(AVG(listprice - unitcost), 2) AS AvgProfit
FROM product
GROUP BY Categoryid HAVING avgprofit > 10
ORDER BY Categoryid

-- Query 9 
SELECT ROUND(AVG(TimeStampDiff(DAY, orderdate, shippeddate)), 4) AS LeadTimeDates
FROM `order`