#!/usr/bin/env python3
import sys
from json import loads
from pathlib import Path


w_path = Path(sys.argv[1])
page_embedding_path = Path(sys.argv[2])

ranks = {}
page_embeddings = loads(page_embedding_path.read_text())



with w_path.open() as f:
    lines = f.readlines()

    for line in lines:
        node, rank = line.strip().split(",")
        ranks[int(node)] = float(rank)

CACHE = {}


def similarity2(p_vector, q_vector, cache=None):
    p_dot_q = 0
    p_sum = 0
    q_sum = 0
    
    for i in range(6):
        p_dot_q += p_vector[i] * q_vector[i]

        p_sum += p_vector[i] ** 2
        q_sum += q_vector[i] ** 2

    sim = p_dot_q / (p_sum + q_sum - p_dot_q)
    return sim


def similarity(p, q, cache):
    p_vector = page_embeddings[str(p)]
    q_vector = page_embeddings[str(q)]
    p_dot_q = 0
    p_sum = 0
    q_sum = 0
    
    n = len(p_vector)

    i = 0
    kernel_size = 6
    bound = n - kernel_size + 1

    while i < bound:
        p_dot_q += p_vector[i] * q_vector[i]
        p_dot_q += p_vector[i+1] * q_vector[i+1]
        p_dot_q += p_vector[i+2] * q_vector[i+2]
        p_dot_q += p_vector[i+3] * q_vector[i+3]
        p_dot_q += p_vector[i+4] * q_vector[i+4]
        p_dot_q += p_vector[i+5] * q_vector[i+5]
        

        if not cache:
            p_sum += p_vector[i] ** 2
            p_sum += p_vector[i+1] ** 2
            p_sum += p_vector[i+2] ** 2
            p_sum += p_vector[i+3] ** 2
            p_sum += p_vector[i+4] ** 2
            p_sum += p_vector[i+5] ** 2
        q_sum += q_vector[i] ** 2
        q_sum += q_vector[i+1] ** 2
        q_sum += q_vector[i+2] ** 2
        q_sum += q_vector[i+3] ** 2
        q_sum += q_vector[i+4] ** 2
        q_sum += q_vector[i+5] ** 2

   
        i += kernel_size
    
    while i < n:
        p_dot_q += p_vector[i] * q_vector[i]

        if not cache:
            p_sum += p_vector[i] ** 2
        q_sum += q_vector[i] ** 2
        i += 1

    if p not in CACHE:
        CACHE[p] = p_sum

    sim = p_dot_q / (CACHE[p] + CACHE[q] - p_dot_q)
    return sim

def contribution2(p, q, num_outgoing_links):
    sim_p_q = similarity2(
        page_embeddings[str(p)],
        page_embeddings[str(q)]
    )
    rank_p = ranks[p]

    return (rank_p * sim_p_q) / num_outgoing_links

def contribution(p, q, num_outgoing_links):
    sim_p_q = similarity(
        p,
        q
    )
    rank_p = ranks[p]

    return (rank_p * sim_p_q) / num_outgoing_links


def total_contributions(node, values):
    sum_contribs = 0
    num_outgoing_links = len(values)

    for value in values:
        sum_contribs += contribution(node, int(value), num_outgoing_links)

    return sum_contribs


for line in sys.stdin:
    node, values = line.strip().split(maxsplit=1)
    node = int(node)
    values = loads(values)

    # print(node, 0)

    for value in values:
        print(contribution(node, int(value), len(values)))
        
    
    print()