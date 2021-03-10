import logging
import math
import random
import time

log = logging.getLogger(__name__)

def clear_database(db):
    """Clear the database."""

    db.execute_query("MATCH (n) DETACH DELETE n")
    log.info("Database cleared")

def init_data(db, raw_supplier_count, supplier_count):
    start_time = time.time()
    db.execute_query(f'CREATE (p:Product {{ name : "Product", lat: {tan(rand())*100}, lon: {tan(rand())*100}, co2: {200}, cost: {100}, time: {0}}} )')
    
    for i in range(0, 2):
        db.execute_query(f'CREATE (w:Wholesaler {{name : "Wholesaler" + {str(i)}, cost: {round(exp(rand()*3)+20)}, co2: {round(exp(rand()*8)+250)}, lat: {tan(rand())*100}, lon: {tan(rand())*100},  time: {round(rand()*5)} }} )')

    for i in range(0, supplier_count):
        db.execute_query(f'CREATE (sa:SupplierA {{name : "SupplierA" + {str(i)}, cost: {round(exp(rand()*3)+20)}, co2: {round(exp(rand()*8)+250)}, lat: {tan(rand())*100}, lon: {tan(rand())*100},  time: {round(rand()*5)} }} )')
    
    for i in range(0, supplier_count/2):
        db.execute_query(f'CREATE (sb:SupplierB {{name : "SupplierB" + {str(i)}, cost: {round(exp(rand()*3)+20)}, co2: {round(exp(rand()*8)+250)}, lat: {tan(rand())*100}, lon: {tan(rand())*100},  time: {round(rand()*5)} }} )')
    
    for i in range(0, 2*raw_supplier_count):
        db.execute_query(f'CREATE (r:Retailer {{name : "Retailer" + {str(i)}, cost: {round(exp(rand()*3)+20)}, co2: {round(exp(rand()*8)+250)}, lat: {tan(rand())*100}, lon: {tan(rand())*100},  time: {round(rand()*5)} }} )')

    for i in range(0, raw_supplier_count):
        db.execute_query(f'CREATE (rsa:RawSupplierA {{name : "RawSupplierA" + {str(i)}, cost: {round(exp(rand()*3)+20)}, co2: {round(exp(rand()*8)+250)}, lat: {tan(rand())*100}, lon: {tan(rand())*100},  time: {round(rand()*5)} }} )')
        db.execute_query(f'CREATE (rsb:RawSupplierB {{name : "RawSupplierB" + {str(i)}, cost: {round(exp(rand()*3)+20)}, co2: {round(exp(rand()*8)+250)}, lat: {tan(rand())*100}, lon: {tan(rand())*100},  time: {round(rand()*5)} }} )')
    
     log.info("Initialized data in %.2f sec", time.time() - start_time)

    create_relationship(db)

def create_relationship(db):
    db.execute_query(f'MATCH (sa:SuppilerA), (p:Product), (w:Wholesaler), (r:Retailer)' \
                    'CREATE UNIQUE (sa)-[:DELIVER]->(p)-[:DELIVER]->(w)-[:DELIVER]->(r) WITH p, sa' \
                    'MATCH (sb:SupplierB) CREATE UNIQUE (sb)-[:DELIVER]->(p) WITH sb, sa' \
                    'MATCH (ra:RawSuplierA), (rb:RawSupplierB) CREATE UNIQUE (ra)-[:DELIVER]->(sa)' \
                    'CREATE UNIQUE (rb)-[:DELIVER]->(sb)')