import pymupdf #biblioteca para conversão

# Abrindo o arquivo PDF
pdf_document = pymupdf.open("C:\\Users\\leonardo\\Desktop\\trabalho-estrutura-de-dados\\testePDF\pdfteste1.pdf")
# Extraindo texto de cada p´agina
with open("documento.txt", "w", encoding="utf-8") as txt_file:
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        txt_file.write(text + "\n")
pdf_document.close()