-- https://learnsql.com/blog/sql-window-functions-practice-exercises/
-- Q1
SELECT 
    single_rental.rental_date
    movie.title AS movie_title
    ,movie.genre AS genre
    ,payment_amount
    ,RANK() OVER(PARTITION BY genre OR payment_amount DESC) AS  rank_price_paid
FROM single_rental
LEFT JOIN movie ON
    single_rental.movie_id = movie.id
;
-- Q2

-- we use this because we don't want payment_rank
-- if we didn't create this subquery, we couldn't delete column payment_rank
WITH ranking AS (
    SELECT 
    first_name
    ,last_name
    ,payment_date 
    ,RANK() OVER(payment_date DESC) AS payment_rank 
FROM giftcard
JOIN customer ON
    giftcard.customer_id = customer.id
WHERE payment_rank = 2
)

SELECT 
    first_name,
    last_name,
    payment_date
FROM ranking
WHERE payment_rank = 2
