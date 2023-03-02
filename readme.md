# mucking about

## Dependencies

Server is running on flask.

```sh
cd server
pip install -r requirements.txt
cd ..
```

## Server

To run the server

```sh
npm run server
```

Should start on port 5000

Give it a wink and a nudge:

```sh
curl -X POST -H "Content-Type: application/json" -d '' http://localhost:5000/
```

and you will get back

```json
{
    "perks": [1, 2, 3, 4, 5]
}
```

Well done you.

## Client

Just a single page.

to run the client

```sh
npm run client
```

## Run the whole lot

```sh
npm run start
```

This uses a library called concurrently to run both the server and the client at the same time. It's fab.

## Show CORS working / not working

Remove / comment out the cors header being sent back to the client in `server.py`:

    ```python
        #response.headers.add('Access-Control-Allow-Origin', '*')
    ```
