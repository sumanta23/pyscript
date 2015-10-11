from pyscript import pyscript
import io

session = pyscript.open("https://localhost:8443")
response = session.terminal().execute("list rootca")

if type(response) is bytearray:
    with io.open('tb.crt', 'wb') as handle:
        handle.write(response)
else:
    line = response.get_output()
    print line

pyscript.close(session)


