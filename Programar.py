import wexpect

def Programar(selectFile, IdAutentication=""):
    command = '"C:\\Program Files (x86)\\Renesas Electronics\\Programming Tools\\Renesas Flash Programmer V3.12\\rfp-cli.exe" -d rx200 -t e2l -vo 3.3 -a '
    command = command + "'{}'".format(selectFile)
    print(command)
    child = wexpect.spawn(command, timeout=30)
   
    try:
        codigo_autenticacion = IdAutentication
        child.expect('Enter ID Code (16 Bytes)?')
        child.sendline(codigo_autenticacion)
        child.expect(wexpect.EOF)
    
    except wexpect.wexpect_util.EOF:
        pass


# print(len('45CAFEC0FFEECAFEC0FFEECAFEC0FFEE'))
# print(len("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"))
