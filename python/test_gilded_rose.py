# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # the quality of an item is never negative
    def test_quality_never_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # once the sell date has passed, items.quality will degrade twice as fast.
    def test_past_sell_date(self):
        items = [Item("foo", sell_in=0, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    # "Aged Brie" actually increases in Quality the older it gets
    def test_aged_brie_quality_increase(self):
        item = Item("Aged Brie", sell_in=0, quality=4)
        gilded_rose = GildedRose()
        gilded_rose._update_aged_brie(item)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(5, item.quality)
        
    # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def test_sulfuras(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches
    def test_backstage_passes_sell_in_over_ten(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
        gilded_rose = GildedRose()
        gilded_rose._update_backstage_passes(item)
        self.assertEqual(14, item.sell_in)
        self.assertEqual(21, item.quality)

    # "Backstage passes" Quality increases by 2 when there are 10 days or less
    def test_backstage_passes_sell_in_under_ten(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=20)
        gilded_rose = GildedRose()
        gilded_rose._update_backstage_passes(item)
        self.assertEqual(8, item.sell_in)
        self.assertEqual(22, item.quality)

    # "Backstage passes" Quality increases by 3 when there are 5 days or less
    def test_backstage_passes_sell_in_under_five(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=20)
        gilded_rose = GildedRose()
        gilded_rose._update_backstage_passes(item)
        self.assertEqual(3, item.sell_in)
        self.assertEqual(23, item.quality)

    # "Conjured" items degrade in Quality twice as fast as normal items
    # def test_conjured_items(self):
    #     items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual(2, items[0].sell_in)
    #     self.assertEqual(4, items[0].quality)


if __name__ == '__main__':
    unittest.main()
