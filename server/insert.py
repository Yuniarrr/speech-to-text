import pymongo

myclient = pymongo.MongoClient("mongodb://user:pass1234@localhost:27017/")
mydb = myclient["halodoc"]
mycol = mydb["medicine"]

# mylist = [
#     {"slug": "paramex-flu-dan-batuk-pe-4-tablet",
#         "ratings": "4", "coordinate": "-7.289646115762818, 112.79297032212878"},
#     {"slug": "paramex-flu-dan-batuk-4-tablet",
#         "ratings": "4.5", "coordinate": "-7.289050156711579, 112.80000843855835"},
#     {"slug": "bodrex-flu-dan-batuk-berdahak-pe-4-kaplet",
#         "ratings": "5", "coordinate": "-7.290540052852883, 112.80099549147226"},
#     {"slug": "bodrex-flu-dan-batuk-tidak-berdahak-pe-4-kaplet",
#         "ratings": "4.1", "coordinate": "-7.280304575365306, 112.78790559993469"},
#     {"slug": "bodrex-flu-dan-batuk-berdahak-pe-sirup-60-ml",
#         "ratings": "5", "coordinate": "-7.2910529009371166, 112.80325991527874"},
#     {"slug": "panadol-flu-dan-batuk-3-strip-10-kaplet-strip-hemat-borongan",
#         "ratings": "4.5", "coordinate": "-7.2806295603016, 112.78374109252611"},
#     {"slug": "obh-combi-plus-batuk-flu-madu-sirup-100-ml", "ratings": "5",
#         "coordinate": "-7.28910077727788, 112.78580102904212"},
#     {"slug": "hufagrip-flu-dan-batuk-sirup-60-ml", "ratings": "5",
#         "coordinate": "-7.279863311675731, 112.78206739410692"},
#     {"slug": "panadol-flu-dan-batuk-10-kaplet",
#         "ratings": "3", "coordinate": "-7.283439127394398, 112.7763596533439"},
#     {"slug": "obh-combi-plus-batuk-flu-menthol-100-ml", "ratings": "4.3",
#         "coordinate": "-7.282800590964701, 112.78781805021399"}
# ]

# x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# define the column you want to delete
column_to_delete = 'apotek'

# loop through every document in the collection and delete the column
for doc in mycol.find():
    if column_to_delete in doc:
        del doc[column_to_delete]
        mycol.replace_one({'_id': doc['_id']}, doc)
