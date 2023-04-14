class Document:
    def __init__(self,doc_name,doc_id,page_no,issue_date,pdf_link,html_link,classfication, found_keys, transaction_size, market_of_listing):
        self.doc_name = doc_name
        self.doc_id = doc_id
        self.page_no = page_no
        self.issue_date = issue_date
        self.pdf_link = pdf_link
        self.html_link = html_link
        self.classfication = classfication
        self.found_keys  = found_keys
        self.transaction_size = transaction_size
        self.market_of_listing = market_of_listing