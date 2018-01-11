from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response", methods=['GET', 'POST'])
def render_response():
    error = None
    color = request.forms['color']
    #the request object stores data about the request sent to the server
    # args is a MultiDict (like a dictionary, but can store multiple values for the same key)
    # the information in args is visible in the url for the page  being requested (i.e. ... /response?color=blue)
    if request.method == 'POST':
        if color == 'red':
            reply = "gg"
        else:
            reply = "Get good red is the true A1 color."
        return render_template('response.html', response = reply)
    else:
        reply = "go away stupid"
        error = 'dummy'
        return render_template('response.html', response = reply, error = error)
if __name__=="__main__":
    app.run(debug=False, port=54321)
