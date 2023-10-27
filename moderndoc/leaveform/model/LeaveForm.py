from xerial.Record import Record
from xerial.IntegerColumn import IntegerColumn
from xerial.StringColumn import StringColumn
from xerial.JSONColumn import JSONColumn
from xerial.DateColumn import DateColumn

class LeaveForm (Record) :
	student = IntegerColumn(foreignKey='User.id')
	name = StringColumn(length=120)
	reason = StringColumn(length=-1)
	uploadedFile = JSONColumn()
	submitDate = DateColumn()
	issuedDate = DateColumn(default=DateColumn.getDayAfterToday(1))
	leaveDate = DateColumn()

	def modify(self):
		modification = self.createModification('1.1')
		modification.add('leaveDate', DateColumn())
		modification = self.createModification('1.2')
		modification.rename('issueDate', 'issuedDate')
