from cc1_levelset_proto import CC1TileCodes, CC1Levels

class CC1LevelsetTransformer:
    def transform(self, levels, old, new):
        if isinstance(levels, Levelset):
            levels = levels.levels
        if isinstance(levels, Level):
            levels = [levels]
        if isinstance(old, int):
            old = [old]
        for level in levels:
            for pos, tspec in level.map.items():
                if CC1Levels.remove(level, pos, old):
                    CC1Levels.add(level, pos, new)
                elif CC1TileCode.FLOOR in old: # since FLOOR is default, it doesn't ever get removed
                    if tspec.top == CC1TileCode.FLOOR or (tspec.top in CC1TileCodes.ENTITIES and tspec.bottom == CC1TileCode.FLOOR):
                        CC1Levels.add(level, pos, new)
    
    def keep(self, levels, old):
        if isinstance(old, int):
            old = set((old,))
        old = set(old)
        self.transform(levels, CC1TileCodes.ALL.difference(old), CC1TileCode.FLOOR)
    
    def walls_of(self, levels, walls=CC1TileCodes.WALLS, *, keep_panels=True):
        if keep_panels:
            walls.update(CC1TileCodes.PANELS)
        return self.keep(levels, walls)
    
    def mobs_of(self, levels, mobs=CC1TileCodes.ENTITIES, *, keep_cloners=True):
        if keep_cloners:
            mobs.add(CC1TileCode.CLONER)
        return self.keep(levels, mobs)
    
    # for a different mob, replace blobs with CC1TileCodes.TEETH for example
    def blobs_edition(self, levels, blobs=CC1TileCodes.BLOBS):
        for d in "NESW":
            targets = set(tuple(mob for mob in CC1TileCodes.MONSTERS if CC1TileCode.Name(mob).endswith(f"_{d}")))
            replace = tuple(mob for mob in blobs if CC1TileCode.Name(mob).endswith(f"_{d}"))
            print(targets)
            print(replace)
            self.transform(levels, targets, replace[0])