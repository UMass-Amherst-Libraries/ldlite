# This script uses LDLite to extract sample data from the FOLIO demo sites.

import sys
import ldlite

# Demo sites
#current_release = 'https://folio-juniper-okapi.dev.folio.org/'
# latest_snapshot = 'https://folio-snapshot-okapi.dev.folio.org/'

###############################################################################
# Select a demo site here:
#selected_site = current_release
###############################################################################
# Note that these demo sites are unavailable at certain times in the evening
# (Eastern time) or if a bug is introduced and makes one of them unresponsive.
# At the time of this writing, the "current release" demo site appears to be
# more stable than the "latest snapshot" site.  For information about the
# status of the demo sites, please see the #hosted-reference-envs channel in
# the FOLIO Slack organization.  For general information about FOLIO demo
# sites, see the "Demo Sites" section of the FOLIO Wiki at:
# https://wiki.folio.org
###############################################################################

ld = ldlite.LDLite()
#ld.connect_okapi(url=selected_site, tenant='diku', user='diku_admin', passowrd='admin')






#db = ld.connect_db(filename='ldlite.db')
db = ld.connect_db_postgresql(dsn='dbname=ldplite host=localhost port=6991 user=ldplite password=saltldplite')

# For PostgreSQL, use connect_db_postgresql() instead of connect_db():
# db = ld.connect_db_postgresql(dsn='dbname=ldlite host=localhost user=ldlite')

allrec = 'cql.allRecords=1 sortby id'

queries = [
    ('inventory.holdings_record0', '/holdings-storage/holdings', 'id=0* sortby id', 0),
    ('inventory.holdings_record1', '/holdings-storage/holdings', 'id=1* sortby id', 0),
    ('inventory.holdings_record2', '/holdings-storage/holdings', 'id=2* sortby id', 0),
    ('inventory.holdings_record3', '/holdings-storage/holdings', 'id=3* sortby id', 0),
    ('inventory.holdings_record4', '/holdings-storage/holdings', 'id=4* sortby id', 0),
    ('inventory.holdings_record5', '/holdings-storage/holdings', 'id=5* sortby id', 0),
    ('inventory.holdings_record6', '/holdings-storage/holdings', 'id=6* sortby id', 0),
    ('inventory.holdings_record7', '/holdings-storage/holdings', 'id=7* sortby id', 0),
    ('inventory.holdings_record8', '/holdings-storage/holdings', 'id=8* sortby id', 0),
    ('inventory.holdings_record9', '/holdings-storage/holdings', 'id=9* sortby id', 0),
    ('inventory.holdings_recorda', '/holdings-storage/holdings', 'id=a* sortby id', 0),
    ('inventory.holdings_recordb', '/holdings-storage/holdings', 'id=b* sortby id', 0),
    ('inventory.holdings_recordc', '/holdings-storage/holdings', 'id=c* sortby id', 0),
    ('inventory.holdings_recordd', '/holdings-storage/holdings', 'id=d* sortby id', 0),
    ('inventory.holdings_recorde', '/holdings-storage/holdings', 'id=e* sortby id', 0),
    ('inventory.holdings_recordf', '/holdings-storage/holdings', 'id=f* sortby id', 0)

#        ('inventory.holdings_note_type', '/holdings-note-types', allrec),
#    ('inventory.holdings_record', '/holdings-storage/holdings', allrec),
#    ('inventory.holdings_type', '/holdings-types', allrec),
    ]


tables = []
for q in queries:
    try:
        if len(q) == 4:
            t = ld.query(table=q[0], path=q[1], query=q[2], json_depth=q[3])
        else:
            t = ld.query(table=q[0], path=q[1], query=q[2])
        tables += t
    except (ValueError, RuntimeError):
        print('folio_demo.py: error processing "' + q[1] + '"', file=sys.stderr)
print()
table = 'inventory.holdings_record'
ld.query_big(table, 3, 50)
print('Tables:')
for t in tables:
    print(t)
print('(' + str(len(tables)) + ' tables)')

