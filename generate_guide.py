from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib import colors
from reportlab.lib.units import cm
import datetime

def create_security_pdf():
    """Crée un PDF de sensibilisation à la sécurité"""
    
    # Nom du fichier
    filename = "Sensibilisation_Securite_Ingenierie_Sociale.pdf"
    
    # Création du document
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Styles personnalisés
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=18,
        textColor=colors.HexColor('#2c3e50'),
        alignment=TA_CENTER,
        spaceAfter=30,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#3498db'),
        spaceBefore=20,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )
    
    subsection_style = ParagraphStyle(
        'SubsectionStyle',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#e74c3c'),
        spaceBefore=15,
        spaceAfter=5,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['BodyText'],
        fontSize=11,
        leading=14,
        alignment=TA_JUSTIFY
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['BodyText'],
        fontSize=11,
        leftIndent=20,
        bulletIndent=10,
        spaceBefore=3,
        spaceAfter=3,
        alignment=TA_LEFT
    )
    
    warning_style = ParagraphStyle(
        'WarningStyle',
        parent=styles['BodyText'],
        fontSize=11,
        textColor=colors.red,
        backColor=colors.HexColor('#FFF3CD'),
        borderPadding=10,
        borderColor=colors.HexColor('#FFEEBA'),
        borderWidth=1,
        leading=14
    )
    
    legal_style = ParagraphStyle(
        'LegalStyle',
        parent=styles['BodyText'],
        fontSize=10,
        textColor=colors.HexColor('#6c757d'),
        fontName='Helvetica-Oblique',
        alignment=TA_JUSTIFY
    )
    
    # Contenu du PDF
    content = []
    
    # === PAGE 1 ===
    content.append(Paragraph("FICHE DE SENSIBILISATION", title_style))
    content.append(Paragraph("INGÉNIERIE SOCIALE & SÉCURITÉ PHYSIQUE", title_style))
    
    content.append(Spacer(1, 30))
    
    # Introduction
    intro_text = """
    <b>Objectif :</b> Cette fiche a pour objectif de sensibiliser l'ensemble du personnel 
    aux risques d'ingénierie sociale et de renforcer les bonnes pratiques de sécurité 
    physique et numérique au sein de l'organisation.
    """
    content.append(Paragraph(intro_text, body_style))
    
    content.append(Spacer(1, 20))
    
    # Section 1: Les 3 attaques principales
    content.append(Paragraph("1. LES 3 ATTAQUES D'INGÉNIERIE SOCIALE LES PLUS COURANTES", section_style))
    content.append(Spacer(1, 10))
    
    # Attaque 1
    content.append(Paragraph("1.1 TAILGATING / PIGGYBACKING", subsection_style))
    tailgating_text = """
    <b>Description :</b> Une personne non autorisée suit un employé légitime pour entrer 
    dans une zone sécurisée sans présenter de badge ou d'identification.
    
    <b>Méthode :</b> L'attaquant profite de la politesse, de la distraction ou de moments 
    d'affluence (pause-café, déjeuner) pour suivre un employé autorisé.
    
    <b>Conséquences :</b> Accès non autorisé aux locaux, vol d'informations, installation 
    de matériel d'écoute, accès aux systèmes informatiques.
    """
    content.append(Paragraph(tailgating_text, body_style))
    content.append(Spacer(1, 15))
    
    # Attaque 2
    content.append(Paragraph("1.2 BAITING / APPÂT NUMÉRIQUE", subsection_style))
    baiting_text = """
    <b>Description :</b> Utilisation d'un appât physique ou numérique pour inciter 
    une victime à exécuter une action compromettante.
    
    <b>Méthode :</b> Clé USB « perdue », CD-ROM « promotionnel », lien trompeur par email, 
    offre trop alléchante en ligne.
    
    <b>Conséquences :</b> Installation de malware, vol de données, prise de contrôle 
    du poste de travail, accès au réseau interne.
    """
    content.append(Paragraph(baiting_text, body_style))
    content.append(Spacer(1, 15))
    
    # Attaque 3
    content.append(Paragraph("1.3 IMPERSONNATION / USURPATION D'IDENTITÉ", subsection_style))
    impersonation_text = """
    <b>Description :</b> L'attaquant se fait passer pour une personne de confiance ou 
    une autorité légitime pour obtenir des informations ou un accès.
    
    <b>Méthode :</b> Appel téléphonique en se faisant passer pour le support IT, 
    technicien de maintenance, cadre supérieur, ou fournisseur.
    
    <b>Conséquences :</b> Divulgation d'informations confidentielles, modification 
    de paramètres de sécurité, autorisation d'accès frauduleuse.
    """
    content.append(Paragraph(impersonation_text, body_style))
    
    content.append(PageBreak())
    
    # === PAGE 2 ===
    content.append(Paragraph("2. BONNES PRATIQUES DE SÉCURITÉ", section_style))
    content.append(Spacer(1, 20))
    
    # Règle 1
    rule1_text = """
    <b>RÈGLE N°1 : NE JAMAIS LAISSER SUIVRE SANS BADGE</b>
    
    • Chaque personne doit présenter son badge d'accès individuel
    • Ne jamais tenir la porte pour un inconnu, même s'il semble pressé
    • Vérifier systématiquement que la porte se referme bien derrière vous
    • Signaler immédiatement toute personne sans badge dans les zones sécurisées
    """
    content.append(Paragraph(rule1_text, body_style))
    content.append(Spacer(1, 15))
    
    # Exemple de scénario
    scenario1_text = """
    <b>Scénario type :</b> Un individu se présente à l'entrée en prétendant avoir oublié 
    son badge. Il vous demande de le laisser passer car il a un rendez-vous urgent 
    avec la direction.
    
    <b>Réponse appropriée :</b>
    1. Lui demander de contacter son interlocuteur pour qu'il vienne le chercher
    2. L'accompagner à la réception pour vérifier son identité
    3. Ne jamais lui donner accès sans vérification formelle
    """
    content.append(Paragraph(scenario1_text, warning_style))
    content.append(Spacer(1, 20))
    
    # Règle 2
    rule2_text = """
    <b>RÈGLE N°2 : NE JAMAIS BRANCHER DE CLÉ USB INCONNUE</b>
    
    • Toute clé USB trouvée doit être remise au service sécurité/système
    • N'utiliser que des périphériques fournis et approuvés par l'entreprise
    • Désactiver l'exécution automatique sur tous les postes de travail
    • Scanner tout périphérique externe avant utilisation
    """
    content.append(Paragraph(rule2_text, body_style))
    content.append(Spacer(1, 15))
    
    # Exemple de scénario
    scenario2_text = """
    <b>Scénario type :</b> Vous trouvez une clé USB dans le parking avec une étiquette 
    "Salaires Décembre 2023 - CONFIDENTIEL".
    
    <b>Réponse appropriée :</b>
    1. Ne pas brancher la clé USB sur votre ordinateur
    2. La remettre immédiatement au service sécurité
    3. Signaler la découverte à votre responsable
    """
    content.append(Paragraph(scenario2_text, warning_style))
    content.append(Spacer(1, 20))
    
    # Règle 3
    rule3_text = """
    <b>RÈGLE N°3 : TOUJOURS VÉRIFIER L'IDENTITÉ D'UN INTERVENANT</b>
    
    • Demander systématiquement une pièce d'identité officielle
    • Vérifier l'autorisation de visite auprès du service concerné
    • Accompagner les visiteurs dans les zones non publiques
    • Ne jamais divulguer d'informations sans autorisation préalable
    """
    content.append(Paragraph(rule3_text, body_style))
    
    content.append(Spacer(1, 20))
    
    # Tableau récapitulatif
    content.append(Paragraph("RÉCAPITULATIF DES BONNES PRATIQUES", subsection_style))
    
    practices_data = [
        ['Situation', 'Action à éviter', 'Action à privilégier'],
        ['Personne sans badge', 'Laisser passer par politesse', 'Demander vérification identité'],
        ['Clé USB trouvée', 'La brancher pour voir le contenu', 'Remettre à la sécurité'],
        ['Technicien inconnu', 'Lui donner accès immédiat', 'Vérifier auprès du service IT'],
        ['Appel "urgent" du support', 'Donner ses identifiants', 'Rappeler sur numéro officiel'],
        ['Email suspect', 'Cliquer sur les liens', 'Signaler à l\'équipe sécurité']
    ]
    
    practices_table = Table(practices_data, colWidths=[5*cm, 5*cm, 5*cm])
    practices_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#dee2e6')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8f9fa')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
    ]))
    
    content.append(practices_table)
    
    # === PAGE 3 ===
    content.append(PageBreak())
    
    content.append(Paragraph("3. CADRE LÉGAL ET RÉFÉRENCES", section_style))
    content.append(Spacer(1, 20))
    
    # Loi 19-05
    legal_text = """
    <b>LOI N° 19-05 DU 10 RAMADHAN 1440 CORRESPONDANT AU 15 MAI 2019</b>
    <i>relative à la protection des personnes physiques dans le traitement des données à caractère personnel</i>
    
    <b>Article 14 : Violation de la vie privée</b>
    
    "Constitue une violation de la vie privée le fait, par tout moyen, de collecter, 
    de traiter, de conserver, d'utiliser ou de divulguer des données à caractère 
    personnel concernant une personne physique sans son consentement exprès, 
    ou en violation des dispositions de la présente loi."
    
    <b>Sanctions prévues :</b>
    • Amende de 100.000 à 1.000.000 DZD
    • Emprisonnement de 6 mois à 2 ans
    • Les deux peines peuvent être cumulées
    
    <b>Responsabilité de l'entreprise :</b>
    En cas de violation de données due à une négligence dans les mesures de sécurité, 
    l'entreprise peut être tenue responsable civilement et pénalement.
    """
    content.append(Paragraph(legal_text, legal_style))
    
    content.append(Spacer(1, 20))
    
    # Obligations des employés
    obligations_text = """
    <b>OBLIGATIONS DES EMPLOYÉS</b>
    
    Conformément à la politique de sécurité de l'entreprise et aux dispositions légales, 
    chaque employé est tenu de :
    
    1. Respecter les procédures de sécurité établies
    2. Signaler immédiatement tout incident ou tentative d'intrusion
    3. Protéger les informations confidentielles dont il a connaissance
    4. Participer aux formations de sécurité organisées
    5. Ne pas contourner les mesures de sécurité mises en place
    """
    content.append(Paragraph(obligations_text, body_style))
    
    content.append(Spacer(1, 20))
    
    # Contacts
    contacts_text = """
    <b>CONTACTS EN CAS D'INCIDENT</b>
    
    • <b>Service Sécurité :</b> extension 1111 | securite@entreprise.dz
    • <b>Support Informatique :</b> extension 2222 | support.it@entreprise.dz
    • <b>Ressources Humaines :</b> extension 3333 | rh@entreprise.dz
    • <b>Urgences 24/7 :</b> 021-XX-XX-XX
    """
    content.append(Paragraph(contacts_text, body_style))
    
    content.append(Spacer(1, 30))
    
    # Signature
    signature_text = """
    <b>ATTESTATION DE PRISE DE CONNAISSANCE</b>
    
    Je soussigné(e), ______________________________________________________,
    certifie avoir pris connaissance du contenu de cette fiche de sensibilisation 
    et m'engage à respecter les bonnes pratiques de sécurité décrites.
    
    Fait à ____________________, le ______/______/________
    
    Signature :
    """
    content.append(Paragraph(signature_text, body_style))
    
    content.append(Spacer(1, 20))
    
    # Footer
    footer_text = """
    <i>Document interne - Version 1.0 - {date}
    Diffusion restreinte - Ne pas copier sans autorisation</i>
    """.format(date=datetime.datetime.now().strftime("%d/%m/%Y"))
    
    content.append(Paragraph(footer_text, 
        ParagraphStyle('FooterStyle', parent=styles['BodyText'], fontSize=8, 
                      textColor=colors.gray, alignment=TA_CENTER)))
    
    # Génération du PDF
    doc.build(content)
    print(f"✅ PDF généré avec succès : {filename}")
    print(f"📄 Nombre de pages : 3")
    print(f"📏 Format : A4")
    print(f"📋 Contenu inclus :")
    print(f"   - 3 attaques d'ingénierie sociale détaillées")
    print(f"   - 3 bonnes pratiques avec exemples concrets")
    print(f"   - Référence légale Loi 19-05 Article 14")
    print(f"   - Tableau récapitulatif des bonnes pratiques")
    print(f"   - Formulaire de prise de connaissance")

if __name__ == "__main__":
    create_security_pdf()



