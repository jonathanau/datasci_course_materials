select count(docid)
from frequency
where term = "parliament"
  and count >= 1
;
