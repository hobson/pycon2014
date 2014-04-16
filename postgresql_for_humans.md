Cribbed/Learned from [Craig Kerstiens (Heroku DBA)](craigkerstiens.com) 


cache hit rate >= 99%
---------------------


    SELECT 
      sum(heap_blks_read) as heap_read,
      sum(heap_blks_hit)  as heap_hit,
      sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio
    FROM 
      pg_statio_user_tables;


index hit rate >= 95% (99% for any tables > 10k rows)
---------------------

    SELECT 
      relname, 
      100 * idx_scan / (seq_scan + idx_scan) percent_of_times_index_used, 
      n_live_tup rows_in_table
    FROM 
      pg_stat_user_tables
    WHERE 
        seq_scan + idx_scan > 0 
    ORDER BY 
      n_live_tup DESC;


examine your queries to see what part is causing problems
---------------------------------------------------------

    #EXPLAIN ANAYLZE
    SELECT * FROM ...


Use pg_stat_statements
----------------------

    select * from pg_stat_statements where query ~ '...'

Index options
-------------

+ B-Tree - default
+ GIN - JSON or multiple values in a column
+ GIST -- shapes, text search
+ KNN - K nearest neighbors
+ VODKA - space-partitioned GIN index
+ conditional index - can index only portions of table using SELECT conditions
+ functional index - user-defined function output is indexable

Here's how you add one 

    CREATE INDEX ... where population > 10000

Or in django just add the `db_index=True` option to your field(s)


functional index (can index on output of a function)


Key Tips/Tools
--------------

+ If your user-defined function is deterministic (same input = same output) make sure you declare it as immutable in the functional INDEX


+ Cam create index CONCURRENTLY without blocking DB and bringing down live site .. It's roughly 2-3x slower and doesn't block!

+ hstore - key-value store that is better that JSON for doing key indexes, etc

    CREATE EXTENSION hstore ... # gives you json-like key-value field type


+ connection pooler in django 1.6 will reduce connection from 30-40 ms to less than a ms vs the same query on django 1.5 without connection pooling

+ pgbouncer better than pgpool if all you need is connection pooling

+ Use wal-e and barman for database replication

logical database backup < 50 GB, physical backup > 50 GB but lose cross-platform compatibility

