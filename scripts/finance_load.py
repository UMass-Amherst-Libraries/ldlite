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
    ('finance.budget', '/finance/budgets', allrec),
    ('finance.expense_class', '/finance/expense-classes', allrec),
#    ('finance.fund_code_exp_cla', '/finance/fund-codes-expense-classes', allrec),
    ('finance.fiscal_year', '/finance/fiscal-years', allrec),
    ('finance.fund', '/finance/funds', allrec),
    ('finance.fund_type', '/finance/fund-types', allrec),
    ('finance.group_fund_fy', '/finance/group-fund-fiscal-years', allrec),
##    ('finance.group_fy_sum', '/finance/group-fiscal-year-summaries', allrec),
    ('finance.groups', '/finance/groups', allrec),
    ('finance.ledger_roll_budget', '/finance/ledger-rollovers-budgets', allrec),
    ('finance.ledger_roll_log', '/finance/ledger-rollovers-logs', allrec),
#    ('finance.ledger_roll_error', '/finance/ledger-rollovers-errors', allrec),
#    ('finance.ledger_roll', ' /finance/ledger-rollovers', allrec),
    ('finance.ledger_roll_prog', '/finance/ledger-rollovers-progress', allrec),
    ('finance.ledger', '/finance/ledgers', allrec),
    ('finance.transaction', '/finance/transactions', allrec), 
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

