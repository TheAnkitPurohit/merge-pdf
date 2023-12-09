import PyPDF2
import os

def merge_pdfs(input_folder, output_filename):
    # Create a PDF writer object

    print(input_folder)
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through all PDF files in the input folder
    for filename in os.listdir(input_folder):
        print(filename)
        if filename.lower().endswith('.pdf'):
            # Construct the full file path
            input_path = os.path.join(input_folder, filename)

            # Open each PDF file
            with open(input_path, 'rb') as pdf_file:
                # Create a PDF reader object
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Loop through each page and add it to the writer
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

    # Write the merged PDF to the output file
    with open(output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    # Specify input folder containing PDFs to merge
    input_folder = "comics"

    # Specify output filename for the merged PDF
    output_filename = "merged_output.pdf"

    # Merge PDFs
    merge_pdfs(input_folder, output_filename)
