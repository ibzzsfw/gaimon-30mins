from moderndoc.leaveform.model.LeaveForm import LeaveForm
from datetime import datetime
import requests


form = LeaveForm()
form.name = 'Kittipong'
form.reason = 'I do not know, why.'
form.student = 1
form.issuedDate = datetime.today()
response = requests.post('http://localhost:8080/leaveform/insert', json=form.toDict())
print(response.json())
