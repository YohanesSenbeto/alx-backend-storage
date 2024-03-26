#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    """Total number of logs"""
    total_logs = collection.count_documents({})

    """Number of logs for each method"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    """Number of logs for method=GET and path=/status"""
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    """"Display stats"""
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}:", count)
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
