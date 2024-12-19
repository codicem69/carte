# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        root.thpage(u"!![it]Proprietari Carte", table="carte.proprietario", multipage="True", tags="")
        root.thpage(u"!![it]Movimenti", table="carte.movimenti", multipage="True", tags="")
        root.thpage(u"!![it]Carte", table="carte.carta", multipage="True", tags="")
        root.thpage(u"!![it]Banche", table="carte.banca", multipage="True", tags="")
