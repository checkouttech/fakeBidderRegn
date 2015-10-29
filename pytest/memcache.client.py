import memcache
mc = memcache.Client(['192.168.150.110:11211'], debug=0)

mc.set("some_key", "Some value")
value = mc.get("some_key")

mc.set("another_key", 3)
mc.delete("another_key")

mc.set("key", 1)   # note that the key used for incr/decr must be a string.
print  mc.get("key")
mc.incr("key")
print  mc.get("key")
mc.decr("key")
print  mc.get("key")


print  mc.get("Remotekey")

print mc.stats

networkID = 10 
userID = "ABX2356"
mc.set(str(networkID)+""+str(userID),"this is value") 

print mc.get(str(networkID)+""+str(userID))
