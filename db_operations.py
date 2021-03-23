import logging
from math import tan
from math import exp
from random import random
import time

log = logging.getLogger(__name__)

def clear_database(db):
    """Clear the database."""

    db.execute_query("MATCH (n) DETACH DELETE n")
    log.info("Database cleared")

def init_data(db, raw_supplier_count, supplier_count):
    start_time = time.time()
    db.execute_query(f'CREATE (p:Product {{ name : "Product", lat: {tan(random())*100}, lng: {tan(random())*100}, co2: {200}, cost: {100}, time: {0}}} )')
    
    for i in range(0, 2):
        db.execute_query(f'CREATE (w:Wholesaler {{name : "Wholesaler" + {str(i)}, cost: {round(exp(random()*3)+20)}, co2: {round(exp(random()*8)+250)}, lat: {tan(random())*100}, lng: {tan(random())*100},  time: {round(random()*5)} }} )')

    for i in range(0, supplier_count):
        db.execute_query(f'CREATE (sa:SupplierA {{name : "SupplierA" + {str(i)}, cost: {round(exp(random()*3)+20)}, co2: {round(exp(random()*8)+250)}, lat: {tan(random())*100}, lng: {tan(random())*100},  time: {round(random()*5)} }} )')
    
    for i in range(0, int(supplier_count/2)):
        db.execute_query(f'CREATE (sb:SupplierB {{name : "SupplierB" + {str(i)}, cost: {round(exp(random()*3)+20)}, co2: {round(exp(random()*8)+250)}, lat: {tan(random())*100}, lng: {tan(random())*100},  time: {round(random()*5)} }} )')
    
    for i in range(0, 2*raw_supplier_count):
        db.execute_query(f'CREATE (r:Retailer {{name : "Retailer" + {str(i)}, cost: {round(exp(random()*3)+20)}, co2: {round(exp(random()*8)+250)}, lat: {tan(random())*100}, lng: {tan(random())*100},  time: {round(random()*5)} }} )')

    for i in range(0, raw_supplier_count):
        db.execute_query(f'CREATE (rsa:RawSupplierA {{name : "RawSupplierA" + {str(i)}, cost: {round(exp(random()*3)+20)}, co2: {round(exp(random()*8)+250)}, lat: {tan(random())*100}, lng: {tan(random())*100},  time: {round(random()*5)} }} )')
        db.execute_query(f'CREATE (rsb:RawSupplierB {{name : "RawSupplierB" + {str(i)}, cost: {round(exp(random()*3)+20)}, co2: {round(exp(random()*8)+250)}, lat: {tan(random())*100}, lng: {tan(random())*100},  time: {round(random()*5)} }} )')
    
    log.info("Initialized data in %.2f sec", time.time() - start_time)

    create_relationship(db)

def create_relationship(db):
    db.execute_query('MATCH (sa:SupplierA), (p:Product) CREATE (sa)-[:DELIVER]->(p)')
    db.execute_query('MATCH (p:Product), (w:Wholesaler )CREATE (p)-[:DELIVER]->(w)')
    db.execute_query('MATCH (w:Wholesaler), (r:Retailer) CREATE (w)-[:DELIVER]->(r)')
    db.execute_query('MATCH (sb:SupplierB), (p:Product) CREATE (sb)-[:DELIVER]->(p)')
    db.execute_query('MATCH (ra:RawSuplierA), (sa:SupplierA) CREATE (ra)-[:DELIVER]->(sa) ')
    db.execute_query('MATCH (sb:SupplierB), (rb:RawSupplierB) CREATE (rb)-[:DELIVER]->(sb)')