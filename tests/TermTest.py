from pyscript import pyscript
import io

session = pyscript.open("https://localhost:8443")
#response = session.terminal().execute("list rootca")
response = session.terminal().execute("export -cat keystore rootca -serialno 1448654747524 -filename d.p12 -format p12");


if type(response[1]) is bytearray:
    filename = response[0]
    content = response[1]
    with io.open(filename, 'wb') as handle:
        handle.write(content)
else:
    line = response.get_output()
    print line

pyscript.close(session)
