test_data = [
    {
        "data": "data 1",
        "foo": "bar",
    },
    {
        "data": "data 2",
        "foo": 123,
    },
    {
        "data": "data 3",
        "bar": "321",
    },
    {
        "data": {
            "data": "data 11",
            "bar": "foo",
        },
        "foo": "bar"
    },
    {
        "baz": "bar",
        "data": {
            "other_data": None,
            "data": {
                "data": "data 22"
            }
        }
    },
    {"data": {
        "foo": 789
        }
    }
]


tmp = [i['data'] for i in test_data if 'data' in i.keys()]
res = []
for i in tmp:
    while type(i) == dict and 'data' in i:
        i = i['data']








