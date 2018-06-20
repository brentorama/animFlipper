import maya.cmds as cmd

def flipIt()):
    r=[[0,0,0],[0,0,0],[0,0,0]]
    l=[[0,0,0],[0,0,0],[0,0,0]]
    userAttsL, = ['']
    userAttsR = ['']
    selL = ['']
    selR = ['']

    #define naming conventions.
    right = ['right', '_R_']
    left = ['left', '_L_']

    #store your selection

    for r, l in (right, left):
        storeR = cmd.ls(sl=True, ("*:*"+r+"*"))
        storeL = cmd.ls(sl=True, ("*:*"+l+"*"))

    selL.append(storeL)
    selR.append(storeR)
    lenR = len(selR)
    #get the values
    if lenR:
        for i in range(lenR):
            ob = selR[i]
            r[0]= cmd.getAttr(ob+'.t')
            r[1]= cmd.getAttr(ob+'.r')
            r[2]= cmd.getAttr(ob+'.s')
            userAtts = cmd.listAttr(ob, ud = True, k = True)
                for att in userAtts:
                    value = cmd.getAttr('%s.%s' % (ob, att))
                    userAttsR.append('setAttr %s.%s %s' % (ob, att, value)

    