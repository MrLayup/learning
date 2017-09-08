def get_city(country, city, population=''):
	if population:
		formated_city = country + " " + city + " " + population
	else:
		formated_city = country + " " + city
	return(formated_city.title())

