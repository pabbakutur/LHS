import csv
import xlsxwriter

thefile = 'Landspitalinn_test.csv'

data = []
file = open(thefile, encoding = 'utf8')
reader = csv.DictReader(file, delimiter = ',')
for i in reader:
    data.append(i)
file.close()



personal_info = []
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
	patient_arrives = i['Sjúklingur mætir']
	booking_or_arrival = i['Bókun tengist komu']
	type_of_booking = i['Heiti komuflokks']
	time_unit = i['Tímaeining'] 
	number_of_bookings = i['Fjöldi bókana']
	#Create groups of information to easily write to csv and input to sql
	personal_info.append([identifier, postal_code, gender, age, booking_nr])



f = open('Landspitalinn_python_finished.csv', 'w')
#f.write('DateFrom;DateTo;LicensePlate;Dropoff\n')
for x in personal_info:
	f.write('{},{},{},{},{}\n'.format(x[0], x[1], x[2], x[3], x[4]))
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