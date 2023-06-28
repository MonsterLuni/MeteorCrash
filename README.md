# MeteorCrash
MeteorCrash is a game that i made in Python for the Module 122

# Wie kann man spielen?
Das Skript funktioniert nur, wenn man Python heruntergeladen hat und sich die nachfolgenden Packets herunterlädt:

pygame -> pip install pygame

mysql.connector -> pip install mysql.connector

# Spiel & UI 

## Menu
Der Blaue punkt ist dafür da, Vollbild an und aus zu toggeln.
Der Grüne Punkt ist dafür da, das Spiel zu starten.

## Spiel
Es gibt 2 Elemente die statisch sind. Diese sind zwei wichtige Objekte in die man fahren kann ohne dass man stirbt.

## Sammelobjekte
Der Grüne ist ein Powerup mit dem man ein wenig schneller wird in der x und y Richtung.
Der Goldene ist dafür da, einen Meteor (die herunterfallenden Dinge) zu zerstören.

## Highscore Speichern
Man kann seinen Highscore im Game-Over menu und oder im Win menu speichern. 
Dazu gibt man seinen Namen in der Input Box an, und drückt danach aus der Box hinaus, 
wenn das getan ist muss man noch "s" drücken damit es gespeichert wird. 

Man merkt dass es speichern konnte wenn das Programm sich automatisch schliesst.

## Ende des Spiels
Das ende des Spiels ist erreicht nachdem man es geschafft hat 216 Sekunden lang zu überleben, was ziemlich schwierig ist. 
Wenn man es jedoch schafft wird bei deinem Highscore angezeigt, dass du es auch wirklich zuende geschafft hast (Win = True) 

## Wie wird eigentlich der Score berechnet?
Der Score zählt jeden Frame hoch, solange man "W" gedrückt hält, das blöde daran ist nur,
dass man dies ja tun muss, sodass man nicht ins Schwarze Loch reinfällt.

# Lore
Das Spiel handelt um eine weit entwickelte Weltraumspezies die im Jahre 3299 nach Mexus (das ist ihr Gott) einen riesigen Fehler begangen hat.
Sie haben kürzlich erst einen durchbruch in der Quantenforschung erlebt. Dabei haben sie herausgefunden wie man sich durch Quanten Tunneling Teleportieren kann.
Was sie jedoch nicht geahnt haben ist, dass solche Teleportationen eine nicht gleich erhebliche Chance haben das Raum-zeit-kontinuum zu zerstören. Man kann es ihnen
jedoch auch nicht verübeln, wer hätte denn das annehmen sollen?

An einem friedlichen Sonntag Abend ist es dann passiert. 
Ein kleiner Junge der nichts besonderes ist, hat ohne die Erlaubnis seiner Eltern im Spacemobil von gegenüber wie wild auf verschiedenen komisch aussehenden Knöpfen rumgedrückt von denen er nichtmal wusste was sie tun. 
"SCHPLOING" hat es gemacht, und schwupps war alles was er jemals kannte ausgelöscht. In einem schwarzen Loch verschwunden. 
Sein Spacemobil konnte sich noch weg teleportieren, jedoch beherrscht der Junge die Steuerung nicht, und kann deswegen nicht entkommen. 
Das einzige was er drücken konnte ist der Alarmknopf der Hilfe schickt. Es dauert aber leider ganze 216 Sekunden bis die Hilfe ankommt und den Jungen rettet, 
da die Galaktische Föderation in diesem Viertel der Andromeda vor 3.14 Galaktischen Jahren (Ein Galaktisches Jahr entspricht etwa 3.14 menschen Jahren) eine Hyperraum-Umgehungsstrasse gebaut hat.
