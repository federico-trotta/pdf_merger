import PyPDF2
import os

def combine_pdfs_in_current_folder(output_filename):
    """
    Combines all PDF files in the current folder into a single PDF.
    
    :param output_filename: The name of the output PDF file.
    """
    pdf_writer = PyPDF2.PdfWriter()

    # Get a list of all files in the current folder
    files = os.listdir()

    # Loop through the files in the current folder
    for file_name in files:
        # Check if the file is a PDF
        if file_name.lower().endswith('.pdf'):
            try:
                pdf_reader = PyPDF2.PdfReader(file_name)
                # Add all pages of each PDF to the writer object
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)
                print(f"Added {file_name}")
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
        else:
            print(f"Skipping non-PDF file: {file_name}")

    # Write the combined PDF to a new file
    with open(output_filename, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"PDFs combined successfully into {output_filename}")


if __name__ == "__main__":
    # Desired name for the combined PDF
    output_pdf = "combined_output.pdf"

    # Combine PDFs from the current folder
    combine_pdfs_in_current_folder(output_pdf)
