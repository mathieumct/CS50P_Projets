from fpdf import FPDF, XPos, YPos
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        self.set_text_color(0, 0, 0)
        lenght_page = 210
        text = "CS50 Shirtificate"
        text_width = self.get_string_width(text)
        position_x = (lenght_page - text_width) / 2
        self.set_x(position_x)
        self.cell(110, 20, text, 0, 1, 'C')

    def add_image(self):
        im = Image.open("shirtificate.png")
        image_width, image_height = im.size
        image_width_mm = image_width * 0.264583
        image_height_mm = image_height * 0.264583
        height_page = 297
        position_y = (height_page - image_height_mm) / 2
        self.set_y(position_y)
        lenght_page = 210
        position_x = (lenght_page - image_width_mm) / 2
        self.set_x(position_x)
        self.image("shirtificate.png", w=image_width_mm, h=image_height_mm)

    def text(self):
        name_user = input("Name: ")
        lenght_page = 210
        height_page = 297
        image_height = 592
        image_height_mm = image_height * 0.264583
        self.set_font("helvetica", "", 20)
        position_x = (lenght_page - self.get_string_width(name_user)) / 2
        self.set_x(position_x)
        position_y = (height_page + image_height_mm) / 2 - 100
        self.set_y(position_y)
        self.set_text_color(255, 255, 255)
        self.cell(0, 0, name_user + " took CS50", 0, 1, 'C')

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.add_image()
pdf.text()
pdf.output("shirtificate.pdf")
