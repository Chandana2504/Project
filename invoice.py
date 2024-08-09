import fpdf
from transaction import Sale,Returns
class Invoice:
    def __init__(self, invoice_id, transactions, products):
        """
        Initialize a new invoice.

        :param invoice_id: Unique identifier for the invoice
        :param transactions: List of transactions to include in the invoice
        :param products: Dictionary of product_id to Product objects
        """
        self.invoice_id = invoice_id
        self.transactions = transactions
        self.products = products

    def generate_pdf(self, filename):
        """
        Generate a PDF file for the invoice.

        :param filename: Name of the PDF file to save
        """
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Header
        pdf.cell(200, 10, txt="Invoice", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Invoice ID: {self.invoice_id}", ln=True, align='L')
        pdf.cell(200, 10, txt=" ", ln=True, align='L')  # Blank line

        # Transaction details
        for transaction in self.transactions:
            product = self.products.get(transaction.product_id, None)
            if product:
                pdf.cell(200, 10, txt=f"Transaction ID: {transaction.transaction_id}", ln=True, align='L')
                pdf.cell(200, 10, txt=f"Product ID: {transaction.product_id}", ln=True, align='L')
                pdf.cell(200, 10, txt=f"Product Name: {product.name}", ln=True, align='L')
                pdf.cell(200, 10, txt=f"Category: {product.category}", ln=True, align='L')
                pdf.cell(200, 10, txt=f"Quantity: {transaction.quantity}", ln=True, align='L')
                pdf.cell(200, 10, txt=f"Date: {transaction.date}", ln=True, align='L')
                if isinstance(transaction, Sale):
                    pdf.cell(200, 10, txt=f"Sale Price: {transaction.sale_price}", ln=True, align='L')
                elif isinstance(transaction, Returns):
                    pdf.cell(200, 10, txt=f"Reason for Return: {transaction.reason}", ln=True, align='L')
                pdf.cell(200, 10, txt=" ", ln=True, align='L')  # Blank line

        # Save the PDF
        pdf.output(filename)

