class DocumentProcessor:
    def __init__(self):
        self.documents = {}
    
    def add_document(self, doc_id, content):
        """Add a document to the collection."""
        self.documents[doc_id] = content
    
    def get_document(self, doc_id):
        """Retrieve a document by ID."""
        return self.documents.get(doc_id, "Document not found")
    
    def search_text(self, query):
        """Basic search function."""
        results = []
        for doc_id, content in self.documents.items():
            if query.lower() in content.lower():
                results.append((doc_id, content))
        return results