README: CV Generator Application


Overview

The CV Generator Application is a simple Python program that allows users to create a PDF version of their CV/Resume by filling in their details through a graphical user interface (GUI). This application uses the Tkinter library for the GUI, FPDF for generating the PDF, and pyqrcode for creating a QR code based on the user's website.

                -----------------------------------------------------------------------------------------------------------
Features:
User-friendly interface to input personal details.
Generates a PDF CV with sections such as Contact Information, Skills, Work Experience, Education, and About Me.
Automatically creates a QR code linked to the user's website and embeds it in the PDF.
Customizable CV template that includes headers and formatting for different sections.

                -----------------------------------------------------------------------------------------------------------
Requirements

To run this application, you need to have the following Python libraries installed:
    1. Tkinter - for creating the graphical user interface.
    2. FPDF - for generating the PDF file.
    3. pyqrcode - for generating the QR code from the website URL.
    4. Pillow (optional, for better image handling in PDFs).
    You can install these packages using pip:
        bash: pip install fpdf pyqrcode pypng

                -----------------------------------------------------------------------------------------------------------
How to Run the Application

1. Clone or download the code into your local environment.
2. Install the required dependencies (mentioned above).
3. Run the script using Python:
                    bash: python cv_generator.py
4. A GUI window will pop up allowing you to fill in the following details:
    Name
    Email
    Phone Number
    Address
    Website (a QR code will be generated from this)
    Skills (one per line)
    Education (in the format Degree: University)
    Work Experience (in the format Job Title: Description)
    About Me (brief description or summary)
5. Click on "Generate CV" once all the fields are filled.
6. A PDF file named cv1.pdf will be generated in the same directory as the script, with the details you entered.

                -----------------------------------------------------------------------------------------------------------
Code Structure

PDFCV class:
    Inherits from FPDF and is responsible for creating and formatting the CV.
    Implements header() to add the QR code image and generate_cv() to handle content generation for the PDF.
generate_cv_pdf function:
    Collects the input data from the GUI.
    Creates a QR code image from the website link.
    Calls the PDFCV class to generate the CV in PDF format.
Tkinter GUI:
    The GUI contains multiple entry fields where the user can input their personal details, skills, education, experience, and a summary.
    A "Generate CV" button that triggers the creation of the CV.

                -----------------------------------------------------------------------------------------------------------
Dependencies

    Python 3.x: Ensure Python 3.x is installed on your system.
    Tkinter: Built-in Python package for GUI.
    FPDF: For generating PDFs.
    pyqrcode: For generating a QR code of the user's website.
    Install them using:
        bash: pip install fpdf pyqrcode pypng

                -----------------------------------------------------------------------------------------------------------
Customization

You can easily customize the layout and appearance of the CV by modifying the following sections:
    PDFCV.header(): Customize the header section of the CV, where the QR code image is placed.
    PDFCV.generate_cv(): You can change the font, layout, or content of each section by adjusting this function.

                -----------------------------------------------------------------------------------------------------------
Error Handling

The application includes basic validation to ensure all fields are filled before generating the CV. If any fields are left empty, an error message will be displayed.


                -----------------------------------------------------------------------------------------------------------
Author

Created by Kevin Mathew.

This CV generator was designed as a simple tool to help individuals create their resumes quickly and efficiently using Python.