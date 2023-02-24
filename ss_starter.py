import smartsheet
import logging
import os
import json
import time

#define smartsheet user-specific api token
token = "insert your token here"

#initiate api call by creating an object of Smartsheet class, passing user-specific API token as parameter
smart = smartsheet.Smartsheet(token)
print("api call instantiated")

#obtain column ids of sheet with "get sheet" endpoint
try:
    sheet = smart.Sheets.get_sheet(2955863947274116) # <--pass sheet id here
except Exception as e:
    print("SS API error detected")
    exc = json.loads(str(e))
    print(exc)
else:
    sheet = json.loads(str(sheet))

#wipe out all current rows in the sheet
for quarter in list(quarters.quarters(row_ids).values()): #for every separate quarter list in the row_ids list
    for row_id in quarter:
        smart.Sheets.delete_rows(
        2955863947274116,                       # sheet_id
        [row_id ])     # row_ids
print("rows wiped out of smartsheet licensed users sheet")

#add user information in licensed_users py dict to "Smartsheet Licensed Users" grid in Smartsheet
try:
    for quarter in list(quarters.quarters(licensed_users['user_id']).values()):
        for employee in quarter:

            row_a = smartsheet.models.Row()
            row_a.to_bottom = True
            row_a.cells.append({
            'column_id': 1442733793535876,#column id for user email
            'value': licensed_users['user_email'][licensed_users["user_id"].index(employee)],
            'strict': False
            })
            row_a.cells.append({
            'column_id': 5946333420906372, #column id for sheet count
            'value': licensed_users['sheet_count'][licensed_users["user_id"].index(employee)],
            'strict': False
            })
            row_a.cells.append({
            'column_id': 3694533607221124, #column id for sheet count
            'value': licensed_users['last_login'][licensed_users["user_id"].index(employee)],
            'strict': False
            })

            #add rows to sheet
            response = smart.Sheets.add_rows(
            2955863947274116,       # sheet_id
            [row_a])
except Exception as e:
    print("SS API error detected")
    exc = json.loads(str(e))
    print(exc)
else:
    print("licensed user rows added to smartsheet licensed users sheet")