import pandas as pd

def find_best_XI(folder):
    teamsacr = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
    teamsacr_before2022=['CSK','DC','KKR','MI','PBKS','RR','RCB','SRH'] 
    if (int(folder)<2023):
        teamsacr = teamsacr_before2022
    all_data=pd.DataFrame()
    #folder="2022" #input from user

    for team in teamsacr:
        bat_stats=pd.read_csv(f"../{folder}/{team}_Batstats.csv")
        player_details=pd.read_csv(f"../{folder}/{team}_players.csv")
        bowl_stats=pd.read_csv(f"../{folder}/{team}_Bowlstats.csv")
        bat_stats["player_name"]=bat_stats["player_name"].str.upper()
        bowl_stats["player_name"]=bowl_stats["player_name"].str.upper()
        bat_stats=pd.merge(bat_stats,player_details,on=["player_name"])
        complete_stats=pd.merge(bat_stats,bowl_stats,on=["player_name"],how="outer").fillna(0)
        all_data=pd.concat([all_data,complete_stats],ignore_index=True)
    #print(all_data)
    all_data["total_score_bat"]=all_data["Runs_x"]*1.5+all_data["4s"]*0.5+all_data["6s"]-all_data["BF"]*0.5
    all_data["total_score_bat"]/=10
    all_data["total_score_bat"]+=(all_data["SR_x"]-120)/10+(all_data["Avg_x"]-30)/5
    #all_data=all_data.sort_values(by="total_score_bat",ascending=False)

    all_data["total_score_bowl"]=all_data["Wkts"]*20-all_data["Econ"]*2-all_data["SR_y"]*0.5-all_data["Avg_y"]*2
    all_data["total_score_bowl"]/=10
    #all_data=all_data.sort_values(by="total_score_bowl",ascending=False)
    all_round=all_data.loc[all_data["player_role"]=="All-Rounder"]
    all_round["total_score"]=all_round["total_score_bat"]+all_round["total_score_bowl"]
    batsmen=all_data.loc[all_data["player_role"]=="Batter"]
    bowlers = all_data.loc[all_data["player_role"]=="Bowler"]
    wks = all_data.loc[all_data["player_role"]=="WK Keeper - Batter"].sort_values("total_score_bat",ascending=False).head(1)
    all_round=all_round.sort_values("total_score",ascending=False).head(3)
    batsmen=batsmen.sort_values("total_score_bat",ascending=False).head(4)
    bowlers=bowlers.sort_values("total_score_bowl",ascending=False).head(3)

    t=dict(pd.concat([batsmen,wks,all_round,bowlers],ignore_index=True)["player_name"])
    return (t)
