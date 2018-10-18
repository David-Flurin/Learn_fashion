from tg import expose, TGController, AppConfig
from wsgiref.simple_server import make_server
import cgi
from webob import Request

class RootController(TGController):
    @expose()
    def index(self, upload, **kw):
      Request.POST['upload']
      print(kw)
      #form = cgi.FieldStorage()
      return 'Hello World'
    @expose("Server.templates.example")
    def example(self):
    	mydata = {'person':'Kanye West','office':'President'}
    	return mydata




config = AppConfig(minimal=True, root_controller=RootController())
application = config.make_wsgi_app()
print("Serving on port 8080...")
httpd = make_server('', 8080, application)
httpd.serve_forever()