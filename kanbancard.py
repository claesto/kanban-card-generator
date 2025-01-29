from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from urllib.parse import quote
import segno
import os

class KanbanCard:
    """
    Class to generate a Kanban card as a PDF with QR code.
    """
    default_colors = {
        "dark": "black",
        "light": "gray"
    }

    def __init__(self, item="", brand="", store="", kanban_level=0, order_qty=0, list_name="Groceries"):
        """
        Initialize a KanbanCard instance.

        Args:
            item (str): The name of the item
            brand (str): The brand of the item
            store (str): The store where to purchase the item
            kanban_level (int): The kanban level
            order_qty (int): The quantity to purchase
            list_name (str): The name of the list
        """

        if kanban_level < 0 or order_qty < 0:
            raise ValueError("Both 'kanban_level' and 'order_qty' must be non-negative integers.")



        self.item = item
        self.brand = brand
        self.kanban_level = kanban_level
        self.order_qty = order_qty
        self.store = store
        self.list_name = list_name

        
        self.create_kanban_card()

    def generate_qr_code(self, filepath="qrcode.png"):
        """
        Generate a QR code and save it to the specified filepath.

        Args:
            filepath (str): The file path to save the QR code.
        """
        encoded_list_name = quote(self.list_name)
        encoded_item = quote(self.item + " " + "(" + self.brand + ")")
        qr_url = f"shortcuts://run-shortcut?name=AddToList&input=list={encoded_list_name}:item={encoded_item}"
        qrcode = segno.make_qr(qr_url)
        qrcode.save(filepath, scale=3, border=0)

    def create_kanban_card(self):
        """
        Generate a Kanban card PDF.
        """
        qrcode_path = "qrcode.png"
        self.generate_qr_code(qrcode_path)

        output_path=f"kanban-cards/{self.brand}-{self.item}-kanban.pdf"

        try:
            canvas = Canvas(output_path, pagesize=(8.5 * cm, 5.5 * cm))
            canvas.setFont("Courier", 16)

            # Item name
            canvas.setFillColor(self.default_colors["dark"])
            canvas.drawString(0.5 * cm, 4.5 * cm, self.item.upper())

            # Brand
            canvas.setFillColor(self.default_colors["light"])
            canvas.setFont("Courier", 10)
            canvas.drawString(0.5 * cm, 4.2 * cm, "Merk: " + self.brand)

            # Kanban level and quantity
            canvas.setFillColor(self.default_colors["dark"])
            canvas.drawString(0.5 * cm, 3 * cm, "Kanban: " + str(self.kanban_level))
            canvas.drawString(0.5 * cm, 2.7 * cm, "Aantal: " + str(self.order_qty))

            # Store
            canvas.setFillColor(self.default_colors["light"])
            canvas.drawString(0.5 * cm, 2.4 * cm, "Winkel: " + str(self.store))

            # QR Code
            qrcode_image = ImageReader(qrcode_path)
            canvas.drawImage(qrcode_image, 6.2 * cm, 0.2 * cm, 2 * cm, 2 * cm)

            # Save PDF
            canvas.save()

        finally:
            # Clean up the QR code image
            if os.path.exists(qrcode_path):
                os.remove(qrcode_path)