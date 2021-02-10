import json
import tkinter as tk
from tkinter import filedialog

def parseJSON():
  # Choose input file here
  root = tk.Tk()
  root.withdraw()

  file = filedialog.askopenfilename(
    title = "File to read"
  )

  # CSV table formatting block
  fields = [
    "VodRequest_ID", 
    "name",
    "ATPScore",
    "group",
    "amount",
    "log value",
    "date",
    "description squeezed and trimmed",
    "description original"
  ]
  data = []

  # Extraction
  with open(file) as infile:
    for line in infile:
      borrower = json.loads(line)
      vod_request_id = borrower["VodRequest_ID"]
      name = borrower["Name"]
      atp = borrower["ATPScore"]["ATP"]
      for group_title in borrower["GroupedTransactions"]:
        if borrower["GroupedTransactions"][group_title] != []:
          for item in borrower["GroupedTransactions"][group_title]:
            for transaction in item:
              csv_entry = [
                vod_request_id, 
                name, 
                atp, 
                group_title, 
                transaction["Amount"], 
                transaction["Tags"]["_LogAmount"], 
                transaction["Date"], 
                transaction["DescriptionSqueezedAndTrimmed"], 
                transaction["DescriptionLower"]
              ]
              data.append(csv_entry)
  
  return [fields, data]
