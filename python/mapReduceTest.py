import csv;

file = open('../data.csv');
csvReader = csv.reader(file);
occurency = {};

for line in csvReader:
    fields = line[0].split(';');

    country = fields[0];
    year = fields[1];
    code = fields[2];
    commodity = fields[3];
    flux = fields[4];
    value = fields[5];
    weight = fields[6];
    unit = fields[7];
    quantity = fields[8];
    category = fields[9];

    # What will be generated as key value and should be usedin the Shuffle function (automatic one)

    if country == "Albania":


        rawRows = '%s\t%s' % (commodity, "1");



        print(rawRows);

    # Reduce function - simulating getting the values one by one in another step (after the Shuffle function)

        key, value = rawRows.split('\t', 1);

        try:
            value = int(value);
        except:
            continue;
        try:
            occurency[key] = occurency[key]+value;
        except:
            occurency[key] = value;

    for country in occurency.keys():
        print('%s\t%s' % (occurency[country], country));
