import os
from PyPDF2 import PdfFileMerger
from fpdf import FPDF
from PIL import Image

# Diretórios de entrada e saída (substitua pelo caminho absoluto do seu input e output)
input_dir = r'C:/workspace/projeto_py/input'
output_dir = r'C:/workspace/projeto_py/output'

# Lista de extensões suportadas para conversão
supported_extensions = ['.txt', '.csv', '.tif', '.tiff', '.png', '.jpg', '.jpeg']

# Função para converter arquivos para PDF
def convert_to_pdf(input_path, output_path, filename):
    if input_path.lower().endswith(('.tif', '.tiff', '.png', '.jpg', '.jpeg')):
        img = Image.open(input_path)
        img.save(os.path.join(output_path, f'{filename}.pdf'), 'PDF')
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        with open(input_path, 'r', encoding='utf-8') as file:
            for line in file:
                pdf.cell(200, 10, txt=line, ln=True)

        pdf.output(os.path.join(output_path, f'{filename}.pdf'))

# Percorre arquivos na pasta de entrada
for filename in os.listdir(input_dir):
    if filename.lower().endswith(tuple(supported_extensions)):
        file_path = os.path.join(input_dir, filename)
        pdf_filename = os.path.splitext(filename)[0]
        convert_to_pdf(file_path, output_dir, pdf_filename)

# Combina todos os PDFs gerados em um único arquivo
pdf_merger = PdfFileMerger()
for pdf_filename in os.listdir(output_dir):
    if pdf_filename.endswith('.pdf'):
        pdf_path = os.path.join(output_dir, pdf_filename)
        pdf_merger.append(pdf_path)

output_pdf_path = os.path.join(output_dir, 'combined.pdf')
pdf_merger.write(output_pdf_path)
pdf_merger.close()

print('Conversão para PDF realizada com sucesso!')
