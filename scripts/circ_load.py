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

ld.connect_okapi(url='', tenant='', user='', password='')




#db = ld.connect_db(filename='ldlite.db')
db = ld.connect_db_postgresql(dsn='dbname=ldplite host=localhost port=6991 user=ldplite password=saltldplite')

# For PostgreSQL, use connect_db_postgresql() instead of connect_db():
# db = ld.connect_db_postgresql(dsn='dbname=ldlite host=localhost user=ldlite')

allrec = 'cql.allRecords=1 sortby id'

queries = [
    ('audit.circulation_logs', '/audit-data/circulation/logs', allrec),
    ('circulation.audit_loan', '/loan-storage/loan-history', allrec),
    ('circulation.cancellation_reason', '/cancellation-reason-storage/cancellation-reasons', allrec),
    ('circulation.check_in', '/check-in-storage/check-ins', allrec),
    ('circulation.fixed_due_date_schedule', '/fixed-due-date-schedule-storage/fixed-due-date-schedules',allrec),
    ('circulation.loan', '/loan-storage/loans', allrec),
    ('circulation.loan_policy', '/loan-policy-storage/loan-policies', allrec),
    ('circulation.patron_action_session', '/patron-action-session-storage/patron-action-sessions', allrec),
    ('circulation.patron_notice_policy', '/patron-notice-policy-storage/patron-notice-policies', allrec),
    ('circulation.request', '/request-storage/requests', allrec),
    ('circulation.request_policy', '/request-policy-storage/request-policies', allrec),
    ('circulation.scheduled_notice', '/scheduled-notice-storage/scheduled-notices', allrec),
    ('circulation.staff_slips', '/staff-slips-storage/staff-slips', allrec),
    ('circulation.user_request_preference', '/request-preference-storage/request-preference', allrec),
    ('configuration.config_data', '/configurations/entries', allrec),
    ('circulation.email_notices', '/email', allrec),
    ('circulation.manualblocks', '/manualblocks', allrec)
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

