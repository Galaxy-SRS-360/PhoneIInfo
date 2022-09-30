import pyfiglet
import phonenumbers as pn
from phonenumbers import timezone,geocoder, carrier
  
  
text = pyfiglet.figlet_format("PhoneInfo")
print(text)
String=input("[+] Enter Phone number with Countrycode: ")

for match in pn.PhoneNumberMatcher(String, "IN"):
   print(match)
print("-------------------------------------------")
print("--------------BASIC DETAILS----------------")
print("-------------------------------------------")
National=pn.format_number(match.number, pn.PhoneNumberFormat.NATIONAL)
International=pn.format_number(match.number,pn.PhoneNumberFormat.INTERNATIONAL)
E164=pn.format_number(match.number, pn.PhoneNumberFormat.E164)

# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(match.number)
 
# Getting carrier of a phone number
Carrier = carrier.name_for_number(match.number, 'en')
  
# Getting region information
Region = geocoder.description_for_number(match.number, 'en')
# Validating a phone number
valid = pn.is_valid_number(match.number)
  
# Checking possibility of a number
possible = pn.is_possible_number(match.number)
  
# print the of a phonenumber
print("Natoinal_Format :",National)
print("Interatoinal_Format :",International)
print("E164_Format :",E164)
print("TimeZone :",timeZone)
print("Carrier :",Carrier)
print("Country :",Region)
print("Validity :",valid)
print("possibility :",possible)















