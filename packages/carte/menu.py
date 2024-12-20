# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        user=self.db.currentEnv.get('user')
        taguser = self.db.currentEnv.get('userTags')
        tag_user=taguser.split(',')

        if 'admin' in tag_user or 'superadmin' in tag_user or '_DEV_' in tag_user:
            carte = root.branch(u"carte", tags="")
            carte.packageBranch('Amministrazione sistema',pkg='adm')#, branchMethod='userSubmenu')
            carte.packageBranch('System',pkg='sys')
            carte.packageBranch('Email',pkg='email')
            carte.packageBranch('Unlocode',pkg='unlocode')
            carte.packageBranch('Agencies',pkg='agz')

            carte.thpage(u"!![it]Proprietari Carte", table="carte.proprietario", multipage="True", tags="")
            carte.thpage(u"!![it]Movimenti", table="carte.movimenti", multipage="True", tags="")
            carte.thpage(u"!![it]Carte", table="carte.carta", multipage="True", tags="")
            carte.thpage(u"!![it]Banche", table="carte.banca", multipage="True", tags="")
        else:
            carte = root.branch(u"carte", tags="")
            agz = root.branch(u"Agencies", tags="")
            agz.thpage(u"Staff", table="agz.staff", tags="")
            carte.thpage(u"!![it]Proprietari Carte", table="carte.proprietario", multipage="True", tags="")
            #carte.thpage(u"!![it]Movimenti", table="carte.movimenti", multipage="True", tags="")
            carte.thpage(u"!![it]Carte", table="carte.carta", multipage="True", tags="")
            carte.thpage(u"!![it]Banche", table="carte.banca", multipage="True", tags="")
            carte.packageBranch('Unlocode',pkg='unlocode')
