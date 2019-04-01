from bocadillo import App
from chatbot import diego

app = App()

@app.websocket_route("/conversation")
async def converse(ws):
    async for message in ws:
        response = diego.get_response(message)
        await ws.send(str(response))

if __name__ == "__main__":
    app.run()
