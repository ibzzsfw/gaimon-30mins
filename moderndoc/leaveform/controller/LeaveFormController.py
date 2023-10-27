from gaimon.core.Route import POST
from xerial.AsyncDBSessionBase import AsyncDBSessionBase
from moderndoc.leaveform.model.LeaveForm import LeaveForm
from sanic import Request
from sanic import response

class LeaveFormController :
	def __init__(self, application) :
		self.application = application
		self.session: AsyncDBSessionBase = None

	@POST('/leaveform/insert', role=['guest'])
	async def insert(self, request:Request) :
		form = LeaveForm()
		form.fromDict(request.json)
		await self.session.insert(form)
		return response.json({})