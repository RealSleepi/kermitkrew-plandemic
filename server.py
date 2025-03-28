# importing all the functions 
# from http.server module 
from http.server import *
from server_utils import get_homepage_content  # Import the function from the second file

# creating a class for handling 
# basic Get and Post Requests 
class PyDevServer(BaseHTTPRequestHandler): 
	
	# creating a function for Get Request 
	def do_GET(self): 
		
		# Success Response --> 200 
		self.send_response(200) 
		
		# Type of file that we are using for creating our 
		# web server. 
		self.send_header('content-type', 'text/html') 
		self.end_headers() 
		
		# Get the homepage content from the utility function
		content = get_homepage_content()
		self.wfile.write(content.encode('utf-8'))  # Encode the string to bytes before writing
			

# this is the object which takes port 
# number and the server-name 
# for running the server 
port = HTTPServer(('', 80), PyDevServer) 

# this is used for running our 
# server as long as we wish 
# i.e. forever 
port.serve_forever() 
