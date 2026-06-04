#!/usr/bin/env python3
"""8-all module"""


def list_all(mongo_collection):
    """List all documents in a collection"""
    documents = list(mongo_collection.find())
    if not documents:
        return []
    return documents
