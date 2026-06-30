'''Task : raw data recieved frm external database or API 
often comes in standardized, hypenated strings => need to slice 
them appropriately to get required data.'''

db_record = "RDM-LITHIUM-2026-HIGH_RISK"

# extracting the name of the  resource
resource = db_record[4:11]

# extracting vulnerablility risk
vulnerability_status = db_record[-9:]

# generate unique cache id
cache_id = db_record[::-1]

print(f'Parsed data => ID : {cache_id} ||| Resource : {resource} ||| Reading : {vulnerability_status}')