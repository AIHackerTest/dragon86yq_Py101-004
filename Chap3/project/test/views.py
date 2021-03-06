from flask import render_template, Flask, request
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index3.html",
        title = 'Home',
        user = user,
        posts = posts)

if __name__ == '__main__':
    app.run(debug=True)




