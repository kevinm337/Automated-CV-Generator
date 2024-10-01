from tkinter import * 
from fpdf import FPDF
import pyqrcode
from fpdf import FPDF
from tkinter import messagebox


class PDFCV(FPDF):
    def header(self):
        self.image('mywebsite.png',10,8,33)

    def footer(self):
        pass

    def generate_cv(self, name, email, phone, address, skills, work_exp, education, about_me):
        self.add_page()
        self.ln(20)

        # Displaying the name
        self.set_font("Arial", "B", 26)
        self.cell(0, 10, name, ln=True, align='C')

        # Adding Contact Info Header
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Contact Information', ln=True, align='L')

        # Adding the Contact Information
        self.set_font("Arial", "", 10)
        self.cell(0, 5, 'Email: {}'.format(email), ln=True)
        self.cell(0, 10, 'Phone: {}'.format(phone), ln=True)
        self.cell(0, 10, 'Address: {}'.format(address), ln=True)

        # Skills
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Skills', ln=True, align='L')

        # Adding Skills
        self.set_font("Arial", "", 10)
        for skill in skills:
            self.cell(0, 5, "- {}".format(skill), ln=True)

        # Work Experience
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Work Experience', ln=True, align='L')

        # Adding Experience
        self.set_font("Arial", "", 10)
        for workExp in work_exp:
            self.cell(0, 5, "{}: {}".format(workExp["title"], workExp["description"]), ln=True)

        # Education
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'Education', ln=True, align='L')

        # Adding Education
        self.set_font("Arial", "", 10)
        for educationItem in education:
            self.cell(0, 5, "{}: {}".format(educationItem["degree"], educationItem["university"]), ln=True)

        # About Me Header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, 'About Me', ln=True, align='L')

        # About Me
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, about_me)

        self.output('cv1.pdf')


def generate_cv_pdf():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    website = entry_website.get()
    skills = entry_skills.get('1.0', END).strip().split('\n')
    work_exp = []
    education = []

    work_exp_lines = entry_experience.get('1.0', END).strip().split('\n')
    for line in work_exp_lines:
        title, description = line.split(":")
        work_exp.append({'title': title.strip(), 'description': description.strip()})

    education_lines = entry_education.get('1.0', END).strip().split('\n')
    for line in education_lines:
        degree, university = line.split(":")
        education.append({'degree': degree.strip(), 'university': university.strip()})

    about_me = entry_about_me.get('1.0', END)

    # Create QR Code
    qrcode = pyqrcode.create(website)
    qrcode.png('mywebsite.png', scale=6)

    if not name or not email or not phone or not address or not skills or not work_exp or not education or not about_me:
        messagebox.showerror("Error", "Please fill in all the details")
        return

    cv = PDFCV()
    cv.generate_cv(name, email, phone, address, skills, work_exp, education, about_me)


root = Tk()
root.title('CV Generator')

label_name = Label(root, text='Name: ')
label_name.pack()

entry_name = Entry(root)
entry_name.pack()

label_email = Label(root, text='Email: ')
label_email.pack()
entry_email = Entry(root)
entry_email.pack()

label_phone = Label(root, text='Phone: ')
label_phone.pack()
entry_phone = Entry(root)
entry_phone.pack()

label_address = Label(root, text='Address: ')
label_address.pack()
entry_address = Entry(root)
entry_address.pack()

label_website = Label(root, text='Website: ')
label_website.pack()
entry_website = Entry(root)
entry_website.pack()

label_skills = Label(root, text='Skills (Enter one skill per line)')
label_skills.pack()
entry_skills = Text(root, height=5)
entry_skills.pack()

label_education = Label(root, text="Education (One per line in format 'Degree':'University')")
label_education.pack()
entry_education = Text(root, height=5)
entry_education.pack()

label_experience = Label(root, text="Experience (One per line in format 'Job Title':'Description')")
label_experience.pack()
entry_experience = Text(root, height=5)
entry_experience.pack()

label_about_me = Label(root, text="About Me")
label_about_me.pack()
entry_about_me = Text(root, height=5)
entry_about_me.pack()

button_generate = Button(root, text='Generate CV', command=generate_cv_pdf)
button_generate.pack()

root.mainloop()
