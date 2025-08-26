class Response:
    def __init__(self, is_success, data, status_code=200):
        self.data = data
        self.is_success = is_success
        self.status_code = status_code
        
    def to_dict(self):
        return {
            "is_success": self.is_success,
            "data": self.data
        }