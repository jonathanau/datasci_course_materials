select sum(matrix_element)
from (
  select A.term, B.term, sum(A.count * B.count) as matrix_element
  from (
    select term, count
    from frequency
    where docid = "10080_txt_crude"
  ) as A
  ,
  (
    select term, count
    from frequency
    where docid = "17035_txt_earn"
  ) as B
  where A.term = B.term
  group by A.term, B.term
)
;
