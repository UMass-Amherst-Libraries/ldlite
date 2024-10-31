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
    ('inventory.instance0', '/instance-storage/instances', 'id=0* sortby id', 0),
    ('inventory.instance1', '/instance-storage/instances', 'id=1* sortby id', 0),
    ('inventory.instance2', '/instance-storage/instances', 'id=2* sortby id', 0),
    ('inventory.instance3', '/instance-storage/instances', 'id=3* sortby id', 0),
    ('inventory.instance4', '/instance-storage/instances', 'id=4* sortby id', 0),
    ('inventory.instance5', '/instance-storage/instances', 'id=5* sortby id', 0),
    ('inventory.instance6', '/instance-storage/instances', 'id=6* sortby id', 0),
    ('inventory.instance7', '/instance-storage/instances', 'id=7* sortby id', 0),
    ('inventory.instance8', '/instance-storage/instances', 'id=8* sortby id', 0),
    ('inventory.instance9', '/instance-storage/instances', 'id=9* sortby id', 0),
    ('inventory.instancea', '/instance-storage/instances', 'id=a* sortby id', 0),
    ('inventory.instanceb', '/instance-storage/instances', 'id=b* sortby id', 0),
    ('inventory.instancec', '/instance-storage/instances', 'id=c* sortby id', 0),
    ('inventory.instanced', '/instance-storage/instances', 'id=d* sortby id', 0),
    ('inventory.instancee', '/instance-storage/instances', 'id=e* sortby id', 0),
    ('inventory.instancef', '/instance-storage/instances', 'id=f* sortby id', 0)


#    ('inventory.instance', '/instance-storage/instances', allrec),
#    ('inventory.instance_format', '/instance-formats', allrec),
#    ('inventory.instance_note_type', '/instance-note-types', allrec),
#    ('inventory.instance_relationship', '/instance-storage/instance-relationships', allrec),
#    ('inventory.instance_relationship_type', '/instance-relationship-types', allrec),
#    ('inventory.instance_status', '/instance-statuses', allrec),
#    ('inventory.instance_type', '/instance-types', allrec)
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
table = 'inventory.instance'
ld.query_big(table, 3, 50)
print('Tables:')
for t in tables:
    print(t)
print('(' + str(len(tables)) + ' tables)')

