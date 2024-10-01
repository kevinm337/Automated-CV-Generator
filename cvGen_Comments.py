# Importing necessary modules from tkinter and fpdf for GUI and PDF generation
from tkinter import * 
from fpdf import FPDF
import pyqrcode  # Importing pyqrcode for generating QR codes
from fpdf import FPDF  # Re-importing FPDF for generating the PDF
from tkinter import messagebox  # Importing messagebox for error alerts


# Defining a class PDFCV that inherits from FPDF to create custom CV PDF
class PDFCV(FPDF):
    # Defining the header method to display an image at the top of the page
    def header(self):
        self.image('mywebsite.png', 10, 8, 33)  # Inserting the website QR code image in the header

    # Defining the footer method, currently empty, you can add custom footer if needed
    def footer(self):
        pass

    # Defining a method to generate the CV PDF
    def generate_cv(self, name, email, phone, address, skills, work_exp, education, about_me):
        self.add_page()  # Adds a new page to the PDF
        self.ln(20)  # Adding some space at the top of the page

        # Displaying the name in the center with a large font size
        self.set_font("Arial", "B", 26)
        self.cell(0, 10, name, ln=True, align='C')

        # Adding the 'Contact Information' header
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Contact Information', ln=True, align='L')

        # Adding the contact information details (email, phone, address)
        self.set_font("Arial", "", 10)
        self.cell(0, 5, 'Email: {}'.format(email), ln=True)
        self.cell(0, 10, 'Phone: {}'.format(phone), ln=True)
        self.cell(0, 10, 'Address: {}'.format(address), ln=True)

        # Adding a space and 'Skills' header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Skills', ln=True, align='L')

        # Adding the list of skills one by one
        self.set_font("Arial", "", 10)
        for skill in skills:
            self.cell(0, 5, "- {}".format(skill), ln=True)

        # Adding a space and 'Work Experience' header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Work Experience', ln=True, align='L')

        # Adding the list of work experiences
        self.set_font("Arial", "", 10)
        for workExp in work_exp:
            self.cell(0, 5, "{}: {}".format(workExp["title"], workExp["description"]), ln=True)

        # Adding a space and 'Education' header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Education', ln=True, align='L')

        # Adding the list of education details
        self.set_font("Arial", "", 10)
        for educationItem in education:
            self.cell(0, 5, "{}: {}".format(educationItem["degree"], educationItem["university"]), ln=True)

        # Adding a space and 'About Me' header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'About Me', ln=True, align='L')

        # Adding the 'About Me' content in multi-line format
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, about_me)

        # Saving the generated PDF as 'cv1.pdf'
        self.output('cv1.pdf')


# Function to collect data from user input and generate the CV PDF
def generate_cv_pdf():
    # Retrieving data from the text fields
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    website = entry_website.get()
    
    # Splitting the skills entered by the user into a list
    skills = entry_skills.get('1.0', END).strip().split('\n')

    # Initializing empty lists for work experience and education
    work_exp = []
    education = []

    # Splitting and parsing the work experience entered by the user
    work_exp_lines = entry_experience.get('1.0', END).strip().split('\n')
    for line in work_exp_lines:
        title, description = line.split(":")  # Splitting the job title and description
        work_exp.append({'title': title.strip(), 'description': description.strip()})

    # Splitting and parsing the education details entered by the user
    education_lines = entry_education.get('1.0', END).strip().split('\n')
    for line in education_lines:
        degree, university = line.split(":")  # Splitting the degree and university
        education.append({'degree': degree.strip(), 'university': university.strip()})

    # Retrieving the 'About Me' section text
    about_me = entry_about_me.get('1.0', END)

    # Creating a QR code for the website URL provided by the user
    qrcode = pyqrcode.create(website)
    qrcode.png('mywebsite.png', scale=6)  # Saving the QR code as 'mywebsite.png'

    # Checking if any of the required fields are missing, if so show error message
    if not name or not email or not phone or not address or not skills or not work_exp or not education or not about_me:
        messagebox.showerror("Error", "Please fill in all the details")  # Error message if fields are missing
        return

    # Creating an instance of PDFCV and generating the CV
    cv = PDFCV()
    cv.generate_cv(name, email, phone, address, skills, work_exp, education, about_me)


# Setting up the Tkinter GUI window
root = Tk()
root.title('CV Generator')

# Name label and entry field
label_name = Label(root, text='Name: ')
label_name.pack()

entry_name = Entry(root)
entry_name.pack()

# Email label and entry field
label_email = Label(root, text='Email: ')
label_email.pack()

entry_email = Entry(root)
entry_email.pack()

# Phone label and entry field
label_phone = Label(root, text='Phone: ')
label_phone.pack()

entry_phone = Entry(root)
entry_phone.pack()

# Address label and entry field
label_address = Label(root, text='Address: ')
label_address.pack()

entry_address = Entry(root)
entry_address.pack()

# Website label and entry field
label_website = Label(root, text='Website: ')
label_website.pack()

entry_website = Entry(root)
entry_website.pack()

# Skills label and multi-line text field
label_skills = Label(root, text='Skills (Enter one skill per line)')
label_skills.pack()

entry_skills = Text(root, height=5)
entry_skills.pack()

# Education label and multi-line text field for entering education details
label_education = Label(root, text="Education (One per line in format 'Degree':'University')")
label_education.pack()

entry_education = Text(root, height=5)
entry_education.pack()

# Experience label and multi-line text field for entering work experience
label_experience = Label(root, text="Experience (One per line in format 'Job Title':'Description')")
label_experience.pack()

entry_experience = Text(root, height=5)
entry_experience.pack()

# About Me label and multi-line text field
label_about_me = Label(root, text="About Me")
label_about_me.pack()

entry_about_me = Text(root, height=5)
entry_about_me.pack()

# Button to trigger CV generation
button_generate = Button(root, text='Generate CV', command=generate_cv_pdf)
button_generate.pack()

# Start the Tkinter event loop
root.mainloop()
