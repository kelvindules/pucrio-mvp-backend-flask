from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote

from model import Session
from model.product import Product

from schemas import *

info = Info(title="Product API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

doc_product_tag = Tag(name="Produto", description="CRUD de produtos")

@app.post('/products', tags=[doc_product_tag], responses={"200": ProductViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_product(form: ProductCreateUpdateSchema):
    new_product = Product(
        name=form.name,
        count=form.count,
        price=form.price)
    print('product: ${new_product}')
    try:
        session = Session()
        session.add(new_product)
        session.commit()
        return render_product(new_product), 200
    except IntegrityError as e:
        return {"message": "Já existe um produto com esse nome"}, 409
    except Exception as e:
        return {"message": "Não foi possível adicionar o novo produto"}, 400

@app.get('/products', tags=[doc_product_tag], responses={"200": ProductListSchema, "404": ErrorSchema})
def get_products():
    session = Session()
    products = session.query(Product).all()
    if not products:
        return {"products": []}, 200
    else:
        print(products)
        return render_products(products), 200

@app.delete('/products/<string:name>', tags=[doc_product_tag], responses={"200": ProductDeleteSchema, "404": ErrorSchema})
def delete_product(path: ProductDeleteSchema):
    session = Session()
    count = session.query(Product).filter(Product.name == unquote(unquote(path.name))).delete()
    session.commit()
    if count:
        return {"message": "Produto removido com sucesso!"}
    else:
        return {"message": "Produto não encontrado!"}, 404