import unittest
from app import app

class FlaskTest(unittest.TestCase):
    
    #Check for response 200
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get("/")
        statuscode=response.status_code
        self.assertEqual(statuscode,200)
    
    #Check if index page returns application/json
    def test_index_content(self):
        tester=app.test_client(self)
        response=tester.get("/")
        self.assertEqual(response.content_type,"application/json")
  
if __name__=="__main__":
    unittest.main()