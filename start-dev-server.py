from vcab.app import app

app.run(debug = True, host = '', port = 53042, master = True, processes = 8)
