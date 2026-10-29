# Méthode de candidature de stage : Yasin Boukraa

Ce dossier commence par `_` : GitHub Pages ne le publie pas.

## Profil
- BUT Informatique 2e année, IUT de Marne-la-Vallée (Université Gustave Eiffel), 1re année validée.
- Paris, permis B, véhiculé. yasin.boukraa0@gmail.com, 07 69 08 68 12.
- Compétences réelles (n'en inventer aucune) : TCP/IP, adressage IP, DHCP, DNS, routage, VLAN, Cisco Packet Tracer, Wireshark, ping/traceroute/ipconfig, Linux Debian, Bash, SSH, Apache, VirtualBox/VMware, SQL/PostgreSQL, MCD/MLD, Python, Java, PHP, HTML/CSS/JS, Git.
- Expérience : gestion locative saisonnière (Djerba Sans Vis-à-Vis) depuis 2023, en saison.
- Ne maîtrise PAS encore : Active Directory, administration de serveurs Windows, Microsoft 365 en entreprise. Le dire honnêtement comme « ce que je viens apprendre ».

## Stage recherché
- Phrase exacte : « Je recherche un stage de 2 mois minimum, débutant en avril 2027 jusqu'à fin août 2027. » Ne jamais mentionner d'heures.
- Réseau / systèmes / support en priorité, data en alternative. Paris et toute l'Île-de-France. Tous types de structures.

## Sélection (5 cibles par lot)
1. Offres publiées récentes ET candidatures spontanées.
2. Vérifier la date : pas d'offre retirée, pas d'offre non datée introuvable sur le site, pas d'adresse mail tirée d'une annonce de plus d'un an sans confirmation récente.
3. Exclure : stages de 6 mois minimum, niveau Bac+4/5 exigé, alternance.
4. Exclure les écoles privées, organismes de formation et CFA qui publient de fausses offres pour recruter des élèves (OpenClassrooms, Studi, etc.).
5. Pas de doublon avec le doc de suivi.

## Pour chaque cible
1. Ajouter une entrée dans `_outils/candidatures.json` (même structure que les existantes) :
   `name`, `poste`, `lieu` (ville des locaux de l'entreprise), `cv` (`technicien` | `reseaux` | `data`),
   `lettre_pdf` (`lettre-yasin-boukraa-<slug>.pdf`), `objet`, `match` (3 triplets : titre, ce que fait l'entreprise, ce que Yasin sait faire),
   `apprendre`, `projets` (3 parmi net, boot, bdd, old, java, graph), `paras` (4 paragraphes de lettre), `date` (date du jour, ex. « 21 octobre 2026 »).
   Optionnel : `hello`, `ref`, `chez`, `att` pour les tournures (voir Mission Locale).
   Choix du CV : technicien = support/systèmes et réseaux généraliste ; reseaux = orienté réseau/infra ; data = données/BDD.
2. Lancer `python3 _outils/build.py <slug>` : génère `candidature/<slug>/index.html` et la lettre PDF (vérifier « lettre sur 1 page »).
3. Commit + push sur `main`. Page en ligne : `https://saykito.github.io/Portfolio/candidature/<slug>/` (vérifier qu'elle répond).
4. Si l'entreprise a une adresse mail : brouillon Gmail sur le modèle ci-dessous. Si c'est un formulaire : préparer le message à coller et la liste des fichiers.
5. Mettre à jour le doc de suivi (ligne du tableau + section avec mail et lettre).
6. Ne jamais envoyer : Yasin relit et envoie lui-même.

## Modèle de mail (brouillon Gmail)
Objet : `Candidature spontanée : stage <poste> (avril à août 2027)` (sans « spontanée » si c'est une offre publiée)

Madame, Monsieur,

Étudiant en 2e année de BUT Informatique à l'IUT de Marne-la-Vallée, je me permets de vous adresser ma candidature [spontanée] pour un stage de <poste> au sein de <entreprise>. Je recherche un stage de 2 mois minimum, débutant en avril 2027 jusqu'à fin août 2027.

<Paragraphe adapté : leur activité réelle, 2 ou 3 projets de Yasin, expérience client, permis B et véhiculé.>

J'ai préparé une page dédiée à ma candidature chez <entreprise>, avec ma lettre de motivation, mon CV et les projets liés au poste :
https://saykito.github.io/Portfolio/candidature/<slug>/

Mon CV en PDF : https://saykito.github.io/Portfolio/cv-yasin-boukraa-<cv>.pdf
Mon portfolio complet : https://saykito.github.io/Portfolio/

Je serais ravi d'échanger avec vous à l'occasion d'un entretien. Je vous remercie pour l'attention portée à ma candidature.

Bien cordialement,

Yasin Boukraa
07 69 08 68 12
yasin.boukraa0@gmail.com

Note : le connecteur Gmail réécrit les liens en redirection Google. Le signaler à Yasin, qui peut recoller les liens lui-même avant d'envoyer.

## Tableau Excel de suivi (Google Drive)
- Source : `_outils/suivi.json` (une ligne par entreprise : nom, ville, type, CV, mode, contact, date d'envoi, statut, dernière réponse, date de réponse, prochaine action, slug).
- Statuts possibles : À envoyer, À vérifier, Envoyée, Relancée, En cours, Entretien, Refus, En pause.
- À chaque changement (nouvelle cible, envoi, réponse) : mettre à jour `suivi.json` (et `maj`), lancer `python3 _outils/suivi_xlsx.py`, recalculer le fichier (script recalc du skill xlsx), puis l'envoyer sur le Drive de Yasin sous le titre « Suivi candidatures stage 2027 - Yasin Boukraa.xlsx » (create_file, base64, disableConversionToGoogleType = true), mettre le trash_file sur l'ancien `drive_file_id` et enregistrer le nouvel id dans `suivi.json`.
- Le connecteur Drive ne permet pas de remplacer le contenu d'un fichier : le lien change à chaque mise à jour, le nom reste le même.
