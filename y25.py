me = {
    "first_name": "Mikk",
    "surname": "Maltis",
    "year_of_birth": 2006,
    "place_of_residence": "Muhu",
    "favorite_dessert": "caramel_pudding"
}

print(me.get("place_of_residence"))


me["favorite_dessert"] = "ice_cream"

del me["year_of_birth"]
print(me)

for k, v in me.items():
    print(k, v)

me["personal_code"] = "1234567890"

if "personal_code" in me:
    print("Personal identification number available")
else:
    print("There's no personal code")

print(len(me))

me = {
    "height": "1.8",
}

print(me.get("height"))



me.clear()

print(me)