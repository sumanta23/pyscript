from pyscript import pyscript
import io
import unittest
import unicodedata

class TermTest(unittest.TestCase):
    def exe(self,command):
        session = pyscript.open("https://localhost:8443")

        response = session.terminal().execute(command);

        if type(response) is tuple:
            filename = response[0]
            content = response[1]
            with io.open(filename, 'wb') as handle:
                handle.write(content)
        else:
            line = response.get_output()
            print(line)
            return line

        pyscript.close(session)

    def fetchSerialNo(self,res):
        serialno = res
        s = serialno.split('\t')
        s=s[2]
        return s

    def test_commands(self):
        rstr = '<serialno>'
        serialno = None
        fd = open("commands",'rb')
        for line in fd.readlines():
            line = str(line, "utf-8")
            if rstr in line:
                line = line.replace(rstr,serialno)
            print('executing: ' + line)
            res = self.exe(line)
            if res is not None and len(res) > 6:
                res = unicodedata.normalize('NFKD',res).encode('ascii','ignore')
                serialno = self.fetchSerialNo(res)


if __name__ == '__main__':
    unittest.main()
