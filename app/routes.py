from app.services.exchangeRates.views import exchangeRates_bp
from app.services.weather.views import weather_bp
from app.services.localidade.views import localidade_bp
from app.services.shopping.shoppingList.views import shoppingList_bp
from app.services.shopping.store.views import store_bp
from app.services.shopping.product.views import product_bp
from app.services.shopping.productPrice.views import productPrice_bp

def register_routes(app):
    app.register_blueprint(exchangeRates_bp, url_prefix='/api/exchangeRates')
    app.register_blueprint(weather_bp, url_prefix='/api/weather')
    app.register_blueprint(localidade_bp, url_prefix='/api/localidade')
    app.register_blueprint(shoppingList_bp, url_prefix='/api/shoppingList')
    app.register_blueprint(store_bp, url_prefix='/api/store')
    app.register_blueprint(product_bp, url_prefix='/api/product')
    app.register_blueprint(productPrice_bp, url_prefix='/api/productPrice')
    

