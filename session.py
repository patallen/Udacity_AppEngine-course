def Session(ndb.Model):
	"""Session -- session database model"""
	name = ndb.StringProperty(required=True)
	highlights = ndb.StringProperty()
	speaker = ndb.StringProperty()
	durationInMin = ndb.IntegerProperty()
	typeOfSession = ndb.StringProperty(default="NOT_SPECIFIED")
	date = ndb.DateProperty()
	startTime = ndb.TimeProperty()

def SessionForm(messages.Message):
	"""SessionForm -- outbound form message"""
	name = messages.StringField(1)
	highlights= messages.StringField(2)
	speaker = messages.StringField(3)
	durationInMin = messages.IntegerField(4)
	typeOfSession = message.EnumField('TypeOfSession', 5)
	date = messages.StringField(6)
	startTime = messages.StringField(7)

def SessionForms(messages.Message):
	"""SessionForms -- multiple Sessions outbound form message"""
	items = messages.MessageField(SessionForm, 1, repeated=True)