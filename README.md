# Odoo Module : Complaint Management

## 📌 Description
Ce projet est un module personnalisé pour **Odoo 17** permettant de gérer efficacement les plaintes des clients. Il a été développé dans le cadre du **LAB 2 - ERP**.

L'application permet d'enregistrer des plaintes, de les catégoriser (Service, Produit, Autre) et de suivre leur cycle de vie à travers différents états.

## 🚀 Fonctionnalités
- **Gestion des Plaintes** : Enregistrement du sujet, du client et de la description.
- **Cycle de Vie (Workflow)** : Passage des états `Brouillon` (Draft) ➔ `Ouvert` (Open) ➔ `Résolu` (Resolved).
- **Interface Ergonomique** : 
  - Vue Liste avec badges colorés.
  - Vue Formulaire détaillée avec barre de statut.
  - Vue Recherche avec filtres par catégorie et statut.
- **Sécurité** : Droits d'accès configurés pour les utilisateurs internes.

## 🛠️ Installation avec Docker
Le projet est entièrement containerisé pour faciliter le déploiement.

1. **Démarrer les conteneurs** :
   ```bash
   docker-compose up -d
   ```
2. **Accéder à Odoo** : Rendez-vous sur `http://localhost:8069`.
3. **Installer le module** :
   - Activez le **Mode Développeur**.
   - Allez dans **Applications** > **Mettre à jour la liste**.
   - Recherchez "Complaint Management" et cliquez sur **Activer**.

## 📂 Structure du Projet
- `addons/complaint_management/` : Code source du module (Python, XML, CSV).
- `ScreenShots/` : Captures d'écran de l'application.
- `docker-compose.yml` : Configuration de l'environnement Odoo/PostgreSQL.

## 📄 Documentation
Le dossier contient également les rapports détaillés du projet :
- [Rapport Markdown](.gemini/antigravity/brain/778dd700-9b10-4b30-9222-9bc5631269a8/LAB_2_Complaint_Management.md)
- [Source LaTeX du Rapport](.gemini/antigravity/brain/778dd700-9b10-4b30-9222-9bc5631269a8/LAB_2_Complaint_Management.tex)

---
**Réalisé par :** Saida EL AJIMI  
**Encadré par :** Mohammed Aitdaoud  
**Année :** 2025-2026
