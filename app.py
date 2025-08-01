import pandas as pd
from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import seaborn as sns           

df = pd.read_csv('./data/chris-paul.csv')

app = Flask(__name__)

points_data = df[['Season', 'PTS']].sort_values('Season')
points_peak = points_data.loc[points_data['PTS'].idxmax()]
plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")
sns.lineplot(data=points_data, x='Season', y='PTS', marker='o', color='#1f77b4', linewidth=2)
plt.scatter(points_peak['Season'], points_peak['PTS'], s=200, marker='*', color='gold', edgecolor='black', zorder=5)
plt.annotate(f"{points_peak['PTS']}",
             xy=(points_peak['Season'], points_peak['PTS']),
             xytext=(12, 0),
             textcoords='offset points',
             ha='left', va='center',
             fontsize=14, fontweight='bold',
             color='black',
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=1))
plt.xticks(rotation=45, fontsize=12)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Points per Game', fontsize=14)
plt.title('Chris Paul Points per Season', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig('./static/chris-paul-pts.png', dpi=300)
plt.close()

assists_data = df[['Season', 'AST']].sort_values('Season')
assists_peak = assists_data.loc[assists_data['AST'].idxmax()]
plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")
sns.lineplot(data=assists_data, x='Season', y='AST', marker='o', color='#2ca02c', linewidth=2)
plt.scatter(assists_peak['Season'], assists_peak['AST'], s=200, marker='*', color='gold', edgecolor='black', zorder=5)
plt.annotate(f"{assists_peak['AST']}",
             xy=(assists_peak['Season'], assists_peak['AST']),
             xytext=(12, 0),
             textcoords='offset points',
             ha='left', va='center',
             fontsize=14, fontweight='bold',
             color='black',
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=1))
plt.xticks(rotation=45, fontsize=12)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Assists per Game', fontsize=14)
plt.title('Chris Paul Assists per Season', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig('./static/chris-paul-ast.png', dpi=300)
plt.close()

rebound_data = df[['Season', 'TRB']].sort_values('Season')
rebound_peak = rebound_data.loc[rebound_data['TRB'].idxmax()]
plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")
sns.lineplot(data=rebound_data, x='Season', y='TRB', marker='o', color='#ff7f0e', linewidth=2)
plt.scatter(rebound_peak['Season'], rebound_peak['TRB'], s=200, marker='*', color='gold', edgecolor='black', zorder=5)
plt.annotate(f"{rebound_peak['TRB']}",
             xy=(rebound_peak['Season'], rebound_peak['TRB']),
             xytext=(12, 0),
             textcoords='offset points',
             ha='left', va='center',
             fontsize=14, fontweight='bold',
             color='black',
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=1))
plt.xticks(rotation=45, fontsize=12)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Rebounds per Game', fontsize=14)
plt.title('Chris Paul Rebounds per Season', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig('./static/chris-paul-trb.png', dpi=300)
plt.close()

steals_data = df[['Season', 'STL']].sort_values('Season')
steals_peak = steals_data.loc[steals_data['STL'].idxmax()]
plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")
sns.lineplot(data=steals_data, x='Season', y='STL', marker='o', color='#d62728', linewidth=2)
plt.scatter(steals_peak['Season'], steals_peak['STL'], s=200, marker='*', color='gold', edgecolor='black', zorder=5)
plt.annotate(f"{steals_peak['STL']}",
             xy=(steals_peak['Season'], steals_peak['STL']),
             xytext=(12, 0),
             textcoords='offset points',
             ha='left', va='center',
             fontsize=14, fontweight='bold',
             color='black',
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=1))
plt.xticks(rotation=45, fontsize=12)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Steals per Game', fontsize=14)
plt.title('Chris Paul Steals per Season', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig('./static/chris-paul-stl.png', dpi=300)
plt.close()
