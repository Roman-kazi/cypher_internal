from neo4j.v1 import GraphDatabase
import csv
import neo4j
from py2neo import cypher



uri = "bolt://localhost:7687"
password = "root"
user = "neo4j"

        # connecting to server

graphDB_driver = GraphDatabase.driver(uri, auth=(user, password))
session = graphDB_driver.session()
        #session.run('create(:car {name: $vehicle})',vehicle="mercedes")
with open("bloom2.csv", 'r') as file:
    reader = csv.DictReader(file)

    keys = reader.fieldnames

    node = []
    created = []
    i = 0
    graph_db = neo4j.v1.GraphDatabase()
    for line in reader:
        var1 = "test"+str(i)
        var2 = "temp"+str(i)
        call_type = str(line[keys[4]])
        number1 = line[keys[0]]
        number2 = line[keys[1]]
        status = line[keys[6]]
        start_time = str(line[keys[2]])
        end_time = str(line[keys[3]])



        session.run("MERGE ("+var1+":"+"mobile_number"+ "{ number: \""+number1+"\"})MERGE("+var2+":"+"mobile_number"+ "{ number:\""+number2+"\"})MERGE("+var1+")-[article:"+status+"{type:\""+call_type+"\",start_date:apoc.temporal.format(datetime(\""+start_time+"\"), \"dd MM yyyy\"),start_time: apoc.temporal.format(datetime(\""+start_time+"\"), \"HH:mm:ss\"),end_date:apoc.temporal.format(datetime(\""+end_time+"\"), \"dd MM yyyy\"), end_time:apoc.temporal.format(datetime(\""+end_time+"\"), \"HH:mm:ss\"),duration:  duration.inSeconds(datetime('"+ start_time +"') ,datetime('"+ end_time +"')).seconds}]->("+var2+")")

        i =i+1