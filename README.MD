### Code for implementing map and reduce functions for Hadoop

### Data will be like

| Country | Year | Code   | Commodity      | Flux   | Value | Weight | Unit            | Quantity | Category        |
| ------- | ---- | ------ | -------------- | ------ | ----- | ------ | --------------- | -------- | --------------- |
| Brasil  | 2017 | 010410 | Sheep, live    | Export | 6088  | 2339   | Number of items | 51       | 01_live_animals |
| Chile   | 2015 | 010410 | Elephant, live | Import | 16288 | 222339 | Number of items | 12       | 01_live_animals |

### Command to run functions just for 199 first lines of base

```
head -199 data.csv | python map.py | sort | python reduce.py
```
