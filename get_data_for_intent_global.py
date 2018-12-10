import json





data={
	"modify_leave_application": {
		"examples": [
			"want to modify",
			"can you change it.",
			"i want to change the date of leave and leave type",
			"a small correction needs to be done",
			"i want to modify starting date of leave and also leave type.",
			"i want to modify ending date of leave and also leave type.",
			"can you please change duration of leave along with leave type.",
			"i want to change it.",
			"want to change duration of leave",
			"i want to change the date of leave",
			"i want to change number of days.",
			"i want to modify starting date of leave.",
			"want to change duration of leave.",
			"i want to modify ending date of leave",
			"want to modify the leave type.",
			"can you change leave type.",
			"can i change category of leave applied",
			"i want to change type of leave.",
			"want to change leave type from sick to casual",
			"want to change leave type from annual to sick",
			"want to change leave type from casual to sick leave",
			"want to change my start date",
			"want to change my end date",
			"want to change my end date to 23rd april",
			"want to change my start date to 24th may",
			"a small correction needs to be done in duration of leave",
			"can u please help me for changing duration of leave",
			"can you please help me for changing leave type"
		]
	},
	"leave_application": {
		"examples": [
			"i want a leave for 2 days from 24th.",
			"i want a leave for 5 days starting from 3rd."
			"i want a leave for 6 days from 1st july.",
			"i want a leave for 7 days from tomorrow.",
			"i want to have leave for 2 days after jan 1st 2018",
			"just a week from 27th may",
			"i want a leave for 9 days since 2nd.",
			"i want a leave for 2 days before 24th.",
			"i want a leave for 5 days before 3rd."
			"i want a leave for 6 days before 1st july.",
			"i want a leave for 7 days before tomorrow.",
			"one week before 3rd april",
			"i want a leave for 9 days before 2nd.",
			"can you please sancation leave",
			"i want to apply for annual leave",
			"i want to apply for sick leave",
			"hey bot can you please help me in application for leave",
			"i want to have a leave for 25th july for attending my cousins marriage",
			"i want to have a leave for only today",
			"i want to apply for casual leave",
			"leave application",
			"apply for leave",
			"want to have a sick leave",
			"want to have a casual leave",
			"want to have a annual leave",
			"sick leave",
			"annual leave",
			"casual leave"
		]
	},
	"global_no": {
		"examples": [
			"nope",
			"no never",
			"nah!",
			"never",
			"nop",
			"a big no",
			"always a no",
			"reject"
		]
	},
	"terminate": {
		"examples": [
			"want to cancel it.",
			"No terminate it.",
			"nah cancel it.",
			"can you cancel the leave application",
			"cancel it"
		]
	},
	"global_yes": {
		"examples": [
			"yes",
			"yaa",
			"go ahead",
			"yup",
			"yah",
			"yeah",
			"ya",
			"a big yes",
			"yea!"
		]
	},
	"uncertain": {
		"examples": [
			"may be",
			"probably",
			"maybe",
			"mostly",
			"likely",
			"not yet decided",
			"hopefully"
		]
	},
	"misguiding_class": {
		"examples": [
			"want to apply for a bank loan",
			"i want to apply for pan card",
			"i want to apply for aadhar card",
			"i want to apply for house allowance",
			"can you book me movie tickets.",
			"i want to have a pizza",
			"can you change my order.",
			"i want to change my choice in pan card.",
			"can i change my phone number in aadhar card.",
			"i want to have a coffee.",
			"can you apply for pan card",
			"can you please apply for gas connection",
			"hey bot can you please help me in application of a new landline connection."
			"casual",
		]
	},
	"greet": {
		"examples": [
			"hello",
			"hey there",
			"good evening",
			"what can you do for me",
			"good afternoon",
			"hi",
			"hey",
			"hey ho",
			"whats up",
			"good morning",
			"what's up",
			"whatsup"
		]
	}
}

file_open = open('data_global_intent.json','w')
json.dump(data,file_open)
file_open.close()