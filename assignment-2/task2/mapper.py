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



def similarity(p_vector, q_vector, cache=None):
    p_dot_q = 0
    p_sum = 0
    q_sum = 0
    
    for i in range(6):
        p_dot_q += p_vector[i] * q_vector[i]

        p_sum += p_vector[i] ** 2
        q_sum += q_vector[i] ** 2

    
    sim = p_dot_q / (p_sum + q_sum - p_dot_q)
    return sim


def contribution(p, q, num_outgoing_links):
    sim_p_q = similarity(
        page_embeddings[str(p)],
        page_embeddings[str(q)]
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

    print(node, 0)

    for value in values:
        print(value, contribution(node, int(value), len(values)))