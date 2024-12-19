# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('banca', pkey='id', name_long='!![it]Banca', name_plural='!![it]Banche',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('nome', name_short='!![it]Nome Banca')
        tbl.column('filiale', name_short='!![it]Filiale')
        

        