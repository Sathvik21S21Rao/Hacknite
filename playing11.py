import csv
import pandas as pd
def find_best_teamXI(team,folder):

    # team='PBKS' #input from the site
    # folder="2019"
    bat_stats=pd.read_csv(f"{folder}/{team}_Batstats.csv")
    player_details=pd.read_csv(f"{folder}/{team}_players.csv")
    bowl_stats=pd.read_csv(f"{folder}/{team}_Bowlstats.csv")
    bat_stats["player_name"]=bat_stats["player_name"].str.upper()
    bowl_stats["player_name"]=bowl_stats["player_name"].str.upper()
    bat_stats=pd.merge(bat_stats,player_details,on=["player_name"])
    bowl_stats=pd.merge(bowl_stats,player_details,on=["player_name"])
    bat_stats["total_score_bat"]=bat_stats["Runs"]*1.5+bat_stats["4s"]*0.5+bat_stats["6s"]-bat_stats["BF"]*0.5
    bat_stats["total_score_bat"]/=10
    bat_stats["total_score_bat"]+=(bat_stats["SR"]-120)/10+(bat_stats["Avg"]-30)/5
    bat_stats=bat_stats.sort_values(by="total_score_bat",ascending=False)
    bowl_stats["total_score_bowl"]=bowl_stats["Wkts"]*20-bowl_stats["Econ"]*2-bowl_stats["SR"]*0.5-bowl_stats["Avg"]*2
    bowl_stats["total_score_bowl"]/=10
    bowl_stats=bowl_stats.sort_values(by="total_score_bowl",ascending=False)
    all_stats=pd.merge(bat_stats,bowl_stats,on="player_name",how="outer").fillna(0)
    all_stats["total_score"]=all_stats["total_score_bat"]+all_stats["total_score_bowl"]
    all_stats=all_stats.loc[all_stats["player_role_x"]=="All-Rounder"].sort_values(by="total_score",ascending=False)
    t=dict(pd.concat([bat_stats.loc[bat_stats["player_role"]=="Batter"].head(4),bat_stats.loc[bat_stats["player_role"]=="WK Keeper - Batter"].head(1),all_stats.loc[all_stats["player_role_x"]=="All-Rounder"].head(3),bowl_stats.loc[bowl_stats["player_role"]=="Bowler"].head(3),],ignore_index=True)["player_name"])
    lt=3
    while(len(t)<=10):
        k=bowl_stats.loc[bowl_stats["player_role"]=="Bowler"]
        p = k.iloc[lt]["player_name"]
        lt=lt+1
        t[len(t)]=p
    return t 
if __name__=="__main__":
    teamsacr = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
    teamsacr_before2022=['CSK','DC','KKR','MI','PBKS','RR','RCB','SRH']
    print(find_best_teamXI("CSK",2020))
