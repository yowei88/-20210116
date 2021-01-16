from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
a=random.randrange(0,16)
for j in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+j
    for i in range(10):
        r=random.randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)
while True:
    h=mc.events.pollBlockHits()
    if len(h)>0:
        t=h[0]
        b=mc.getBlockWithData(t.pos)
        d=b.data
        if d==a:
            mc.postToChat("u find meeeeeeeeeeeeee")
            mc.setBlock(t.pos,46)
            break
        elif d>a:
            mc.postToChat('wrong smaller')
        elif d<a:
            mc.postToChat('wrong bigger')
