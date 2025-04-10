from pydantic import BaseModel
import json
from product import Product

class jsonDB(BaseModel):
    path: str

    def read(self):
        f = open(self.path)
        data = json.loads(f.read())
        f.close()
        return data
    
    def insert(self, product: Product):
        data = self.read()
        data['products'].append(product.dict())
        f = open(self.path, 'w')
        f.write(json.dumps(data))
        f.close()