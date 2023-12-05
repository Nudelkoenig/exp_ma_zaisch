'''
Content file for exp_pretest_ma_zaisch.

Author: Johannes Rollwage
'''

welcome_instruction = """
Vielen Dank für dein Interesse an unserem Experiment und deine Teilnahme. 

In diesem Experiment wirst du 20 Allgemeinwissensfragen beantworten, bei welchen du oft schätzen musst. 
<br>
Eine Frage könnte zum Beispiel sein: <b>Wie hoch ist das Kolosseum in Rom? </b>
<br><br>
Sehr wahrscheinlich weißt du die richtige Antwort (48m) nicht, aber du kannst eine ungefähre Schätzung abgeben, 
wie z.B. 30m. Bei manchen Fragen kannst du vielleicht besser schätzen als bei anderen. 
<br><br>
Das Experiment wird etwa 30 - 45 Minuten dauern und du erhältst <b>7€</b> oder <b>1 Versuchspersonenstunde </b>
als feste Vergütung für deine Teilnahme. Zusätzlich hast du, falls dir die Rolle der:s <b>Entscheidungsträger:in</b>
 zugewiesen wird, die Chance bis zu <b>3€</b> als Bonus zu erhalten.
<br><br>
Bitte schalte dein Handy aus oder auf lautlos und hole es während des Experiments [auch in Wartezeiten] nicht raus.
Es ist für das Experiment wichtig, dass du die Fragen nicht googelst, und, wenn du es nicht weißt, schätzt. 
<br><br>
Bei Fragen oder Anmerkungen kannst du dich jederzeit bei der Versuchsleitung melden.
<br><br>
Wir wünschen dir viel Spaß bei der Bearbeitung
<br>
Rebecca Schmitz und Alina Zain
"""

informed_consent_content = dict(
    title="Informationen für Teilnehmende",
    experimenter_in_charge="Dr. Johannes Rollwage",
    experimenter_in_charge_email="rollwage@psych.uni-goettingen.de",
    privacy_officer="Herr Prof. Dr. Wiebe",
    privacy_officer_email="datenschutzvorfall@uni-goettingen.de",
    study_email="alina.zain@stud.uni-goettingen.de",
    consent_accept_label="Akzeptieren",
    consent_reject_label="Ablehnen",

    # language=HTML
    introduction="""Liebe Teilnehmende, wir bitten dich um deine Einwilligung in die 
    Erhebung und Verarbeitung der im Rahmen dieser Studie erhobenen Daten.
    """,

    # language=HTML
    experiment_info="""<span style="font-size: 1.4em; "><b>Informationen zur Studie</b>
        </span>
        <br>
        In dieser Studie wirst du in zwei Versuchsabschnitten eine Reihe von numerischen 
        Schätzaufgaben bearbeiten. Im Anschluss bitten wir dich um die Beantwortung einiger
        zusätzlicher Fragen. Die Bearbeitungsdauer beträgt ca. 30 - 45 Minuten. Psychologiestudierende können sich
        für ihre Teilnahme eine Versuchspersonenstunde bescheinigen lassen.
        <br><br>
        <b>Deine Teilnahme ist selbstverständlich freiwillig.</b> Es steht dir frei, die 
        Teilnahme jederzeit ohne Angabe von Gründen abzubrechen. Bei Fragen zur Studie oder 
        den Teilnahmeinformationen wende dich bitte an <span style="color: blue; ">
        alina.zain@stud.uni-goettingen.de</span>. Verantwortlich für diese Studie ist Dr. Johannes Rollwage 
        (rollwage@psych.uni-goettingen.de).
        """,

    anonymity_info="""<b>Eine nachträgliche Verknüpfung von Forschungsdaten mit Merkmalen, 
        die einen direkten Rückschluss auf Ihre Person zulassen, ist im vorliegenden Versuch 
        nicht möglich!</b>""",
    # language=HTML
    personal_data_info="""Auf der nächsten Seite dieses Versuchs werden wir deine E-Mailadresse abfragen, 
        um deine Teilnahme zu dokumentieren.
        Zusätzlich werden wir am Ende dieser Studie deinen Vornamen, Nachnamen und nochmals deine 
        E-Mail-Adresse sowie ggf. deine Anschrift und Kontoverbindung abfragen, diese personenbezogenen Daten dienen dazu, 
        um dir deine Versuchspersonenstunden auszustellen bzw. dich monetär für deine Teilnahme zu vergüten. <br>
    """,
    # language=HTML
    data_disclaimer="""Die <b>anonymen</b> Forschungsdaten werden für die Erstellung von 
        wissenschaftlichen Forschungsarbeiten und Vorträgen genutzt. Diese Arbeiten werden 
        veröffentlicht. In den Veröffentlichungen ist die Zuordnung von Forschungsdaten zu einzelnen 
        Personen ausgeschlossen. Anonymisierte Daten können ebenfalls im Sinne einer transparenten und 
        offenen Wissenschaft Dritten zur Verfügung gestellt werden. Personenbezogene Daten werden 
        grundsätzlich nicht an Dritte weitergegeben.""",
    # language=HTML
    consent="""<span style="font-size: large; "><b>Einwilligungserklärung zur Datenerhebung und Datenverarbeitung</b></span>
        <br><br>
        Ich erkläre mich damit einverstanden, dass im Rahmen dieser Studie mich betreffende 
        personenbezogene Daten/Angaben durch die Versuchsleitung erhoben und verarbeitet werden. 
        Mir ist bekannt, dass die erhobenen personenbezogenen Daten gelöscht werden, sobald dies 
        nach dem Forschungs- oder Statistikzweck möglich ist. Von dieser Löschung nicht betroffen 
        sind anonymisierte Daten, die keinen Rückschluss auf meine Person zulassen. <br>
        Ich bin auch damit einverstanden, dass die Studienergebnisse in anonymer Form 
        veröffentlicht werden. Mir ist bekannt, dass ich jederzeit mein Einverständnis ohne Angabe 
        von Gründen und ohne nachteilige Folgen für mich zurückziehen und eine Löschung der von 
        mir erhobenen Daten verlangen kann. Mir ist jedoch klar, dass eine Löschung bereits 
        anonymisierter Daten nicht mehr möglich sein wird. Mir ist bekannt, dass meine Angaben in 
        Übereinstimmung mit §4 BDSG behandelt werden.
        <br><br>
        Der Verantwortliche für diese Studie und die Datenerhebung ist:
        <br>
        {experimenter_in_charge} ({experimenter_in_charge_email}).
        <br><br>
        Der für diese Studie verantwortliche Datenschutzbeauftragte ist der Datenschutzbeauftragte 
        der Georg-August-Universität Göttingen, {privacy_officer}. <br>
        Datenschutzverstöße und -probleme kann ich jederzeit unter folgender E-Mail-Adresse melden:
        {privacy_officer_email}
        <br><br>
        Mir ist bekannt, dass ich bezogen auf die Verarbeitung meiner personenbezogenen Daten ein 
        Beschwerderecht bei einer Datenschutz-Aufsichtsbehörde (Landesbeauftragte für den 
        Datenschutz Niedersachsen, Prinzenstraße 5, 30159 Hannover) habe. Mir ist zudem bekannt, 
        dass ich ein Recht auf Auskunft über meine verarbeiteten personenbezogenen Daten habe, 
        einschließlich einer unentgeltlichen Kopie dieser Daten. Dieses Auskunftsrecht besteht 
        gegenüber dem genannten Verantwortlichen. Weiterhin ist mir bekannt, dass ich ein Recht 
        auf Berichtigung sowie auf Löschung meiner verarbeiteten personenbezogenen Daten habe. 
        Ich willige ein, dass meine Angaben in Übereinstimmung mit Art. 6 DSGVO behandelt werden.
        <br> <br>
        Ich habe diesbezüglich keine weiteren Fragen mehr und willige hiermit in die dargestellte 
        Untersuchung ein. Alle mich interessierenden Fragen wurden ausreichend geklärt.
        <br><br>
        <b>Notiz:</b> Wenn du auf 'Akzeptieren' klickst, wird das Experiment sofort starten. Klicke 
        auf 'Ablehnen', um das Experiment zu beenden, ohne dass deine persönlichen Daten 
        aufgezeichnet werden.""",
    consent_reject_title="Consent: Rejected",
    consent_reject_icon="times-circle",
    # The following text needs a {study_email} placeholder!
    # language=HTML
    consent_reject_message="""Du hast das Experiment abgebrochen.
        <br><br>
        Du kannst diese Seite jetzt schließen.
        <br><br>
        Wenn Du Fragen hast, schreib uns bitte eine Mail an 
        <span style="color: blue; ">{study_email}</span>""",
)

screening_page_content = dict(
    title="Teilnahmeregistrierung",
    button_text="Registrieren",
    screening_info=(
        "Bevor du an dieser Studie teilnehmen kannst, müssen wir sicher gehen, dass "
        "du nicht bereits an dieser oder einer ähnlichen Studie teilgenommen hast. "
        "Dazu möchten wir dich bitten, deine E-Mailadresse einzutragen. Dies dient "
        "gleichzeitig der Dokumentation deiner Teilnahme."
    ),
    email_instruction="Deine E-Mailadresse:",
    email_pattern=r"[^@]+@[^@]+\.[^@]+",
    email_match_hint="Bitte gib eine gültige E-Mailadresse ein",
    data_protection_info=(
        "Deine hier eingegebene E-Mail-Adresse wird getrennt von deinem "
        "Experimentaldatensatz und in einer kodierten Form, die keine Nutzung für "
        "andere Zwecke als den Abgleich mit E-Mailadressen von anderen Teilnehmenden "
        "ermöglicht, gespeichert."
    ),
    exclusion_title="Teilnahme nicht möglich",
    exclusion_icon="times-circle",
    exclusion_message="Leider kannst du an diesem Experiment nicht teilnehmen, da du "
                      "bereits an dieser oder einer sehr ähnlichen Studie teilgenommen "
                      "hast.<br><br>"
                      "Bei Fragen kannst du dich gerne an folgende E-Mail-Adresse wenden: "
                      "alina.zain@stud.uni-goettingen.de",
)

instr_phase_1_title = """
Instruktionen
"""

phase_one_instruction_advisor_block_aware = """
Danke für deine Teilnahme.

In diesem Experiment werden dir 20 Schätzaufgaben gestellt. Die Fragen sind aus unterschiedlichen Wissensgebieten,
 sodass es normal ist, wenn du nicht alle Antworten weißt und raten musst.
 <br><br>
Die Fragen wirst du zusammen mit einem:er Partner:in bearbeiten. Dein:e Partner:in ist mit dir hier im Raum, 
aber ihr wisst nicht, wer mit euch zusammenarbeitet. 
<br><br>
Deine <b>Antwort</b> auf die Frage ist der <b>Ratschlag</b>, den dein:e Partner:in bekommt.
<br><br>
Du bearbeitest zuerst alle Aufgaben allein und erst danach beginnt dein:e Partner:in mit der Bearbeitung der 20 Fragen.
 Danach bekommt er/sie den Ratschlag. Damit kann er/sie seine/ ihre Antwort nochmal überarbeiten. Du bekommst danach 
 eine <b>Rückmeldung</b>, wie die Antwort vor und nach deinem Ratschlag war. Du kannst dann nur sehen, was dein:e 
 Partner:in geantwortet hat, aber <b>nicht mehr deine Ratschläge ändern</b>.
<br><br>
In der Rolle des:der Ratgebers:in erhältst du keine Bonusbezahlung für die Qualität deiner Schätzungen
"""


phase_one_instruction_judge_block_aware = """
Danke für deine Teilnahme.

In diesem Experiment werden dir 20 Schätzaufgaben gestellt. Die Fragen sind aus unterschiedlichen Wissensgebieten,
 sodass es normal ist, wenn du nicht alle Antworten weißt und raten musst.
 <br><br>
Die Fragen wirst du zusammen mit einem:er Partner:in bearbeiten. Dein:e Partner:in ist mit dir hier im Raum, 
aber ihr wisst nicht, wer mit euch zusammenarbeitet. 
<br><br>
Dein:e Partner:in gibt dir <b>Ratschläge</b>. Der Ratschlag ist, was dein:e Partner:in auf die Frage geantwortet hat.
<br><br>
Dein:e Partner:in wird zuerst alle 20 Fragen alleine bearbeiten. Danach beginnst du mit der Bearbeitung. Du beantwortest
 jede Frage erst allein, danach bekommst du den Ratschlag. Damit kannst du deine Antwort nochmal überarbeiten.
  Dein:e Partner:in bekommt anschließend eine <b>Rückmeldung</b>, wie deine Antwort vor und nach dem Ratschlag war. 
<br><br>
Dein:e Partner:in kann die <b>Ratschläge nicht mehr ändern</b> und nicht darauf reagieren, wie du die Ratschläge 
benutzt. 
<br><br>
Wie bereits eingangs gesagt, ist ein Teil deiner Entlohnung für die Teilnahme an unserer Studie erfolgsabhängig. 
Die erfolgsabhängige Entlohnung richtet sich danach, wie gut deine jeweils <b>zweiten Schätzungen</b> sind. 
<br><br>
Für jede Schätzung, die nicht weiter als 10% vom wahren Wert abweicht, erhältst du zusätzlich zu deiner Grundvergütung
 von 7€ einen Bonus von 15 Cent. 
<br>
Insgesamt kannst du also einen Bonus von maximal 3€ erreichen.
"""

phase_one_instruction_advisor_block_unaware = """
Danke für deine Teilnahme.

In diesem Experiment werden dir 20 Schätzaufgaben gestellt. Die Fragen sind aus unterschiedlichen Wissensgebieten,
 sodass es normal ist, wenn du nicht alle Antworten weißt und raten musst.
 <br><br>
Die Fragen wirst du zusammen mit einem:er Partner:in bearbeiten. Dein:e Partner:in ist mit dir hier im Raum, 
aber ihr wisst nicht, wer mit euch zusammenarbeitet. 
<br><br>
Deine <b>Antwort</b> auf die Frage ist der <b>Ratschlag</b>, den dein:e Partner:in bekommt.
<br><br>
 Du bearbeitest zuerst alle Aufgaben allein und erst danach beginnt dein:e Partner:in mit der Bearbeitung der 20 Fragen.
  Danach bekommt er/sie den Ratschlag. Damit kann er/sie seine/ ihre Antwort nochmal überarbeiten.
<br><br>
In der Rolle des:der Ratgebers:in erhältst du keine Bonusbezahlung für die Qualität deiner Schätzungen
"""

phase_one_instruction_judge_block_unaware = """
Danke für deine Teilnahme.

In diesem Experiment werden dir 20 Schätzaufgaben gestellt. Die Fragen sind aus unterschiedlichen Wissensgebieten,
 sodass es normal ist, wenn du nicht alle Antworten weißt und raten musst.
 <br><br>
Die Fragen wirst du zusammen mit einem:er Partner:in bearbeiten. Dein:e Partner:in ist mit dir hier im Raum, 
aber ihr wisst nicht, wer mit euch zusammenarbeitet. 
<br><br>
Dein:e Partner:in gibt dir <b>Ratschläge</b>. Der Ratschlag ist, was dein:e Partner:in auf die Frage geantwortet hat.
<br><br>
Dein:e Partner:in wird zuerst alle 20 Fragen alleine bearbeiten. Danach beginnst du mit der Bearbeitung. Du beantwortest
 jede Frage erst allein, danach bekommst du den Ratschlag. Damit kannst du deine Antwort nochmal überarbeiten.
<br><br>
Deine Antworten sind <b>geheim</b> und dein:e Partner:in erfährt nicht, ob du ihren/seinen Ratschlag genutzt hast.
<br><br>
Wie bereits eingangs gesagt, ist ein Teil deiner Entlohnung für die Teilnahme an unserer Studie erfolgsabhängig. 
Die erfolgsabhängige Entlohnung richtet sich danach, wie gut deine jeweils <b>zweiten Schätzungen</b> sind. 
<br><br>
Für jede Schätzung, die nicht weiter als 10% vom wahren Wert abweicht, erhältst du zusätzlich zu deiner Grundvergütung
 von 7€ einen Bonus von 15 Cent. 
<br>
Insgesamt kannst du also einen Bonus von maximal 3€ erreichen.
"""


phase_one_instruction_advisor_sequence_aware = """
Danke für deine Teilnahme.

In diesem Experiment werden dir 20 Schätzaufgaben gestellt. Die Fragen sind aus unterschiedlichen Wissensgebieten,
 sodass es normal ist, wenn du nicht alle Antworten weißt und raten musst.
 <br><br>
Die Fragen wirst du zusammen mit einem:er Partner:in bearbeiten. Dein:e Partner:in ist mit dir hier im Raum, 
aber ihr wisst nicht, wer mit euch zusammenarbeitet. 
<br><br>
Deine <b>Antwort</b> auf die Frage ist der <b>Ratschlag</b>, den dein:e Partner:in bekommt.
<br><br>
Dein:e Partner:in wird die Frage zuerst alleine bearbeiten. Danach bekommt er/ sie deinen Ratschlag. Damit kann er:sie
 seine:ihre Antwort nochmal überarbeiten. Du bekommst danach eine <b>Rückmeldung</b>, wie die Antwort vor und nach 
 deinem Ratschlag war, und kannst dies bei der nächsten Frage berücksichtigen. 
<br><br>
In der Rolle des:der Ratgebers:in erhältst du keine Bonusbezahlung für die Qualität deiner Schätzungen
"""
phase_one_instruction_judge_sequence_aware = """
Danke für deine Teilnahme.

In diesem Experiment werden dir 20 Schätzaufgaben gestellt. Die Fragen sind aus unterschiedlichen Wissensgebieten,
 sodass es normal ist, wenn du nicht alle Antworten weißt und raten musst.
 <br><br>
Die Fragen wirst du zusammen mit einem:er Partner:in bearbeiten. Dein:e Partner:in ist mit dir hier im Raum, 
aber ihr wisst nicht, wer mit euch zusammenarbeitet. 
<br><br>
Dein:e Partner:in gibt dir <b>Ratschläge</b>. Der Ratschlag ist, was dein:e Partner:in auf die Frage geantwortet hat.
<br><br>
Du und dein:e Partner:in arbeitet immer <b>gleichzeitig</b> an der gleichen Frage. Du beantwortest jede Frage zuerst 
allein, danach bekommst du den Ratschlag. Damit kannst du deine Antwort nochmal überarbeiten. Dein:e Partner:in bekommt
 danach eine <b>Rückmeldung</b>, wie deine Antwort vor und nach dem Ratschlag war. Nachdem dein:e Partner:in diese
 Rückmeldung gesehen hat, beginnt ihr beide damit die nächste Aufgabe zu bearbeiten.
<br><br>
Dein:e Partner:in kann also bei späteren Aufgaben darauf reagieren, wie du die Ratschläge bei den vorherigen Aufgaben
benutzt hast. 
<br><br>
Wie bereits eingangs gesagt, ist ein Teil deiner Entlohnung für die Teilnahme an unserer Studie erfolgsabhängig. 
Die erfolgsabhängige Entlohnung richtet sich danach, wie gut deine jeweils <b>zweiten Schätzungen</b> sind. 
<br><br>
Für jede Schätzung, die nicht weiter als 10% vom wahren Wert abweicht, erhälst du zusätzlich zu deiner Grundvergütung
 von 7€ einen Bonus von 15 Cent. 
<br>
Insgesamt kannst du also einen Bonus von maximal 3€ erreichen.
"""
phase_one_instruction_advisor_sequence_unaware = """
Danke für deine Teilnahme.

In diesem Experiment werden dir 20 Schätzaufgaben gestellt. Die Fragen sind aus unterschiedlichen Wissensgebieten,
 sodass es normal ist, wenn du nicht alle Antworten weißt und raten musst.
 <br><br>
Die Fragen wirst du zusammen mit einem:er Partner:in bearbeiten. Dein:e Partner:in ist mit dir hier im Raum, 
aber ihr wisst nicht, wer mit euch zusammenarbeitet. 
<br><br>
Deine <b>Antwort</b> auf die Frage ist der <b>Ratschlag</b>, den dein:e Partner:in bekommt.
<br><br>
Dein:e Partner:in wird die Frage zuerst alleine bearbeiten. Anschließend bekommt er/ sie deinen Ratschlag. Damit kann 
er/sie seine/ ihre Antwort nochmal überarbeiten. Danach bearbeitet ihr die nächste Frage.
<br><br>
In der Rolle des:der Ratgebers:in erhältst du keine Bonusbezahlung für die Qualität deiner Schätzungen
"""
phase_one_instruction_judge_sequence_unaware = """
Danke für deine Teilnahme.

In diesem Experiment werden dir 20 Schätzaufgaben gestellt. Die Fragen sind aus unterschiedlichen Wissensgebieten,
 sodass es normal ist, wenn du nicht alle Antworten weißt und raten musst.
 <br><br>
Die Fragen wirst du zusammen mit einem:er Partner:in bearbeiten. Dein:e Partner:in ist mit dir hier im Raum, 
aber ihr wisst nicht, wer mit euch zusammenarbeitet. 
<br><br>
Dein:e Partner:in gibt dir <b>Ratschläge</b>. Der Ratschlag ist, was dein:e Partner:in auf die Frage geantwortet hat.
<br><br>
Du und dein:e Partner:in arbeitet immer <b>gleichzeitig</b> an der gleichen Frage. Du beantwortest jede Frage zuerst 
allein, danach bekommst du den Ratschlag. Damit kannst du deine Antwort nochmal überarbeiten.
<br><br>
Deine Antworten sind <b>geheim</b> und dein:e Partner:in erfährt nicht, ob du seinen/ihren Ratschlag genutzt hast.
<br><br>
Wie bereits eingangs gesagt, ist ein Teil deiner Entlohnung für die Teilnahme an unserer Studie erfolgsabhängig. 
Die erfolgsabhängige Entlohnung richtet sich danach, wie gut deine jeweils <b>zweiten Schätzungen</b> sind. 
<br><br>
Für jede Schätzung, die nicht weiter als 10% vom wahren Wert abweicht, erhälst du zusätzlich zu deiner Grundvergütung
 von 7€ einen Bonus von 15 Cent. 
<br>
Insgesamt kannst du also einen Bonus von maximal 3€ erreichen.
"""

phase_one_instruction_greeting = """ 
<br><br>
Falls du jetzt oder später noch Fragen hast, melde dich gerne bei der Versuchsleitung.
<br><br>
Viel Spaß beim Experiment
<br>
Rebecca Schmitz und Alina Zain
"""

phase_two_instruction_advisor_block_aware = """
Vielen Dank für deine Antworten.
<br><br>
Dein:e Partner:in beginnt jetzt mit der Beantwortung der Fragen.
<br><br>
Du bekommst jetzt für jede Frage angezeigt, was dein:e Partner:in geantwortet hat, was dein Ratschlag war und wie 
seine /ihre Antwort am Ende ist. 
<br><br>
Bis du die erste Antwort gezeigt bekommst, kann es einen kleinen Moment dauern. 
<br><br>
Bitte klicke auf weiter, um das Experiment fortzusetzen.
<br>
"""

phase_two_instruction_judge_block= """
Bevor du mit den Fragen loslegen kannst, muss dein:e Partner:in erst alle 20 Fragen beantworten. Diese Antworten sind 
später deine Ratschläge. Das wird zwischen 10 bis 15 Minuten dauern. Bis es soweit ist, siehst du eine „Bitte Warten…“ 
Anzeige. Sobald diese verschwindet, kannst du mit den Fragen starten. 
<br><br>
Bitte nutze in dieser Zeit nicht dein Handy.
<br>
Um die Wartezeit zu verkürzen kannst du dir gerne eine der ausliegenden Zeitschriften nehmen. 
<br>
Vielen Dank für deine Geduld!

"""

final_questionnaire_instruction = """
Du hast nun alle Schätzaufgaben bearbeitet. Bevor das Experiment beendet ist, haben wir auf den
folgenden Seiten noch einige Fragen zu deinem Vorgehen bei der Aufgabenbearbeitung."""

initial_own_accuracy = """
Als wie akkurat würdest du deine ersten Schätzungen im Schnitt einschätzen?
"""

final_own_accuracy = """
Als wie akkurat würdest du deine zweiten Schätzungen im Schnitt einschätzen?
"""

absolut_advice_accuracy = """
Als wie akkurat würdest du die Ratschläge, die du erhalten hast, im Schnitt einschätzen?
"""

relative_advice_accuracy = """
Wie würdest du im Vergleich zu deinen eigenen Schätzungen die Akkuratheit der Ratschläge,
die du erhalten hast, beurteilen? Im Vergleich zu deinen eigenen Schätzungen waren die
Ratschläge...
"""
seriousness_mani_check = """
Hast du die Schätzaufgaben ernsthaft beantwortet?
"""

awareness_mani_check = """
Konnte dein:e Partner:in sehen, wie du seine:ihre Ratschläge verwendet hast?
"""

# Self-reported single item (SRSI) indicator Meade and Craig (2012) and Ward and Pond (2015)
srsi = """
Für diese Studie ist es von entscheidender Bedeutung, dass wir nur Antworten von 
Personen einbeziehen, die ihre volle Aufmerksamkeit dieser Studie gewidmet haben. 
Andernfalls könnten jahrelange Bemühungen (die der Forschenden und die der anderen 
Teilnehmenden) zunichte gemacht werden. 
"""

srsi_question = """
<b>Sollten wir deiner ehrlichen Meinung nach deine Daten in unseren Analysen dieser Studie 
verwenden?</b><br>
"""

graphic_feedback = """
Diese Grafik zeigt dir, wie akkurat du im Vergleich zu den bisherigen Teilnehmende 
die Antworten auf die Allgemeinwissensfragen geschätzt hast. Der <b>Mean Absolute 
Percentage Error (MAPE)</b> entspricht der mittleren prozentualen Abweichung der 
Schätzung von dem tatsächlichen Preis. Folglich ist die Schätzleistung umso besser, je 
kleiner der MAPE ist.
"""

feedback_text = """
Du erhälst nun eine Rückmeldung zu deiner Schätzleistung. Hierzu haben wir die 
durchschnittliche Akkuratheit deiner finalen Schätzungen im zweiten Versuchsabschnitt
berechnet. Die Angabe erfolgt dabei als mittlere prozentuale Abweichung (genauer: Mean 
absolute percentage error). Deine finalen Schätzungen wiesen durchschnittlich folgende
prozentuale Abweichung auf:

<div style="text-align: center;"><b>{mape_self}</b></div>
<br>
Zur besseren Einschätzung dieser Rückmeldung zeigen wir dir nun noch die mittlere
prozentuale Abweichung aller bisherigen Teilnehmenden in dieser Studie:
<br><br>
<div style="text-align: center;"><b>{mape_others}</b></div>

"""

registration_selection_content = dict(
    title="Vergütung",
    statustext="Klick auf 'Weiter', wenn du eine Auswahl getroffen hast.",
    instr_selection="<b>Folgende Vergütungsoptionen stehen zur Auswahl:</b>",
    instr_choice="Bitte entscheide dich für eine Vergütungsoption",
    # The following option needs to be set to the number of options
    # in this dictionary. There can be more options in the dictionary
    # than are shown on the page. You can add configuration blocks for
    # more options and update the available_options setting, whenever
    # necessary
    available_options=5,
    show_option_1=True,
    option_1_instruction="<u>Versuchspersonen-Stunden: </u><br>"
                         "Als Psychologie-Student:in hast du die Möglichkeit, die "
                         " Teilnahme mit 1 Versuchspersonenstunden vergüten zu lassen. "
                         "Zusätzlich erhältst du, falls du Entscheidungsträger:in warst, einen Bonus von bis zu 3€  "
                         "per Überweisung ausgezahlt."
                         " Sofern du dich für diese Vergütungsoption entscheidest, "
                         "benötigen wir auf der nächsten Seite die Eingabe persönlicher"
                         " Informationen (Matrikelnummer, Name, Vorname, "
                         "E-Mail-Adresse, IBAN, Anschrift und Geburtsdatum). Die von dir angegebenen Informationen "
                         "werden vertraulich behandelt und dienen ausschließlich der "
                         "Auszahlung deines Bonus und der Ausstellung deiner Versuchspersonenstunden.",
    option_1_label="VP-Stunden mit Bonus",
    option_1_register_name= True,
    option_1_register_birth_date=True,
    option_1_register_email=True,
    option_1_register_phone=False,
    option_1_register_iban=True,
    option_1_register_address=True,
    option_1_register_various=True,
    option_1_register_payout=True,

    show_option_2=True,
    option_2_instruction="<u>Überweisung</u><br>"
                         "Du erhältst 7€ plus, falls du Entscheidungsträger:in warst, einen Bonus von bis zu 3€ per "
                         "Überweisung ausgezahlt."
                         " Sofern du dich für diese Vergütungsoption entscheidest, benötigen wir auf der nächsten Seite"
                         " die Eingabe persönlicher Informationen (Vorname, Name, E-Mail-Adresse, IBAN, Anschrift und "
                         "Geburtsdatum). Die von dir angegebenen Informationen werden vertraulich behandelt und dienen"
                         " ausschließlich der Auszahlung deiner Versuchspersonenvergütung.",
    option_2_label="Überweisung",
    option_2_register_name=True,
    option_2_register_birth_date=True,
    option_2_register_email=True,
    option_2_register_phone=False,
    option_2_register_iban=True,
    option_2_register_address=True,
    option_2_register_various=False,
    option_2_register_payout=True,

    show_option_3=True,
    option_3_instruction="<u>VP-Stunden ohne Bonus</u><br>"
                         "Als Psychologie-Student:in hast du die Möglichkeit,"
                         " die Teilnahme mit 1 Versuchspersonenstunden vergüten zu lassen, ohne einen Bonus per "
                         "Überweisung zu erhalten. Sofern du dich für diese Vergütungsoption entscheidest, "
                         "benötigen wir auf der nächsten Seite die Eingabe persönlicher"
                         " Informationen (Matrikelnummer, Name, Vorname, "
                         "E-Mail-Adresse). Die von dir angegebenen Informationen "
                         "werden vertraulich behandelt und dienen ausschließlich der "
                         "Ausstellung deiner Versuchspersonenstunden.",
    option_3_label="VP-Stunden ohne Bonus",
    option_3_register_name=True,
    option_3_register_birth_date=False,
    option_3_register_email=True,
    option_3_register_phone=False,
    option_3_register_iban=False,
    option_3_register_address=False,
    option_3_register_various=True,
    option_3_register_payout=False,

    show_option_4=True,
    option_4_instruction="<u>Keine Vergütung</u><br>"
                         "Falls du keine persönlichen Daten angeben möchtest, hast du die Möglichkeit auf eine "
                         "Vergütung zu verzichten.",
    option_4_label="Keine Vergütung",
    option_4_register_name=False,
    option_4_register_birth_date=False,
    option_4_register_email=False,
    option_4_register_phone=False,
    option_4_register_iban=False,
    option_4_register_address=False,
    option_4_register_various=False,
    option_4_register_payout=False,

    show_option_5=False,
    option_5_instruction="This is the instruction for option 5.",
    option_5_label="Itemlabel Option 5",
    option_5_register_name=True,
    option_5_register_birth_date=False,
    option_5_register_email=True,
    option_5_register_phone=False,
    option_5_register_iban=False,
    option_5_register_address=False,
    option_5_register_various=False,
    option_5_register_payout=False,
)

registration_page_content = dict(
    title="Registrierung",
    statustext="Um deine Registrierung zu abzuschließen, klick auf 'Weiter'.",
    instr_no_registration="Wir benötigen keine persönlichen Daten von dir. "
                          "Du kannst auf 'Weiter' klicken.",
    instr_registration="Bitte gib die folgenden persönlichen Informationen ein.",
    first_name_instr="Bitte gib deinen Vornamen ein",
    last_name_instr="Bitte gib deinen Nachnamen ein",
    birth_date_instr="Bitte gib dein Geburtsdatum ein",
    birth_date_pattern=r"^(0[1-9]|[12][0-9]|3[01])[-/.](0[1-9]|1[012])[-/.](19|20)\d\d$",
    birth_date_suffix="TT.MM.JJJJ",
    birth_date_match_hint="Dies ist der Match-Hinweis für das Feld Geburtsdatum.",
    email_instr="Bitte gib deine E-Mail-Adresse ein",
    email_pattern=r"[^@]+@[^@]+\.[^@]+",
    email_match_hint="Bitte gib eine gültige E-Mail-Adresse ein.",
    iban_instr="Bitte gib deine IBAN ein",
    iban_pattern=r"^[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){4}(?:[ ]?[0-9]{1,2})?$",
    iban_match_hint="Fehler: Bitte überprüfe deine Eingabe.",
    bic_instr="Bitte gib deine BIC ein",
    bic_pattern=r"^[a-zA-Z]{6}[0-9a-zA-Z]{2}([0-9a-zA-Z]{3})?$",
    bic_match_hint="Fehler: Bitte überprüfe deine Eingabe.",
    tax_office_instr="Bitte gib den Sitz deines Finanzamtes an.",
    phone_instr="Bitte geben Sie Ihre Telefonnummer ein",
    phone_pattern=r"^\+?(?:[0-9]\x20?){6,14}[0-9]$",
    phone_match_hint="Fehler: Bitte überprüfe deine Eingabe.",
    street_instr="Bitte gib deinen Straßennamen an",
    house_number_instr="Bitte gib deine Hausnummer ein",
    postal_code_instr="Bitte gib deine Postleitzahl ein",
    postal_code_pattern=r"(?i)^[a-z0-9][a-z0-9\- ]{0,10}[a-z0-9]$",
    postal_code_match_hint="Fehler: Bitte überprüfe deine Eingabe.",
    city_instr="Bitte gib den Stadtnamen ein",
    country_instr="Bitte gib den Ländernamen ein",
    various_instr="Bitte gib deine Matrikelnummer ein",
    various_pattern=r"^..*$",  # Anything but empty
    various_match_hint="Fehler: Bitte überprüfe deine Eingabe.",
    privacy_info="This is a dummy text for privacy information",
    repeated_title="Anscheinend hast du bereits an dem Experiment teilgenommen",
    repeated_text="This is a dummy text for the repeated participation page",
    repeated_participation_title="Erneute Teilnahme detektiert",
    repeated_participation_icon="times-circle",
    repeated_participation_message="Es tut uns leid, aber eine wiederholte Teilnahme an diesem "
                                   "Experiment ist nicht erlaubt. Deine persönlichen Daten werden "
                                   "nicht gespeichert",
)

suspicion_check = """
Was wurde deiner Meinung nach in dieser Studie untersucht?
"""

debriefing_text = """
Vielen Dank für deine Teilnahme! Das Experiment ist nun beendet.
Bitte verlasse leise deinen Platz und vergiss deine Wertsachen nicht.
<br> <br>
Falls es dich interessiert, kannst du im folgenden nachlesen, was das Ziel unseres Experiments ist und findest die 
Antworten zu den Allgemeinwissensfragen. 
<br><br>
In diesem Experiment wart ihr entweder zuständig dafür Ratschläge zu geben [Ratgeber:innen] oder mithilfe der 
Ratschläge eure Schätzung zu verbessern [Entscheidungsträger:innen]. 
<br><br>
Bei einer Gruppe sehen die Ratgeber:innen nicht, was mit ihren Ratschlägen passiert. Bei der anderen Gruppe sehen die 
Ratgeber:innen, wie die Entscheidungsträger:innen ihre Ratschläge genutzt haben. Sie sehen nach der Bearbeitung zum 
Beispiel: Wie viele Oskars erhielt der Film „Titanic“?
<br><br>
Die erste Schätzung von deinem:r Partner:in: 5
<br><br>
Dein Ratschlag: 15
<br><br>
Die finale Schätzung von deinem:r Partner:in: 10
<br><br>
Sieht fair aus, oder? Genau dafür interessieren wir uns: was Ratgeber:innen fair finden. Wie wäre es für dich, wenn 
dein Ratschlag einfach ignoriert wird? 
<br><br>
Wir möchten herausfinden, wie stark die Ratschläge berücksichtigt werden müssen, damit du dich als Ratgeber:in fair 
behandelst fühlst.
<br><br>
Außerdem möchten wir herausfinden, ob die Entscheidungsträger:innen die Ratschläge stärker berücksichtigen, wenn sie 
wissen, dass ihr:e Partner:innen sehen können, was mit den Ratschlägen passiert. Klingt auch logisch: Wenn niemand 
sieht, dass du den Ratschlag ignorierst, kann sich auch niemand unfair behandelt fühlen. 
<br><br>
Aber warum genau benutzen die Entscheidungsträger:innen die Ratschläge stärker, wenn es sichtbar ist? In diesem
Experiment haben wir zwei Möglichkeiten dafür untersucht:
<br><br>
A:  Menschen möchten einfach fair handeln und dir für deinen Ratschlag etwas zurückgeben, indem sie deinen Ratschlag
 würdigen
 <br><br>
B: Menschen handeln strategisch und wollen sich nicht die zukünftige Zusammenarbeit verbauen, indem sie ihre 
Partner:innen unfair behandeln. 
<br><br>
Deswegen wurden die Ratschläge bei einer Gruppe alle im Block am Anfang gegeben, bei der anderen würden alle Fragen 
gleichzeitig bearbeitet. Bei der ersten Gruppe können die Ratschläge deswegen nicht verändert werden, wenn die 
Entscheidungsträger:innen unfair handeln. Wenn sie also strategisch sein wollen, können sie die Ratschläge auch 
ignorieren, da es keine zukünftige Zusammenarbeit gibt. Wenn wir aber fair sein wollen, müssen wir auch bei keiner
weiteren Zusammenarbeit die Ratschläge fair wertschätzen. 
<br><br>
Für die Untersuchung unserer Fragestellung ist es wichtig, dass unsere Versuchspersonen 
die konkrete Fragestellung nicht kennen. Da diese und ähnliche Studien noch eine gewisse 
Zeit weiterlaufen werden, würden wir dich daher um Stillschweigen bezüglich des Ziels 
unserer Untersuchung bitten. Wir bitten dich auch Stillschweigen bezüglich der konkreten 
Aufgaben zu bewahren, die du in diesem Versuch bearbeitet hast. Bei weiteren Fragen 
kannst du dich gerne an die Versuchsleitung (alina.zain@stud.uni-goettingen.de) 
wenden.
<br><br>
Wenn es dich interessiert, kannst du hier weiterlesen und die Antworten auf die Fragen finden.
<br><br>
1.	Wie viele Saiten hat eine Konzertharfe? <br>
<b> Antwort:</b> Eine Konzertharfe hat normalerweise 47 Saiten.
<br><br>
2.	Wie groß ist die größte Fliege der Welt (in mm)? <br>
<b> Antwort:</b> Sie ist ungefähr 70 mm groß.
<br><br>
3.	Was ist die Höchstgeschwindigkeit, die Delfine erreichen können (in km/h)? <br>
<b> Antwort:</b> Delfine können höchstens 55 km/h schwimmen.
<br><br>
4.	Wie viel Krill frisst ein Blauwal pro Tag (in Tonnen)? <br>
<b> Antwort:</b> Ein Blauwal frisst 16 Tonnen Krill, wenn er kann.
<br><br>
5.	Wie viel kostete das iPhone5 32GB bei seiner Einführung 2012 (in Euro)? <br>
<b> Antwort:</b> Das iPhone kostete 789€.
<br><br>
6.	Wie viele Menschen haben 2019 den Gipfel des Mount Everest bestiegen? <br>
<b> Antwort:</b> Insgesamt 878 Menschen.
<br><br>
7.	Wie viele Kalorien hat ein Big Mac? <br>
<b> Antwort:</b> Ein Big Mac hat 495 Kalorien.
<br><br>
8.	Wie viel Kalorien haben 250 ml Sprite? <br>
<b> Antwort:</b> Es sind insgesamt 94 Kalorien.
<br><br>
9.	Wie schnell ist die schnellste Wasserschildkröte (km/h)? <br>
<b> Antwort:</b> Bis zu 35 km/h schnell kann eine Lederschildkröte schwimmen.
<br><br>
10.	Wie viele Erdnüsse braucht man für ein Glas Erdnussbutter? <br>
<b> Antwort:</b> Man braucht ca. 600 Erdnüsse.
<br><br>
11.	Wie viele Kg Kartoffeln isst eine Person in Deutschland  durchschnittlich pro Jahr? <br>
<b> Antwort:</b> Ungefähr 60 Kg pro Jahr.
<br><br>
12.	Wie viel Liter Wein trinkt eine Person in Deutschland durchschnittlich pro Jahr? <br>
<b> Antwort:</b> Durchschnittlich 20 Liter Wein.
<br><br>
13.	Wie viele Tasten hat ein Klavier? <br>
<b> Antwort:</b> Ein Klavier hat 88 Tasten.
<br><br>
14.	Wie viele Oscars erhielt der Film “Titanic”? <br>
<b> Antwort:</b> Insgesamt 11 und viele weitere Auszeichnungen.
<br><br>
15.	Wie alt war Queen Elisabeth II bei ihrer Krönung? <br>
<b> Antwort:</b> Sie war 27 Jahre alt.
<br><br>
16.	Aus wie vielen einzelnen Knochen besteht die menschliche Hand? <br>
<b> Antwort:</b> Eine Hand besteht aus 27 Knochen.
<br><br>
17.	Wie hoch hängt der Ring eines Basketballkorbs (in cm)? <br>
<b> Antwort:</b> Die obere Kante ist 305 cm über dem Boden. 
<br><br>
18.	Wie viele Buchseiten hat die gesamte deutsche Version der Harry Potter Reihe? <br>
<b> Antwort:</b> Insgesamt sind es 4.192 Seiten.
<br><br>
19.	Wie tief ist Loch Ness (in m)?<br>
<b> Antwort:</b> Loch Ness ist 230m tief.
<br><br>
20.	Wie lange dauert der längste Flug, den Lufthansa planmäßig anbietet? <br>
<b> Antwort:</b> Der Flug dauert 14 Stunden und geht von Frankfurt nach Buenos Aires.
<br><br>

Noch einmal herzlichen Dank für deine Teilnahme!
"""

end_text = """
Die Erhebung ist nun abgeschlossen.

Sie können diese Seite nun schließen.
"""