import csv
from pprint import pprint
from collections import defaultdict
from sleeper_wrapper import League


def generate_data_sheets(league_id=516427156663472128):
    league = League(league_id)
    rosters = league.get_rosters()
    users = league.get_users()

    user_map = {user["user_id"]: user["display_name"] for user in users}

    running_scores_by_owner = {}
    weekly_scores_by_weekandowner = defaultdict(dict)
    for week in range(1, 18):
        scores_by_owner = get_scores_by_owner(league, rosters, week)
        calculate_team_totals(
            week,
            scores_by_owner,
            weekly_scores_by_weekandowner,
            running_scores_by_owner,
        )

    for week, scores_by_owner in weekly_scores_by_weekandowner.items():
        with open(f"data/week{week}.csv", "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(
                [
                    "owner",
                    "score",
                    "for",
                    "against",
                    "total score",
                    "total for",
                    "total against",
                ]
            )
            for owner_id, row in scores_by_owner.items():
                csvwriter.writerow([user_map[owner_id]] + [i for i in row])

    with open("data/total.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(
            [
                "owner",
                "total score",
                "total for",
                "total against",
            ]
        )
        rows = [(owner_id, row) for owner_id, row in running_scores_by_owner.items()]
        rows.sort(key=lambda row: row[1][-2], reverse=True)
        for owner_id, row in rows:
            csvwriter.writerow([user_map[owner_id]] + [i for i in row[3:]])

    print("Done")


def _sort_func(score):
    return score[0] if score and score[0] else 0


def calculate_team_totals(
    week, scores_by_owner, weekly_scores_by_weekandowner, running_scores_by_owner
):
    scores = []
    if scores_by_owner:
        scores = [(score, player_id) for player_id, score in scores_by_owner.items()]
        scores.sort(key=_sort_func, reverse=True)

    team_count = len(scores) - 1
    for x in range(team_count + 1):
        score, owner_id = scores[x]
        (
            _,
            __,
            ___,
            running_score,
            running_for,
            running_against,
        ) = running_scores_by_owner.get(owner_id, (0, 0, 0, 0, 0, 0))

        score = score or 0
        score_for = 0
        score_against = 0
        if score > 0:
            running_score += score
            score_for = team_count - x
            running_for += score_for
            score_against = x
            running_against += score_against

        row = (
            round(score, 2),
            round(score_for, 2),
            round(score_against, 2),
            round(running_score, 2),
            round(running_for, 2),
            round(running_against, 2),
        )

        weekly_scores_by_weekandowner[week][owner_id] = row
        running_scores_by_owner[owner_id] = row


def get_scores_by_owner(league: League, rosters, week):
    matchups = league.get_matchups(week)
    roster_id_dict = league.map_rosterid_to_ownerid(rosters)

    scores = {}
    total_score = 0
    for team in matchups:
        current_roster_id = team["roster_id"]
        owner_id = roster_id_dict[current_roster_id]
        score = team["points"]
        if score:
            total_score += score
        scores[owner_id] = score

    if total_score == 0:
        return None
    else:
        return scores


if __name__ == "__main__":
    generate_data_sheets()
