import csv
import xlsxwriter

thefile = 'Landspitalinn_test.csv'

data = []
file = open(thefile, encoding = 'utf8')
reader = csv.DictReader(file, delimiter = ',')
for i in reader:
    data.append(i)
file.close()



patient_info = []
employee_info = []
booking_info = []
arrival_info = []
patient_and_employee = []
patient_and_booking = []
patient_and_arrival = []
employee_and_booking = []
employee_and_arrival = []
booking_and_arrival = []
distinct_id_list = []
distinct_employee_list = []
distinct_arrival_number_list = []
id_checker = set()
employee_checker = set()
arrival_number_checker = set()
id_checker_list = []
employee_checker_list = []
arrival_number_checker_list = []
info_list = []
for i in data:
	identifier = i['Identifier']
	booking_nr = i['Bókunarnúmer']
	arrival_number = i['Komunúmer']
	booking_year = i['Ár bókunar']
	booking_month = i['Mánuður bókunar (nr)']
	booking_weekday = i['Vikudagur bókunar nr.']
	booking_weekday_name = i['Vikudagur bókunar heiti']
	booking_date = i['Dagsetning bókunar']
	booking_time = i['Bókunartími']
	booking_hour = i['Bókunartími klst']
	booking_minute = i['Bókunartími mínúta']
	postal_code = i['Póstnúmer']
	gender = i['Kyn']
	age = i['Raunaldur']
	arrival_department = i['Núverandi heiti komudeildar']
	team = i['Heiti lotu'] 
	employee_name = i['Heiti bókað á']
	job_title = i['Starf 3 heiti']
	cancellation_reason = i['Ástæða afbókunar']
	cancellation_reason = cancellation_reason.replace(",","")
	patient_arrives = i['Sjúklingur mætir']
	booking_or_arrival = i['Bókun tengist komu']
	type_of_booking = i['Heiti komuflokks']
	time_unit = i['Tímaeining'] 
	number_of_bookings = i['Fjöldi bókana']
	#only add the id once
	if i['Identifier'] not in id_checker_list:
		distinct_id_list.append([identifier, postal_code, gender, age])
		id_checker.add(i['Identifier'])
		id_checker_list = list(id_checker)
	#only add the employee once
	if i['Heiti bókað á'] not in employee_checker_list:
		employee_checker.add(i['Heiti bókað á'])
		employee_checker_list = list(employee_checker)
		employee_name = employee_name.replace(",","")
		distinct_employee_list.append([employee_name, job_title, arrival_department, team])
	#same process to remove all 0 for arrival id's, only unique values
	if i['Komunúmer'] not in arrival_number_checker_list:
		#if i['Komunúmer'] != '0':
		distinct_arrival_number_list.append([arrival_number, time_unit])
		arrival_number_checker.add(i['Komunúmer'])
		arrival_number_checker_list = list(arrival_number_checker)
	#ath sjúklingur mætir dálkurinn ekki alltaf réttur, stundum 1 þegar það er ekkert komunúmer
	#Create groups of information to easily write to csv and input to sql
	patient_info.append([identifier, postal_code, gender, age])
	employee_info.append([employee_name, job_title, arrival_department, team])
	booking_info.append([booking_nr, booking_year, booking_month, booking_weekday, booking_weekday_name, booking_date, booking_time, booking_hour, booking_minute, type_of_booking])
	arrival_info.append([arrival_number, patient_arrives, cancellation_reason, time_unit])
	#create reference groups
	employee_name = employee_name.replace(",","")
	info_list.append([identifier, employee_name, booking_nr, arrival_number, patient_arrives, cancellation_reason, booking_or_arrival])
	
	#old code
	#patient_and_employee.append([identifier, employee_name])
	#patient_and_booking.append([identifier, booking_nr])
	#patient_and_arrival.append([identifier, arrival_number])
	#employee_and_booking.append([employee_name, booking_nr])
	#employee_and_arrival.append([employee_name, arrival_number])
	#booking_and_arrival.append([booking_nr, arrival_number])


f = open('Landspitalinn_python_finished.csv', 'w')
for x in distinct_id_list:
	f.write("insert into patient (id, postal, gender, age) values ('{}', '{}', '{}', '{}');\n".format(x[0], x[1], x[2], x[3]))
for x in distinct_employee_list:
	f.write("insert into employee (name, job, department, team) values ('{}', '{}', '{}', '{}');\n".format(x[0], x[1], x[2], x[3]))
for x in booking_info:
	f.write("insert into booking (booking_number, year, month, weekday, weekday_name, date, time, hour, minute, type_of_booking) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');\n".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]))
for x in distinct_arrival_number_list:
	f.write("insert into arrival (arrival_number, time_unit) values ('{}', '{}');\n".format(x[0], x[1]))
for x in info_list:
	f.write("insert into info (id, name, booking_number, arrival_number, patient_arrives, cancellation_reason, booking_or_arrival) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}');\n".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
#for x in patient_and_employee:
#	f.write("insert into patient_and_employee (id, name) values ('{}','{}');\n".format(x[0], x[1]))
#for x in patient_and_booking:
#	f.write("insert into patient_and_booking (id, booking_number) values ('{}','{}');\n".format(x[0], x[1]))
#for x in patient_and_arrival:
#	f.write("insert into patient_and_arrival (id, arrival_number) values ('{}','{}');\n".format(x[0], x[1]))
#for x in employee_and_booking:
#	f.write("insert into employee_and_booking (name, booking_number) values ('{}','{}');\n".format(x[0], x[1]))
#for x in employee_and_arrival:
#	f.write("insert into employee_and_arrival (name, arrival_number) values ('{}','{}');\n".format(x[0], x[1]))
#for x in booking_and_arrival:
#	f.write("insert into booking_and_arrival (booking_number, arrival_number) values ('{}','{}');\n".format(x[0], x[1]))	
f.close()










#líka mögulegt að nota set

#identifier = set()
#booking_nr = set()
#arrival_number = set()
#booking_year = set()
#booking_month = set()
#booking_weekday = set()
#booking_weekday_name = set()
#booking_date = set()
#booking_time = set()
#booking_hour = set()
#booking_minute = set()
#postal_code = set()
#gender = set()
#age = set()
#arrival_department = set() #núverandi heiti komudeildar
#team = set() #heiti lotu
#employee_name = set() #heiti bókað á
#job_title = set()
#cancellation_reason = set()
#patient_arrives = set()
#booking_or_arrival = set()
#type_of_booking = set()
#time_unit = set() #tímaeining (skráð tímalengd í kerfinu)
#number_of_bookings = set()

#for i in data:
	#identifier.add(i['Identifier'])
	#booking_nr.add(i['Bókunarnúmer'])
	#arrival_number.add(i['Komunúmer'])
	#booking_year.add(i['Ár bókunar'])
	#booking_month.add(i['Mánuður bókunar (nr)'])
	#booking_weekday.add(i['Vikudagur bókunar nr.'])
	#booking_weekday_name.add(i['Vikudagur bókunar heiti'])
	#booking_date.add(i['Dagsetning bókunar'])
	#booking_time.add(i['Bókunartími'])
	#booking_hour.add(i['Bókunartími klst'])
	#booking_minute.add(i['Bókunartími mínúta'])
	#postal_code.add(i['Póstnúmer'])
	#gender.add(i['Kyn'])
	#age.add(i['Raunaldur'])
	#arrival_department.add(i['Núverandi heiti komudeildar']) #núverandi heiti komudeildar
	#team.add(i['Heiti lotu']) #heiti lotu
	#employee_name.add(i['Heiti bókað á']) #heiti bókað á
	#job_title.add(i['Starf 3 heiti'])
	#cancellation_reason.add(i['Ástæða afbókunar'])
	#patient_arrives.add(i['Sjúklingur mætir'])
	#booking_or_arrival.add(i['Bókun tengist komu'])
	#type_of_booking.add(i['Heiti komuflokks'])
	#time_unit.add(i['Tímaeining']) #tímaeining (skráð tímalengd í kerfinu)
	#number_of_bookings.add(i['Fjöldi bókana'])