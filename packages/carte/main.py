#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='carte package',sqlschema='carte',sqlprefix=True,
                    name_short='Carte', name_long='carte', name_full='Carte')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
