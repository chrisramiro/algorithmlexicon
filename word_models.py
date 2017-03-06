import random
import numpy as np
from word import *

def create_score_comparisons(word, chaining, complex):
    comparisons = []
    sense_pool = word.nb_senses[::]
    real_pool = word.bl_senses[::]
    if complex:
        for i in range(len(sense_pool)):
            comparisons += [chaining(real_pool, sense_pool)]
            real_pool.append(sense_pool[0])
            sense_pool = sense_pool[1::]
        return comparisons
    else:
        multiple_bl = []
        for bl in word.bl_senses:
            real_pool = [bl]
            comparisons = []
            for i in range(len(sense_pool)):
                comparisons += [chaining(real_pool, sense_pool)]
                real_pool.append(sense_pool[0])
                sense_pool = sense_pool[1::]
            multiple_bl += [comparisons]
        return max(multiple_bl, key=lambda x: sum(x))


#---------------------------------------------------------------------#
#                               MODELS                                #
#---------------------------------------------------------------------#

def null_probabilities(word):
    num = word.num_nb_senses
    probabilities = []
    for i in range(num):
        probabilities += [1.0/(num - i)]
    return probabilities

def over_all_progenitor(real_pool, sense_pool):
    score_total = sum([calculate_pure_score(real_pool[0], vs_sense) for vs_sense in sense_pool])
    next_score = calculate_pure_score(real_pool[0], sense_pool[0])
    return float(next_score / score_total)

def over_all_exemplar(real_pool, sense_pool):
    def calculate_distance(r_pool, sense):
        score = 0
        for r in r_pool:
            score += calculate_pure_score(r, sense)
        return score

    score_total = sum([calculate_distance(real_pool, vs_sense) for vs_sense in sense_pool])
    next_score = calculate_distance(real_pool, sense_pool[0])
    return float(next_score / score_total)

def over_all_markov(real_pool, sense_pool):
    score_total = sum([calculate_pure_score(real_pool[-1], vs_sense) for vs_sense in sense_pool])
    next_score = calculate_pure_score(real_pool[-1], sense_pool[0])
    return (float) (next_score / score_total)

def over_all_chaining(real_pool, sense_pool):
    score_total = 0
    for s in sense_pool:
        curr = []
        for r in real_pool:
            curr += [calculate_pure_score(r, s)]
        score_total += max(curr)
    next_score = max([calculate_pure_score(r_score, sense_pool[0]) for r_score in real_pool])
    return (float) (next_score / score_total)

def over_all_dynamic(real_pool, sense_pool):
    id = get_prototype_id(real_pool)
    score_total = sum([calculate_pure_score(real_pool[id], vs_sense) for vs_sense in sense_pool])
    next_score = calculate_pure_score(real_pool[id], sense_pool[0])
    return float(next_score / score_total)

#---------------------------------------------------------------------#
#                          HELPER FUNCTIONS                           #
#---------------------------------------------------------------------#

def get_prototype_id(real_pool):
    """A helper function for over_all_dynamic that determines which is the
    prototypical sense for that step in the word's chronology"""

    scores = [0 for i in range(len(real_pool))]
    for j in range(len(real_pool)):
        for i in range(len(real_pool)):
            if i == j:
                scores[j] += np.exp(-(1))
            else:
                scores[j] += calculate_pure_score(real_pool[j], real_pool[i])
    scores = np.array(scores)
    max_v = scores.max()
    max_indices = [i for i, v in enumerate(scores) if v == max_v]
    return random.choice(max_indices)

def calculate_pure_score(s1, s2):
    """Calculates the sense similarity score between any two senses s1, s2.
    A similarity score is minimal if the sense s1 stops existing before s2
    begins.This is under the assumption that s1 is a real_pool and s2 is from a
    sense_pool or real_pool."""

    similarity_score = 0
    list_range = min(len(s1.listed_cat), len(s2.listed_cat))
    denom = sum([len(s1.listed_cat), len(s2.listed_cat)])
    for r in range(list_range):
        if s1.listed_cat[r] == s2.listed_cat[r]:
            similarity_score += 1
        else:
            break
    f_score = float(2 * similarity_score / denom)

    if s1.end_date > s2.date:
        return np.exp(-(1 - f_score))
    else:
        return np.exp(-(1))





