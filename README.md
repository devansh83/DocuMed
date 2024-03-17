# DocuMed
Group "Ctrl C + Ctrl V"'s Repository for CS253 Course Project, IIT Kanpur.


+ This healthcare-based software system comprises of the main working directory, [`DocuMed`](/DocuMed), containing the overall code responsible for establishing the sofware and getting it started, and 7 other directories, which are:
=
+ [`Doctors`](/doctors), for maintaining the functionalities related to the doctor side interface and all its repositories/files containing the source codes for the same. It includes the URLs, templates, models, forms and views which constitute the entire doctor-side interface.

+ [`Patients`](/patients), same as for Doctors above but for the patient-side interface.





+ Additionally, customers and employees can browse all cars in the store and check whether they can rent a particular car or not, and the price required for renting it. Managers can view all cars in the store, view all user details (except passwords), view which car is rented to whom, and add, delete and update details of any car or user. 

NOTE: There must always be atleast 1 manager in the system, and hence there must always exist 1 manager in the database [`managers.csv`](/managers.csv). All managers cannot be deleted, and this is taken care of since no manager can delete himself/herself.

+ Lastly, at runtime, care has been taken to ensure that invalid inputs are handled by the system accordingly using defensive programming, and only valid inputs will be considered by the system at each and every step of execution.

