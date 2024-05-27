from bottle import route, get, run, template, static_file

@get("/")
@get("/home")
def greet(name="home/index"):
    return template("index", name=name)


@get("/about")
@get("/aboutus")
def greet(name="aboutus/index"):
    return template("index", name=name)

@get("/products")
@get("/ourproducts")
def greet(name="products/index"):
    return template("index", name=name)

@get("/product")
def product(name="products/product"):
    return template("index", name=name)

@get("/services")
@get("/ourservices")
def greet(name="services/index"):
    return template("index", name=name)

@get("/gallery")
def greet(name="gallery/index"):
    return template("index", name=name)

@get("/contacts")
@get("/contactus")
def greet(name="contacts/index"):
    return template("index", name=name)

@route("/images/<filename>")
def send_image(filename):
    return static_file(filename, root="./imgs")

run(host="localhost", port=8080, debug=True, reload=True)