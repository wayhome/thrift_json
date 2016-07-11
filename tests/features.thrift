struct Filter {
    1: required string attr,
    2: required string op,
    3: required string val
}

struct Flag {
    1: required string name,
    2: required i32 weight,
}


struct Branch {
    1: required list<Filter> path,
    2: required i32 volume,
    3: required list<Flag> leaf
}

struct Feature {
  1: required string name,
  2: required string key,
  3: required bool on,
  4: required i64 expired_at,
  5: required list<Branch> tree,
}

