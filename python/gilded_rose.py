# -*- coding: utf-8 -*-

from item_updater import update_aged_brie

class GildedRose(object):

    def __init__(self, items = None):
        self.items = items

    def _update_aged_brie(self, item):
        item._change_quality(1)
        item._change_sell_in(-1)

    def _update_backstage_passes(self, item):
        if item.sell_in > 10:
            item._change_quality(1)
            item._change_sell_in(-1)
        elif 5 < item.sell_in < 10:
            item._change_quality(2)
            item._change_sell_in(-1)
        elif 0 < item.sell_in < 5:
            item._change_quality(3)
            item._change_sell_in(-1)
        else:
            item.quality = 0
            item._change_sell_in(-1)

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
                continue
            elif item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)
                continue
            elif item.quality > 0:
                if item.sell_in <= 0:
                    item._change_quality(-2)
                    item._change_sell_in(-1)
                else:
                    item._change_sell_in(-1)
            elif item.quality == 0:
                item._change_sell_in(-1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def _change_sell_in(self, change):
        self.sell_in = self.sell_in + change
    
    def _change_quality(self, change):
        self.quality = self.quality + change