import fitz  
import re
import os

count = 1

path = r'C:\\Users\\leonardo\\Desktop\\trabalho-estrutura-de-dados\\testePDF'

for file in os.listdir(path):
    if re.search('pdf', file):
        print(file)
        caminho_txt = "C:\\Users\\leonardo\\Desktop\\trabalho-estrutura-de-dados\\result\\doc" + str(count) + ".txt"
        pdf_document = fitz.open("C:\\Users\\leonardo\\Desktop\\trabalho-estrutura-de-dados\\testePDF\\" + file)
        with open(caminho_txt, "w", encoding="utf-8") as txt_file:
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                text = page.get_text()
                txt_file.write(text + "\n")
            pdf_document.close()
        count += 1
        
