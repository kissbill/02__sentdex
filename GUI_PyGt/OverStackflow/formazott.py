def createfile():
    var = """#!/bin/sh\necho ${test}"""
    funcToCreateScript(filename,var)

def createfile():
    #involved. 
    var = """#!/bin/sh
echo ${test}
          """
    return funcToCreateScript(filename,var)

def createfile():
    var = """
#!/bin/sh
echo ${test}
          """
    return var

v = createfile()

print(v)