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
    ('inventory.alternative_title_type', '/alternative-title-types', allrec),
    ('inventory.call_number_type', '/call-number-types', allrec),
    ('inventory.classification_type', '/classification-types', allrec),
    ('inventory.contributor_name_type', '/contributor-name-types', allrec),
    ('inventory.contributor_type', '/contributor-types', allrec),
    ('inventory.electronic_access_relationship', '/electronic-access-relationships', allrec),
    ('inventory.identifier_type', '/identifier-types', allrec),
    ('inventory.ill_policy', '/ill-policies', allrec),
    ('inventory.loan_type', '/loan-types', allrec),
    ('inventory.location', '/locations', allrec),
    ('inventory.loccampus', '/location-units/campuses', allrec),
    ('inventory.locinstitution', '/location-units/institutions', allrec),
    ('inventory.loclibrary', '/location-units/libraries', allrec),
    ('inventory.material_type', '/material-types', allrec),
    ('inventory.mode_of_issuance', '/modes-of-issuance', allrec),
    ('inventory.nature_of_content_term', '/nature-of-content-terms', allrec),
    ('inventory.service_point', '/service-points', allrec),
    ('inventory.service_point_user', '/service-points-users', allrec),
    ('inventory.statistical_code', '/statistical-codes', allrec),
    ('inventory.statistical_code_type', '/statistical-code-types', allrec),
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
print('Tables:')
for t in tables:
    print(t)
print('(' + str(len(tables)) + ' tables)')

