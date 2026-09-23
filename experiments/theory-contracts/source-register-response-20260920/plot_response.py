"""Display the actual certified finite-source spectral measure."""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root=Path(__file__).resolve().parent
data=json.loads((root/'certificate.json').read_text())
rows=data['spectral_weights_numeric']['addition']
energies=np.array([r['energy'] for r in rows])
weights=np.array([r['weight'] for r in rows])/3
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans',
                     'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(2,1,figsize=(10,6.4),sharex=True,sharey=True)
fig.patch.set_facecolor('#fbfbf8')
for ax in axes:
    ax.set_facecolor('#fbfbf8')
    ax.grid(axis='y',alpha=.18)
    ax.set_ylim(0,.74)
    ax.set_ylabel('Normiertes Gewicht')
axes[0].vlines(energies,0,weights,color='#137c83',linewidth=2.3)
axes[0].scatter(energies,weights,color='#137c83',s=30,zorder=3)
axes[0].set_title('Tatsächliche geladene Quelle: 13 Pole',loc='left',weight='bold',color='#11666c')
axes[0].annotate('kleinste geladene Energie ≈ 0,654',
                 xy=(energies[0],weights[0]),xytext=(2.65,.49),
                 arrowprops={'arrowstyle':'->','color':'#11666c'},color='#11666c')
axes[1].vlines([1,2],0,[2/3,1/3],color='#a05b2d',linewidth=2.3)
axes[1].scatter([1,2],[2/3,1/3],color='#a05b2d',s=40,zorder=3)
axes[1].set_title('Gegenkontrolle: Randphase eingefroren',loc='left',weight='bold',color='#8c4b20')
axes[1].set_xlabel('Anregungsenergie in Einheiten des vorhandenen Quell-Hamiltonoperators')
axes[1].set_xlim(0,8)
fig.suptitle('Ein geladenes Feld ändert die Randbedingung des besetzten Meeres',
             x=.08,ha='left',y=.975,fontsize=15,weight='bold')
fig.text(.08,.923,'Originaldiagnose: 3 Zellen · 6 Moden · Masse +1 · bedingter gemeinsamer Fock-Lift',fontsize=10)
fig.text(.08,.025,'Hinzufügen und Entnehmen haben hier dasselbe Gesamtspektrum. '
         '13 Pole exakt; dargestellte Gewichte numerisch.\n'
         'Kein thermodynamischer oder 3+1D-Nachweis. UR.SOURCE.REGISTER_RESPONSE.01',fontsize=9,color='#555555')
fig.subplots_adjust(left=.08,right=.98,bottom=.15,top=.85,hspace=.40)
fig.savefig(root/'spektrum.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(root/'spektrum.svg',facecolor=fig.get_facecolor())
