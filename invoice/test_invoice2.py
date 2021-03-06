from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from decimal import Decimal
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table

def _build_invoice_information():    
    table_001 = Table(number_of_rows=8, number_of_columns=2)

    table_001.add(Paragraph(" "))
    table_001.add(Paragraph("Invoice: #3634-69420", horizontal_alignment=Alignment.RIGHT))

    table_001.add(Paragraph("Customer Name: Arnold"))
    table_001.add(Paragraph(" "))

    table_001.add(Paragraph("Phone: 9999420420"))
    table_001.add(Paragraph(" "))
	
    table_001.add(Paragraph("Address: -----------"))   
    table_001.add(Paragraph(" ")) 

    table_001.add(Paragraph(" "))   
    table_001.add(Paragraph("Sam Goods", font_size=30,  horizontal_alignment=Alignment.RIGHT))

    table_001.add(Paragraph(" "))   
    table_001.add(Paragraph("+91-78891-38650", horizontal_alignment=Alignment.RIGHT))

    table_001.add(Paragraph(" "))   
    table_001.add(Paragraph("sam@samgoods.com", horizontal_alignment=Alignment.RIGHT))

    table_001.add(Paragraph(" "))   
    table_001.add(Paragraph("10th Street, Mumbai", horizontal_alignment=Alignment.RIGHT))
    
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))    		
    table_001.no_borders()
    return table_001


def _build_itemized_description_table(items):  
    table_001 = Table(number_of_rows=len(items) + 2, number_of_columns=4)  
    for h in ["Item/Description", "Price per unit", "Quantity", "Price"]:  
        table_001.add(Paragraph(h, font="Helvetica-Bold"))  
   
    total = 0
    # Add items in the pdf and calculate total cost.
    for item in items:   
        table_001.add(Paragraph(item.name))  
        table_001.add(Paragraph("$ " + str(item.price)))  
        table_001.add(Paragraph(str(item.initial_stock - item.available_stock)))  
        table_001.add(Paragraph("$ " + str(item.price * (item.initial_stock - item.available_stock))))
        total += item.price * (item.initial_stock - item.available_stock)
     
    table_001.add(Paragraph("Total", font="Helvetica-Bold"))
    table_001.add(Paragraph(" "))  
    table_001.add(Paragraph(" "))  
    table_001.add(Paragraph("$ " + str(total))) 

    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))  
    # table_001.no_borders()
    table_001.set_borders_on_all_cells(border_top=True, border_right=True, border_bottom=True, border_left=True)
    return table_001

def build_thank_you():
    table_001 = Table(number_of_rows=1, number_of_columns=1)
    table_001.add(Paragraph("Thank you for shopping with us!", horizontal_alignment=Alignment.CENTERED))
    table_001.no_borders()
    return table_001



def get_pdf(pdf, company_table, items_table):
    page = Page()
    pdf.append_page(page)
    page_layout = SingleColumnLayout(page)
    page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)
    page_layout.add(company_table)  
    page_layout.add(Paragraph(" "))
    page_layout.add(items_table)
    page_layout.add(build_thank_you())
    with open("invoice.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)