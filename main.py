from flask_bootstrap import Bootstrap

from website_management import *
from url_endpoints import *

bootstrap = Bootstrap(app)

if __name__ == "__main__":
    app.run(debug=True)