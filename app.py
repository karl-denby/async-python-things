from bocadillo import App, Templates, static

app = App(static_dir='dist', static_config={"max_age": 30})
app.mount(prefix='js', app=static('dist/js'))
app.mount(prefix='css', app=static('dist/css'))
app.mount(prefix='img', app=static('dist/img'))

templates = Templates(app, directory='dist')

@app.route("/")
async def root(req, res):
    res.html = await templates.render('index.html')

@app.websocket_route("/conversation")
async def converse(ws, diego, save_client):
    with save_client(ws):
        async for message in ws:
            response = diego.get_response(message)
            await ws.send(str(response))

@app.route("/client-count")
async def client_count(req, res, clients):
    res.media = {"count": len(clients)}

if __name__ == "__main__":
    app.run()
