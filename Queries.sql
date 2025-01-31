-- I used mySQL

-- What are the top 5 brands by receipts scanned for most recent month?
SELECT b.name AS brand_name, COUNT(r.receipt_id) AS receipt_count
FROM Receipts_Fact_Table r
JOIN Item_Dimension i ON r.receipt_id = i.receipt_id
JOIN Brands_Dimension b ON i.brand_id = b.brand_id
JOIN Time_Dimension t ON r.scan_date_key = t.time_id
WHERE t.date >= DATE_SUB((SELECT MAX(date) FROM Time_Dimension), INTERVAL 1 MONTH)
GROUP BY b.name
ORDER BY receipt_count DESC
LIMIT 5;

-- How does the ranking of the top 5 brands by receipts scanned for the recent month compare to the ranking for the previous month?
SELECT t.month, b.name AS brand_name, COUNT(r.receipt_id) AS receipt_count
FROM Receipts_Fact_Table r
JOIN Item_Dimension i ON r.receipt_id = i.receipt_id
JOIN Brands_Dimension b ON i.brand_id = b.brand_id
JOIN Time_Dimension t ON r.scan_date_key = t.time_id
WHERE t.date >= DATE_SUB((SELECT MAX(date) FROM Time_Dimension), INTERVAL 2 MONTH)
GROUP BY t.month, b.name
ORDER BY t.month DESC, receipt_count DESC
LIMIT 10;

-- When considering average spend from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?
SELECT
    rewardsReceiptStatus,
    AVG(totalSpent) AS avg_spend
FROM Receipts_Fact_Table
WHERE rewardsReceiptStatus IN ('Accepted', 'Rejected')
GROUP BY rewardsReceiptStatus;

-- When considering total number of items purchased from receipts with 'rewardsReceiptStatus’ of ‘Accepted’ or ‘Rejected’, which is greater?
SELECT
    rewardsReceiptStatus,
    SUM(purchasedItemCount) AS total_items
FROM Receipts_Fact_Table
WHERE rewardsReceiptStatus IN ('Accepted', 'Rejected')
GROUP BY rewardsReceiptStatus;

-- Which brand has the most spend among users who were created within the past 6 months?



-- Which brand has the most transactions among users who were created within the past 6 months?


