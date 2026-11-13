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
4. Si l'entreprise a une adresse mail : brouillon Gmail sur le modèle ci-dessous. Si c'est un formulaire : préparer le message à coller et la liste des fichiers, et envoyer directement à Yasin dans la conversation (SendUserFile) les PDF à téléverser : le CV choisi (`cv-yasin-boukraa-<cv>.pdf` à la racine) et la lettre (`candidature/<slug>/<lettre_pdf>`).
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

## Alertes emploi dans Gmail (à chaque lot)
- Chercher dans Gmail les alertes des 7 derniers jours : `newer_than:7d (from:indeed.com OR from:linkedin.com OR from:hellowork OR from:welcometothejungle OR from:jobteaser)`.
- Garder seulement ce où Yasin peut réellement être pris : vrai stage (pas alternance, pas VIE), 2 à 4 mois possibles, accessible en BUT 2e année (pas « stage ingénieur », pas Bac+4/5 ou Master exigé), pas 6 mois minimum, Île-de-France, réseau / systèmes / support / data. Exclure les écoles, CFA et organismes de formation (ISCOD, Studi, etc.).
- Les pages Indeed et LinkedIn ne sont pas lisibles par les outils : vérifier l'offre sur le site carrières de l'employeur. Si c'est impossible, la lister dans le message final comme « piste à vérifier par Yasin » avec le lien de l'alerte, sans préparer de candidature.
- Une offre vérifiée et valable peut compter dans les 5 cibles du lot.

## Tableau de suivi (Google Sheets sur le Drive de Yasin)
- Fichier unique : https://docs.google.com/spreadsheets/d/1YmmzHb8lhMU_8OPkgO3EAZd-bAupLOtnasm44iQfXh8 (id dans `suivi.json`, champ `drive_file_id`). Ne jamais en créer un autre.
- Le modifier en place avec le connecteur Google Sheets (get_values, update_values, update_spreadsheet). Toujours lire l'onglet avant d'écrire : Yasin peut changer un statut lui-même.
- Onglet « Suivi » : titre en A1, date de mise à jour en A2 (« ... · mis à jour le JJ/MM/AAAA »), en-têtes en ligne 4, une ligne par entreprise à partir de la ligne 5. Colonnes : # | Entreprise | Ville | Type | CV | Mode | Contact | Envoyée le (date) | Statut (liste déroulante) | Dernière réponse | Réponse le (date) | Prochaine action | Page (=HYPERLINK(url;"Voir la page")) | Téléphone.
- Statuts possibles : À envoyer, À vérifier, Envoyée, Relancée, En cours, Entretien, Refus, En pause.
- Colonne Téléphone : seulement un numéro lu sur une page officielle ou dans un mail de l'employeur, avec qui il joint (RH, standard). Ne jamais deviner. Dans le message final, signaler qui vaut le coup d'appeler (réponse en cours, relance due).
- Onglet « Bilan » : formules COUNTIF qui se recalculent seules, rien à modifier.
- Le classeur est en français : séparateur « ; » dans les formules (une virgule donne #ERROR!).
- Nouvelle cible : écrire la ligne juste sous la dernière ligne remplie (la mise en forme, la liste et les couleurs couvrent jusqu'à la ligne 200 ; prolonger les bandes alternées si besoin).
- Garder `_outils/suivi.json` à jour en parallèle (copie de secours dans le repo).

## Relances (à chaque lot)
- Candidature concernée : statut « Envoyée », mode Mail, envoyée il y a 14 jours ou plus, aucune réponse humaine dans Gmail (un accusé de réception automatique ne compte pas comme réponse), et pas encore relancée.
- Ne jamais relancer : Refus, En cours, Entretien, En pause, À vérifier, les candidatures par formulaire, ni une entreprise qui annonce un délai de réponse pas encore écoulé (voir « Prochaine action »).
- Brouillon Gmail en réponse au mail envoyé (replyToMessageId du message envoyé, trouvé dans le dossier Envoyés), jamais d'envoi. Texte court :

  Madame, Monsieur,

  Je me permets de revenir vers vous au sujet de ma candidature pour un stage de <poste>, envoyée le <date>. Je reste très intéressé par <entreprise> et disponible pour un entretien, à votre convenance.

  Ma page de candidature : https://saykito.github.io/Portfolio/candidature/<slug>/

  Bien cordialement,

  Yasin Boukraa
  07 69 08 68 12

- Une seule relance par entreprise. Dans le Google Sheets, colonne « Prochaine action » : « Brouillon de relance prêt (JJ/MM) ». Le statut passe à « Relancée » seulement quand la relance apparaît dans les Envoyés (vérifié au lot suivant), avec la date dans « Prochaine action ».

## Tableau de bord (à chaque lot, en dernier)
- Ajouter le lancement dans `_outils/lancements.json` : date (AAAA-MM-JJ, heure de Paris), heure (« 7h56 »), declenchement (« Automatique » ou « Lancé à la demande »), statut (« Réussi » ou « Échec »), duree_min, entreprises, pages, brouillons, relances.
- `_outils/suivi.json` doit être à jour (copie du Google Sheets).
- Lancer `python3 _outils/tableau_de_bord.py` : écrit `_outils/tableau-de-bord/Tableau_de_bord_candidatures_Yasin_Boukraa.html` et `.pdf` (non publiés sur le site, pas de coordonnées de recruteurs).
- Commiter avec le lot, puis envoyer le PDF et le HTML à Yasin avec SendUserFile.
