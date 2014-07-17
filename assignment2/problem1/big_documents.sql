select count(docid)
from (
  select docid, sum(count) as term_total
  from frequency
  group by docid
  having term_total > 300
)
;
