from docx import Document

doc = Document("D:\\University\\Thesis\\ENGG4093-Project\\example\\Hello World.docx")

print("Paragraphs: ")
for para in doc.paragraphs:
    print(f"-{para.text}")
