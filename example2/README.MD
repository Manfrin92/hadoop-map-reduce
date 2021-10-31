### Code for implementing map and reduce functions for Hadoop

### Data will be like

| Id  | IdAuthor | CreationDate | Tweet                                                       |
| --- | -------- | ------------ | ----------------------------------------------------------- |
| 1   | Empresa1 | 010410       | Sheep, Empresa1, sSheep?                                    |
| 2   | clienteX | 010410       | Elephant, Empresa2, worst, bad, never, horrible ou terrible |
| 3   | clienteX | 010410       | Elephant, Empresa1                                          |

### Command to run functions just for 199 first lines of base

```
head -199 data.csv | python map.py | sort | python reduce.py
```
