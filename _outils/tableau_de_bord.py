#!/usr/bin/env python3
"""Génère le tableau de bord des candidatures (HTML autonome + PDF), à envoyer par mail.
Usage (depuis la racine du repo) : python3 _outils/tableau_de_bord.py
Lit : _outils/suivi.json (copie du Google Sheets), _outils/candidatures.json (date de chaque lot),
      _outils/lancements.json (une entrée par lancement de la tâche planifiée).
Écrit : _outils/tableau-de-bord/Tableau_de_bord_candidatures_Yasin_Boukraa.html et .pdf
Sans coordonnées des recruteurs. Ce dossier commence par _ : GitHub Pages ne le publie pas."""
import json, html, os, datetime
from collections import Counter, OrderedDict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
O = os.path.join(ROOT, "_outils")
E = html.escape
MOIS = {m: i+1 for i, m in enumerate("janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split())}
def iso_fr(s):  # "19 octobre 2026" -> "2026-10-19"
    j, m, a = s.split(); return f"{int(a):04d}-{MOIS[m]:02d}-{int(j):02d}"
def iso_num(s):  # "14/10/2026" -> "2026-10-14"
    if not s: return None
    j, m, a = s.split("/"); return f"{a}-{m}-{j}"
def fr(iso):
    if not iso: return ""
    a, m, j = iso[:10].split("-"); return f"{j}/{m}/{a}"
suivi = json.load(open(os.path.join(O, "suivi.json"), encoding="utf-8"))
cands = json.load(open(os.path.join(O, "candidatures.json"), encoding="utf-8"))
runs = json.load(open(os.path.join(O, "lancements.json"), encoding="utf-8"))
PREMIER = "2026-10-14"
auto = {r["date"] for r in runs if r.get("statut") == "Réussi"}
dates = sorted({iso_fr(c["date"]) if c.get("date") else PREMIER for c in cands.values()} | {PREMIER})
lotnum = {d: i+1 for i, d in enumerate(dates)}
rows = []
for i, l in enumerate(suivi["lignes"]):
    l = l + [""] * 12
    slug = l[11]
    d = iso_fr(cands[slug]["date"]) if slug in cands and cands[slug].get("date") else PREMIER
    rows.append(dict(num=i+1, entreprise=l[0], ville=l[1], type=l[2], cv=l[3], lot=f"Lot {lotnum[d]}", lot_date=d,
        origine="Tâche planifiée" if d in auto else "Manuel", envoyee_le=iso_num(l[6]), statut=l[7],
        derniere_reponse=l[8] or None, page=f"https://saykito.github.io/Portfolio/candidature/{slug}/" if slug else None))
MAJ = suivi.get("maj", "")
total=len(rows); env=sum(1 for r in rows if r['envoyee_le'])
rep=sum(1 for r in rows if r['envoyee_le'] and r['statut'] in ('En cours','Refus','Entretien'))
taux=round(rep*100/env); enc=sum(r['statut']=='En cours' for r in rows); ae=sum(r['statut']=='À envoyer' for r in rows)
lots=OrderedDict()
for r in sorted(rows,key=lambda r:r['lot_date']): lots.setdefault(r['lot'],[r['lot_date'],r['origine'],0]); lots[r['lot']][2]+=1
c=Counter(r['statut'] for r in rows)
ordre=['Envoyée','Relancée','En cours','Entretien','Refus','À envoyer','À vérifier','En pause']
ordre+= [s for s in c if s not in ordre]
ACC='#1F6FB2'; MUT='#B8C4D0'; BAD='#C0392B'
def bars(items, lw=120, W=460):
    rh=30; H=rh*len(items)+4; mx=max(v for _,v,_ in items)
    out=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" xmlns="http://www.w3.org/2000/svg">']
    for i,(lab,v,col) in enumerate(items):
        y=4+i*rh; w=max(2,(W-lw-40)*v/mx)
        out.append(f'<text x="0" y="{y+rh/2}" dominant-baseline="middle" font-size="13" fill="#555">{E(lab)}</text>'
                   f'<rect x="{lw}" y="{y+6}" width="{w:.1f}" height="{rh-12}" rx="3" fill="{col}"/>'
                   f'<text x="{lw+w+6:.1f}" y="{y+rh/2}" dominant-baseline="middle" font-size="13" font-weight="600" fill="#222">{v}</text>')
    out.append('</svg>'); return ''.join(out)
st=bars([(s,c[s],BAD if s=='Refus' else (MUT if s in('En pause','À vérifier') else ACC)) for s in ordre if s in c])
lt=bars([(f"{k} · {fr(v[0])[:5]}",v[2],ACC if v[1]=='Tâche planifiée' else MUT) for k,v in lots.items()])
pill={'En cours':'ok','Entretien':'ok','Refus':'bad','À envoyer':'warn','À vérifier':'warn'}
trs=''.join(f"<tr><td>{r['num']}</td><td>{E(r['entreprise'])}</td><td>{E(r['ville'])}</td><td>{E(r['type'])}</td><td>{E(r['cv'])}</td><td>{r['lot'][4:]}</td><td class=nw>{fr(r['envoyee_le'])}</td><td><span class='pill {pill.get(r['statut'],'')}'>{E(r['statut'])}</span></td><td>{E(r['derniere_reponse'] or '')}</td><td>{'<a href=\"'+r['page']+'\">Voir</a>' if r['page'] else ''}</td></tr>" for r in rows)

JOURS = "lundi mardi mercredi jeudi vendredi samedi dimanche".split()
def jour(iso):
    d = datetime.date.fromisoformat(iso); return f"{JOURS[d.weekday()]} {d.day} {list(MOIS)[d.month-1]} {d.year}"
pr = {"Réussi": "ok", "Échec": "bad"}
runrows = "".join(f"<tr><td class=nw>{jour(r['date'])}, {E(r.get('heure',''))}</td><td>{E(r.get('declenchement',''))}</td><td><span class='pill {pr.get(r.get('statut'),'')}'>{E(r.get('statut',''))}</span></td><td>{r.get('duree_min','')} min</td><td>{r.get('entreprises','')}</td><td>{r.get('pages','')}</td><td>{r.get('brouillons','')}</td><td>{r.get('relances','')}</td></tr>" for r in runs)
kp=lambda k,v,s: f'<div class=card><div class=k>{k}</div><div class=v>{v}</div><div class=s>{s}</div></div>'
doc=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tableau de bord, candidatures de stage automatisées, Yasin Boukraa</title>
<style>
body{{font-family:Segoe UI,Calibri,Arial,sans-serif;color:#1a1a1a;background:#f5f7fa;margin:0}}
.w{{max-width:1050px;margin:0 auto;padding:32px 24px}}
h1{{font-size:28px;margin:0 0 6px}} h2{{font-size:18px;margin:0 0 10px;color:#1F4E79}}
.lead{{color:#444;margin:4px 0}} .note{{color:#777;font-size:13px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0}}
.card,.box{{background:#fff;border:1px solid #dde3ea;border-radius:8px;padding:16px}}
.k{{font-size:13px;color:#666}} .v{{font-size:34px;font-weight:600;margin:4px 0}} .s{{font-size:12px;color:#888}}
.two{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px;margin-bottom:16px}}
.leg{{font-size:12px;color:#666;margin-top:6px}} .leg i{{display:inline-block;width:10px;height:10px;border-radius:2px;margin:0 5px 0 12px;vertical-align:-1px}}
table{{border-collapse:collapse;width:100%;font-size:13px}} th{{text-align:left;color:#555;border-bottom:2px solid #dde3ea;padding:6px 8px;white-space:nowrap}}
td{{border-bottom:1px solid #eef1f4;padding:6px 8px;vertical-align:top}} .nw{{white-space:nowrap}} .sc{{overflow-x:auto}}
.pill{{display:inline-block;padding:1px 8px;border-radius:999px;border:1px solid #ccd;white-space:nowrap;font-size:12px}}
.pill.ok{{border-color:#2e8b57;color:#2e8b57}} .pill.bad{{border-color:#C0392B;color:#C0392B}} .pill.warn{{border-color:#c98a00;color:#a06e00}}
ol{{margin:6px 0 0;padding-left:20px;color:#333}} li{{margin:3px 0}} a{{color:#1F6FB2}}
@media print{{body{{background:#fff}} .w{{padding:0}} .box,.card{{break-inside:avoid}} tr{{break-inside:avoid}}}}
</style></head><body><div class=w>
<h1>Candidatures de stage automatisées</h1>
<p class=lead>Yasin Boukraa, BUT Informatique 2e année, IUT de Marne-la-Vallée (Université Gustave Eiffel).</p>
<p class=lead><b>{total}</b> entreprises suivies en <b>{len(lots)}</b> lots hebdomadaires, <b>{env}</b> candidatures envoyées et <b>{rep}</b> réponses d'employeurs reçues.</p>
<p class=note>Stage recherché : 2 mois minimum, d'avril à fin août 2027, en réseaux et systèmes ou en data, en Île-de-France. Données au {MAJ}, tirées du suivi Google Sheets et de l'historique GitHub.</p>
<div class=kpis>{kp('Entreprises suivies',total,'depuis le '+fr(PREMIER))}{kp('Candidatures envoyées',env,'par moi, après relecture')}{kp("Réponses d'employeurs",rep,'en cours ou refus, hors accusés automatiques')}{kp('Taux de réponse',f'{taux} %','réponses / candidatures envoyées')}{kp('Dossiers en cours',enc,"à l'étude chez l'employeur")}{kp('Prêtes à envoyer',ae,'brouillons Gmail à relire')}</div>
<div class=two><div class=box><h2>Où en sont les candidatures</h2>{st}</div>
<div class=box><h2>Entreprises ajoutées par lot</h2>{lt}<div class=leg><i style="background:{MUT};margin-left:0"></i>Préparé à la main en conversation<i style="background:{ACC}"></i>Tâche planifiée</div></div></div>
<div class=box style="margin-bottom:16px"><h2>La tâche planifiée</h2>
<p class=lead>Chaque lundi à 7h56, une session Claude se lance seule et prépare le lot de la semaine. Elle n'envoie jamais rien : je relis chaque brouillon et je l'envoie moi-même.</p>
<ol><li>Lit le suivi Google Sheets et Gmail pour ne pas recontacter une entreprise et mettre à jour les réponses reçues.</li>
<li>Cherche 5 entreprises qui prennent des stagiaires BUT, avec une adresse de recrutement publiée.</li>
<li>Génère une page de candidature et une lettre PDF par entreprise, et les publie sur GitHub Pages.</li>
<li>Ajoute une ligne par entreprise dans le suivi Google Sheets.</li>
<li>Crée un brouillon Gmail personnalisé, avec le lien vers la page et le bon CV en pièce jointe.</li>
<li>Prépare un brouillon de relance pour chaque candidature restée sans réponse depuis 2 semaines.</li>
<li>Met à jour ce tableau de bord.</li></ol>
<div class=sc style="margin-top:12px"><table><tr><th>Lancement</th><th>Déclenchement</th><th>Statut</th><th>Durée</th><th>Entreprises</th><th>Pages publiées</th><th>Brouillons Gmail</th><th>Relances préparées</th></tr>
{runrows}</table></div></div>
<div class=box><h2>Détail par entreprise</h2><div class=sc><table><tr><th>#</th><th>Entreprise</th><th>Ville</th><th>Type</th><th>CV</th><th>Lot</th><th>Envoyée le</th><th>Statut</th><th>Dernière réponse</th><th>Page</th></tr>{trs}</table></div>
<p class=note>Les adresses et numéros des recruteurs sont volontairement retirés.</p></div>
</div></body></html>'''
OUT = os.path.join(O, "tableau-de-bord"); os.makedirs(OUT, exist_ok=True)
H = os.path.join(OUT, "Tableau_de_bord_candidatures_Yasin_Boukraa.html")
open(H, "w", encoding="utf-8").write(doc)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto("file://" + H)
    pg.pdf(path=H[:-5] + ".pdf", format="A4", landscape=True, print_background=True, margin={"top": "12mm", "bottom": "12mm", "left": "10mm", "right": "10mm"})
    b.close()
print("ok", total, "entreprises,", env, "envoyées,", rep, "réponses,", taux, "%")
