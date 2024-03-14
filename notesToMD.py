from macnotesapp import NotesApp
import markdownify
import re
from datetime import datetime
import json
import time
import schedule


year_month_day_format = '%Y-%m-%d'

notesapp = NotesApp()

def noteToMD():
    notes = notesapp.notes(accounts=["iCloud"])
    cleaned = []
## this loop removes all the files that are not in the "toObsidian Folder"
    for i in range(len(notes)):
        if notes[i].folder != "toObsidian":
            break
        cleaned.append(notes[i])
    notes = cleaned
    with open("processedFiles.json","r") as processed:
        processedFile = json.load(processed)



    for i in range(len(notes)):
        note = notes[i]
        print(note.folder)
        if note.name not in processedFile.keys():
            pass
        elif note.modification_date.strftime(year_month_day_format) != processedFile[note.name]:
            pass
        else:
            break
        # removes the heading by its html tag
        stripped =re.sub('^<div><h1>.*?</h1></div>',"",note.body)
        markdown_text = markdownify.markdownify(stripped)

        with open(note.name + ".md", "w") as file1:
            file1.write(markdown_text)

        with open("processedFiles.json","w") as processed:
            filenameDict = {note.name:note.modification_date}
            processedFile[note.name]=note.modification_date.strftime(year_month_day_format)
            json.dump(processedFile,processed)

schedule.every(1).hours.do(noteToMD)
print(schedule.get_jobs())
while True:
    schedule.run_pending()
    time.sleep(1)
# print("name:",
#     note.name)
# print(
#     note.body,
# # )
# print(re.sub('^<div><h1>.*?</h1></div>',"",note.body))

# markdown_text = markdownify.markdownify(stripped)
# #print(markdown_text)
# with open(note.name + ".md", "w") as file1:
#     file1.write(markdown_text)
# with open("processedFiles.json","r") as processed:
#     processedFile = json.load(processed)
# with open("processedFiles.json","w") as processed:
#     filenameDict = {note.name:note.modification_date}
#     processedFile[note.name]=note.modification_date.strftime(year_month_day_format)
#     json.dump(processedFile,processed)
#print(note.asdict()