from quart import Quart, render_template, request, redirect, url_for

app = Quart(__name__)

posts = []

@app.route('/')
async def home():
    return await render_template('home.html', posts=posts)

@app.route('/create_post', methods=['POST'])
async def create_post():
    data = await request.form
    content = data.get('content')
    user = data.get('user')
    if content:
        posts.append({'user': user, 'content': content})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
