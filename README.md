# DocuMed
Group "Ctrl C + Ctrl V"'s Repository for CS253 Course Project, IIT Kanpur.


+ This healthcare-based software system comprises of the main working directory, [`DocuMed`](/DocuMed), containing the overall code responsible for establishing the sofware and getting it started, and 6 other directories, which are:

+ [`Doctors`](/doctors), the directory for the Django application "doctors", for maintaining the functionalities related to the doctor side interface and all its repositories/files containing the source codes for the same. It includes the URLs, templates, models, forms and views which constitute the entire doctor-side interface.

+ [`Patients`](/patients), same as for Doctors above but for the patient-side interface.

+ [`Media`](/media), the folder storing all the relevant documents required for the doctors and patients' access. It includes files for prescriptions, treatments, medical certificates, lab reports, scans, etc.

+ [`Templates`](/templates) contains the HTML templates and images which constitute the overall frontend of the project, non-specific to the doctor/patient interfaces. It includes the templates for the navbar, login, home, select profile, and registration pages, as well as background images and icons used throughout the whole software.

+ [`db.sqlite3`](/db.sqlite3) is the overall database of the software which maintains the data related to all the users (patients, doctors and admin) and the relations between them, and is responsible for querying, retrieval as well as manipulation of that data.

+ [`manage.py`](/manage.py) is the file which is responsible for managing and running the entire project. It contains code for execution of the project through the command line interface and running it on the Django admin server.









