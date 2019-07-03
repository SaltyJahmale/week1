from flask import Flask, request, escape


app = Flask(__name__)

# exercise 1.1 Show the User-Agent header of HTTP requests
# @app.route('/')
# def hello_world():
#     request_example = request.headers.get('user-agent')
#
#     return request_example

# exercise 1.2 custom user-agent value of ‘<script>alert("Hi!")</script>’
# @app.route('/')
# def hello_world():
#     request_example = request.headers.get('user-agent')
#
#     mode = 'safe'
#
#     if mode == 'safe' :
#         return escape(request_example)
#     else :
#         return request_example

# exercise 1.3 Show all HTTP headers
@app.route('/')
def hello_world():
    return str(request.headers)


if __name__ == '__main__':
    app.run(debug=True)