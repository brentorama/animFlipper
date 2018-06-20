import maya.cmds as cmd
import maya.mel as mel

def flipIt()):
    r=[[0,0,0],[0,0,0],[0,0,0]]
    l=[[0,0,0],[0,0,0],[0,0,0]]
    userAttsL = ['']
    userAttsR = ['']
    selL = ['']
    selR = ['']

    #define naming conventions.

    right = ['right', '_R_']
    left = ['left', '_L_']

    #store your selection

    for r, l in (right, left):
        storeR = cmd.ls(sl=True, ("*:*"+r+"*"))
        storeL = cmd.ls(sl=True, ('*:*'+l+'*'))

    selL.append(storeL)
    selR.append(storeR)

    lenR = len(selR)
    lenL = len(selL)

    #get the values(Can we combine this into one function?)

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
    if lenL:
        for i in range(lenL):
            ob = selL[i]
            l[0]= cmd.getAttr(ob+'.t')
            l[1]= cmd.getAttr(ob+'.r')
            l[2]= cmd.getAttr(ob+'.s')
            userAtts = cmd.listAttr(ob, ud = True, k = True)
                for att in userAtts:
                    value = cmd.getAttr('%s.%s' % (ob, att))
                    userAttsL.append('setAttr %s.%s %s' % (ob, att, value)

    print userAttsL
    print userAttsR

    #perform left and right flip

    if lenR: 
        doFlip(1, lenR, selR, left, right, r, userAttsR);
    if lenL:
        doFlip(0, lenL, selL, left, right, l, userAttsL);    

# This function goes through all possible 'right' and 'left' protocols
# and also through all selected objects and applies the stored R transforms to L
# and vice versa, finally executing the userAttributes commands

def doFlip(isR =0, length= 0, sel ='',left=[''],right=[''], trans=[[0,0,0],[0,0,0],[0,0,0]], userAtt=['']):
    string this, that, name
    for i in range(length):
        for l in left:
            for r in right:
                this = r and that = l if (isR == 1) else this = l and that = r
                if this is in sel[i]:
                    name = sel[i].replace(this, that)
                    if (cmd.objExists(name)):
                        cmd.move    (a=True, ls=True, trans[i][0], name)
                        cmd.rotate  (a=True, ls=True, trans[i][1], name)
                        cmd.scale   (a=True, ls=True, trans[i][2], name)
                        for one in userAtt:
                            command = one.replace(this, that)
                            mel.eval(command)