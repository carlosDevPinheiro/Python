# -*- coding: cp1252 -*-
import fpdf
 
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
# insert my logo
pdf.image("python.png", x=10, y=8, w=23)

pdf.set_font("Arial", size=36)
pdf.cell(200, 10, txt="Python é supimpa!", ln=1, align="C")
pdf.set_font("Arial", size=12)
pdf.cell(200,10, "", ln=1)
pdf.cell(200,10, "", ln=1)
pdf.cell(200,10,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu eros, dapibus quis auctor a, varius ',0,1,'L')
pdf.cell(200,10,'in urna. Nulla at neque malesuada, ornare tortor sed, suscipit magna. Fusce malesuada congue dui,',0,1,'L')
pdf.cell(200,10,'sit amet sodales magna vulputate vel. Ut nec dictum orci. Mauris eleifend posuere diam, pretium',0,1,'L')
pdf.cell(200,10,'imperdiet quam venenatis sit amet. Phasellus id massa nec tortor consequat molestie quis eget erat.',0,1,'L')
pdf.cell(200,10, "", ln=1)
pdf.cell(200,10, "", ln=1)
pdf.cell(200,10,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu eros, dapibus quis auctor a, varius ',0,1,'L')
pdf.cell(200,10,'in urna. Nulla at neque malesuada, ornare tortor sed, suscipit magna. Fusce malesuada congue dui,',0,1,'L')
pdf.cell(200,10,'sit amet sodales magna vulputate vel. Ut nec dictum orci. Mauris eleifend posuere diam, pretium',0,1,'L')
pdf.cell(200,10,'imperdiet quam venenatis sit amet. Phasellus id massa nec tortor consequat molestie quis eget erat.',0,1,'L')
pdf.cell(200,10, "", ln=1)
pdf.cell(200,10, "", ln=1)
pdf.cell(200,10,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu eros, dapibus quis auctor a, varius ',0,1,'L')
pdf.cell(200,10,'in urna. Nulla at neque malesuada, ornare tortor sed, suscipit magna. Fusce malesuada congue dui,',0,1,'L')
pdf.cell(200,10,'sit amet sodales magna vulputate vel. Ut nec dictum orci. Mauris eleifend posuere diam, pretium',0,1,'L')
pdf.cell(200,10,'imperdiet quam venenatis sit amet. Phasellus id massa nec tortor consequat molestie quis eget erat.',0,1,'L')

pdf.output("exemplo.pdf")
