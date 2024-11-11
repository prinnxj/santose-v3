from document_processor import DocumentProcessor

def main():
    # Create processor
    processor = DocumentProcessor()
    
    # Add sample legal text
    processor.add_document(
        "constitution_27",
        """มาตรา ๒๗ บุคคลย่อมเสมอกันในกฎหมาย มีสิทธิและเสรีภาพและได้รับความคุ้มครอง
        ตามกฎหมายเท่าเทียมกัน
        การเลือกปฏิบัติโดยไม่เป็นธรรมต่อบุคคล ไม่ว่าด้วยเหตุความแตกต่างในเรื้องถิ่นกำเนิด
        เชื้อชาติ ภาษา เพศ อายุ ความพิการ จะกระทำมิได้"""
    )
    
    # Test search
    print("\n🔍 Searching for 'เสมอภาค':")
    results = processor.search_text("เสมอภาค")
    for doc_id, content in results:
        print(f"\nFound in {doc_id}:")
        print(content)
    
    # Test document retrieval
    print("\n📄 Getting document 'constitution_27':")
    doc = processor.get_document("constitution_27")
    print(doc)

if __name__ == "__main__":
    main()