select count(*)
from (
  select docid
  from frequency
  where term = "transactions"

  INTERSECT

  select docid
  from frequency
  where term = "world"
)
;
