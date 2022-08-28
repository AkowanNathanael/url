from flask import Flask,render_template,url_for,request,flash,abort,redirect
import os.path
import json


app=Flask(__name__)
app.secret_key="      come to me  we are the way , . 656 67o3 just the .,/33467*&%$#@!~        "


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")



@app.route("/your-url",methods=["GET","POST"])
def your_url():
     if request.method == 'POST':
        urls= {}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        if request.form['code'] in urls.keys():
            flash('That short name has already been taken. Please use another name')
            return redirect(url_for('index'))

        urls[request.form['code']] = {'url':request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file)
            
        return render_template('your_url.html', code=request.form['code'])
     else:
        return redirect(url_for('index'))
    #  return render_template("shorten.html")


@app.route("/shorten")
def shorten():
    return render_template("shorten.html")
   

    

@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
    return abort(404)




@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html")

@app.route("/about")
def about():
    return render_template("about.html")




if __name__=="__main__":
    app.run()