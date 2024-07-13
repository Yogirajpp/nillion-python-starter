from nada_dsl import *


def nada_main():

    # 0. Constants for configuration
    number_of_voters = 3
    number_of_candidates = 2

    # 1. Initialize parties
    voter_parties = [
        Party(name=f"VoterParty{idx}") for idx in range(number_of_voters)
    ]
    result_party = Party(name="ResultParty")

    # 2. Initialize inputs
    votes_count_per_candidate = [
        [
            SecretUnsignedInteger(
                Input(name=f"vote_{voter}_candidate_{candidate}", party=voter_parties[voter])
            ) for voter in range(number_of_voters)
        ] for candidate in range(number_of_candidates)
    ]

    # 3. Calculate results
    final_counts = []
    for candidate in range(number_of_candidates):
        total_votes = votes_count_per_candidate[candidate][0]
        for voter in range(1, number_of_voters):
            # Aggregate votes for candidate
            total_votes += votes_count_per_candidate[candidate][voter]
        # 4. Output final vote counts
        final_counts.append(
            Output(total_votes, f"final_count_candidate_{candidate}", result_party)
        )

    return final_counts
